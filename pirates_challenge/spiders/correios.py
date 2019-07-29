from scrapy.http import FormRequest
from scrapy import Spider
from scrapy.selector import Selector
from functools import partial
from ..items import RecordItemLoader, UfItemLoader
from .contants import *

class CorreiosSpider(Spider):

    name = 'correios'
    start_urls = [
        'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm'
    ]
    created_ufs = {}

    def parse(self, response):
        for uf_option_value in response.xpath("//select[@class='f1col']/option/@value"):
            uf_selected = uf_option_value.get()
            if uf_selected is not '':

                formdata = {FORMDATA_UF : uf_selected}
                if uf_selected not in self.created_ufs.keys():
                    ufloader = UfItemLoader(selector=Selector(response))
                    ufloader.add_value('uf', uf_selected)
                    self.created_ufs[uf_selected] = ufloader

                yield FormRequest.from_response(response,
                                                formname=FORMNAME_GERAL,
                                                formdata=formdata,
                                                callback=partial(self.parse_result,uf_selected=uf_selected))

    def parse_result(self, response, uf_selected):
        result_tables = response.xpath(".//table[@class='tmptabela']")

        table_content = result_tables[0]
        if len(result_tables) > 1:
            table_content = result_tables[1]

        record_loader = RecordItemLoader(selector=Selector(response))
        for td_index in range(len(table_content.xpath(".//tr/td").getall())):
            if (td_index % 4) == 0:
                record_loader.add_value('location', table_content.xpath(".//tr/td").getall()[td_index])
            if (td_index % 4) == 1:
                record_loader.add_value('zip', table_content.xpath(".//tr/td").getall()[td_index])

        formdata = {
            FORMDATA_UF: uf_selected,
            FORMDATA_LOCALIDADE: FORMDATA_ALL_VALUES
        }

        if self.created_ufs[uf_selected].load_item().get('record') is None:
            self.created_ufs[uf_selected].load_item()['record'] = record_loader.load_item()
        else:
            self.created_ufs[uf_selected].load_item()['record']['location'].extend(record_loader.load_item()['location'])
            self.created_ufs[uf_selected].load_item()['record']['zip'].extend(record_loader.load_item()['zip'])

        next_page_form = response.xpath("//form[@name='Proxima']").extract_first()
        if next_page_form is not None:
            yield FormRequest.from_response(response,
                                            formname=FORMNAME_PROXIMA,
                                            formdata=formdata,
                                            callback=partial(self.parse_result, uf_selected=uf_selected))
        else:
            yield self.created_ufs[uf_selected].load_item()

