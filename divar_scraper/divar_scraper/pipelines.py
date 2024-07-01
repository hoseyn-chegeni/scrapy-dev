# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DivarScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip whitespace from all fields except 'description'
        for field_name in adapter.field_names():
            if field_name != 'description':
                value = adapter.get(field_name)
                if value and isinstance(value, str):
                    adapter[field_name] = value.strip()

        # Convert specific fields to lowercase
        lowercase_keys = ['category', 'product_type']
        for key in lowercase_keys:
            value = adapter.get(key)
            if value and isinstance(value, str):
                adapter[key] = value.lower()

        price_keys = ['price_excl_tax','price_incl_tax','tax']
        for i in price_keys:
            value = adapter.get(i)
            value = value.replace('£', '')
            adapter[i] = float(value)

        return item