from wikidata.client import Client
client = Client()

def get_parent_ids(child):
    return [parent['mainsnak']['datavalue']['value']['id'] for parent in child.attributes['claims']['P279'] if 'datavalue' in parent['mainsnak']]


country_class = client.get('Q6256')
entity_class = client.get('Q35120')
print(country_class)

parent_ids = get_parent_ids(country_class)
parents = [client.get(id) for id in parent_ids]
    
print(parent_ids)
