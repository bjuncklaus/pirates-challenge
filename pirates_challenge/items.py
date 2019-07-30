from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.utils.markup import remove_tags
from scrapy.loader.processors import TakeFirst, MapCompose, Compose


class RecordItem(Item):
    location = Field(input_processor=MapCompose(remove_tags))
    zip = Field(input_processor=MapCompose(remove_tags, lambda string: string.strip()))


class UfItem(Item):
    uf = Field()
    record = Field(serializer=RecordItem)


class UfItemLoader(ItemLoader):
    default_item_class = UfItem
    default_output_processor = TakeFirst()


class RecordItemLoader(ItemLoader):
    default_item_class = RecordItem
    default_output_processor = Compose()