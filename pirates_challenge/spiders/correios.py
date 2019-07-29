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
            if self.is_not_uf_table(uf_selected):

                formdata = {FORMDATA_UF: uf_selected}
                self.set_ufitemloader(response, uf_selected)

                yield FormRequest.from_response(response,
                                                formname=FORMNAME_GERAL,
                                                formdata=formdata,
                                                callback=partial(self.parse_result,uf_selected=uf_selected))

    def is_not_uf_table(self, uf_selected):
        return uf_selected is not ''

    def set_ufitemloader(self, response, uf_selected):
        if uf_selected not in self.created_ufs.keys():
            ufloader = UfItemLoader(selector=Selector(response))
            ufloader.add_value(ITEM_FIELD_UF, uf_selected)
            self.created_ufs[uf_selected] = ufloader

    def parse_result(self, response, uf_selected):
        result_tables = response.xpath(".//table[@class='tmptabela']")

        table_content = self.get_table_content(result_tables)

        record_loader = RecordItemLoader(selector=Selector(response))
        for td_index in range(len(table_content.xpath(".//tr/td").getall())):
            self.set_record_loader(record_loader, table_content, td_index)

        formdata = {FORMDATA_UF: uf_selected, FORMDATA_LOCALIDADE: FORMDATA_ALL_VALUES}

        self.set_record_item(record_loader, uf_selected)

        yield from self.yield_result(formdata, response, uf_selected)

    def yield_result(self, formdata, response, uf_selected):
        next_page_form = response.xpath("//form[@name=" + FORMNAME_PROXIMA + "]").extract_first()
        if next_page_form is not None:
            yield FormRequest.from_response(response,
                                            formname=FORMNAME_PROXIMA,
                                            formdata=formdata,
                                            callback=partial(self.parse_result, uf_selected=uf_selected))
        else:
            uf_item = self.created_ufs[uf_selected].load_item()
            yield uf_item

    def set_record_item(self, record_loader, uf_selected):
        uf_item = self.created_ufs[uf_selected].load_item()
        record_item = record_loader.load_item()
        
        if uf_item.get(ITEM_FIELD_RECORD) is None:
            uf_item[ITEM_FIELD_RECORD] = record_item
        else:
            uf_item[ITEM_FIELD_RECORD][ITEM_FIELD_LOCATION].extend(record_item[ITEM_FIELD_LOCATION])
            uf_item[ITEM_FIELD_RECORD][ITEM_FIELD_ZIP].extend(record_item[ITEM_FIELD_ZIP])

    def get_table_content(self, result_tables):
        table_content = result_tables[0]
        if len(result_tables) > 1:
            table_content = result_tables[1]
        return table_content

    def set_record_loader(self, record_loader, table_content, td_index):
        total_columns = 4
        location_index = 0
        zip_index = 1
        
        column_content = table_content.xpath(".//tr/td").getall()[td_index]
        if (td_index % total_columns) == location_index:
            record_loader.add_value(ITEM_FIELD_LOCATION, column_content)
        elif (td_index % total_columns) == zip_index:
            record_loader.add_value(ITEM_FIELD_ZIP, column_content)

