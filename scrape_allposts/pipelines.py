import json
from operator import itemgetter

from scrape_allposts.config.firestore_config import FirestoreConfig


class ScrapeAllpostsPipeline:
    fire_config = None

    def __init__(self):
        self.fire_config = FirestoreConfig()

    def process_item(self, item, spider):
        elements, site_name = itemgetter('elements', 'site_name')(item)
        element_map_to_save = {}

        print(site_name)
        for i, element in enumerate(elements):
            element_map_to_save[f'{site_name}_{i}'] = element

        try:
            site_ref = self.fire_config.firebase_db.reference(site_name)
            site_ref.set(element_map_to_save)
        except:
            self.fire_config.firebase_ref.push(site_name, element_map_to_save)

        return item
