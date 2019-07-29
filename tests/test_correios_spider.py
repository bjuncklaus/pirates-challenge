import unittest
from pirates_challenge.spiders.correios import CorreiosSpider
from scrapy.selector import Selector
from pirates_challenge.items import RecordItemLoader, UfItemLoader
from requests.models import Response

class TestCorreiosSpider(unittest.TestCase):

    # def test_get_table_content_should_return_second_element(self):
    #     correios = CorreiosSpider()
    #
    #     result_tables = ["first_element", "second_element", "third_element"]
    #     expected_result = "second_element"
    #
    #     actual = correios.get_table_content(result_tables)
    #     self.assertEqual(expected_result, actual)
    #
    # def test_get_table_content_should_return_single_element(self):
    #     correios = CorreiosSpider()
    #
    #     result_tables = ["single_element"]
    #     expected_result = "single_element"
    #
    #     actual = correios.get_table_content(result_tables)
    #     self.assertEqual(expected_result, actual)
    #
    # def test_get_table_content_should_throw_index_error(self):
    #     correios = CorreiosSpider()
    #
    #     result_tables = []
    #     with self.assertRaises(IndexError):
    #         correios.get_table_content(result_tables)
    #
    # def test_is_uf_table_should_return_false(self):
    #     correios = CorreiosSpider()
    #
    #     uf_selected = 'I am the uf table'
    #
    #     actual = correios.is_uf_table(uf_selected)
    #     self.assertFalse(actual)
    #
    # def test_is_uf_table_should_return_false(self):
    #     correios = CorreiosSpider()
    #
    #     uf_selected = None
    #
    #     actual = correios.is_uf_table(uf_selected)
    #     self.assertFalse(actual)
    #
    # def test_is_uf_table_should_return_true(self):
    #     correios = CorreiosSpider()
    #
    #     uf_selected = ''
    #
    #     actual = correios.is_uf_table(uf_selected)
    #     self.assertTrue(actual)
    #
    # def test_set_record_loader_should_have_a_location(self):
    #     correios = CorreiosSpider()
    #     filename = '../tests/resources/table_with_two_rows_and_four_columns.html'
    #     file = open(filename, "r")
    #
    #     selector = Selector(text=file.read())
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #     td_index = 0
    #     correios.set_record_loader(record_loader, selector, td_index)
    #
    #     self.assertIn('First column', record_loader.load_item()['location'][0])
    #     self.assertEqual(len(record_loader.load_item()), 1)
    #
    # def test_set_record_loader_should_have_a_zip(self):
    #     correios = CorreiosSpider()
    #     filename = '../tests/resources/table_with_two_rows_and_four_columns.html'
    #     file = open(filename, "r")
    #
    #     selector = Selector(text=file.read())
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #     td_index = 1
    #     correios.set_record_loader(record_loader, selector, td_index)
    #
    #     self.assertIn('Second column', record_loader.load_item()['zip'][0])
    #     self.assertEqual(len(record_loader.load_item()), 1)
    #
    # def test_set_record_loader_should_have_no_data(self):
    #     correios = CorreiosSpider()
    #     filename = '../tests/resources/table_with_two_rows_and_four_columns.html'
    #     file = open(filename, "r")
    #
    #     selector = Selector(text=file.read())
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #     td_index = 2
    #     correios.set_record_loader(record_loader, selector, td_index)
    #
    #     self.assertEqual(len(record_loader.load_item()), 0)
    #
    #     td_index = 3
    #     correios.set_record_loader(record_loader, selector, td_index)
    #
    #     self.assertEqual(len(record_loader.load_item()), 0)
    #
    # def test_set_record_loader_should_throw_index_error(self):
    #     correios = CorreiosSpider()
    #     filename = '../tests/resources/empty.html'
    #     file = open(filename, "r")
    #
    #     selector = Selector(text=file.read())
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #     td_index = 1
    #
    #     with self.assertRaises(IndexError):
    #         correios.set_record_loader(record_loader, selector, td_index)
    #
    # def test_set_record_item_should_have_record(self):
    #     correios = CorreiosSpider()
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #
    #     ufloader = UfItemLoader(selector=Selector(text=''))
    #     uf = 'uf'
    #     ufloader.add_value(uf, 'Uf value')
    #
    #     correios.created_ufs[uf] = ufloader
    #
    #     record_loader.add_value('location', 'Location Address')
    #     record_loader.add_value('zip', 'Zip Code')
    #
    #     correios.set_record_item(record_loader, uf_selected=uf)
    #
    #     self.assertIsNotNone(ufloader.load_item()['record'])
    #
    # def test_set_record_item_should_have_record_with_new_location_and_zip_code(self):
    #     correios = CorreiosSpider()
    #
    #     ufloader = UfItemLoader(selector=Selector(text=''))
    #     uf = 'uf'
    #     ufloader.add_value(uf, 'Uf value')
    #
    #     record_loader = RecordItemLoader(selector=Selector(text=''))
    #     record_loader.add_value('location', 'Location Address')
    #     record_loader.add_value('zip', 'Zip Code')
    #
    #     ufloader.add_value('record', record_loader.load_item())
    #
    #     correios.created_ufs[uf] = ufloader
    #
    #     new_record_loader = RecordItemLoader(selector=Selector(text=''))
    #     new_record_loader.add_value('location', 'New Location Address')
    #     new_record_loader.add_value('zip', 'New Zip Code')
    #
    #     correios.set_record_item(new_record_loader, uf_selected=uf)
    #
    #     self.assertEqual(len(ufloader.load_item()['record']['location']), 2)
    #     self.assertEqual(len(ufloader.load_item()['record']['zip']), 2)
    #     self.assertIn('New Location Address', ufloader.load_item()['record']['location'])
    #     self.assertIn('New Zip Code', ufloader.load_item()['record']['zip'])

    def test_set_ufitemloader_should_contain_an_uf(self):
        correios = CorreiosSpider()

        uf = 'uf'
        correios.set_ufitemloader(Response(), uf_selected=uf)

        self.assertEqual(len(correios.created_ufs), 1)

    def test_set_ufitemloader_should_not_add_same_uf(self):
        correios = CorreiosSpider()

        uf = 'uf'
        correios.created_ufs[uf] = 'I am already created'

        correios.set_ufitemloader(Response(), uf_selected=uf)

        self.assertEqual(len(correios.created_ufs), 1)

    def test_a(self):
        correios = CorreiosSpider()

        ufloader = UfItemLoader(selector=Selector(text=''))
        uf = 'uf'
        ufloader.add_value(uf, 'Uf value')

        record_loader = RecordItemLoader(selector=Selector(text=''))
        record_loader.add_value('location', 'Location Address')
        record_loader.add_value('zip', 'Zip Code')

        ufloader.add_value('record', record_loader.load_item())

        correios.created_ufs[uf] = ufloader
        for e in correios.yield_result(None, Selector(text=''), 'uf'):
            print(e)

if __name__ == '__main__':
    unittest.main()