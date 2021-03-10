import json
import requests

query = "http://solr.dk-back.infra.mzk.cz/solr/kramerius/select?q=collection%3A%22vc%3Ab1adb6f0-01db-45fd-bc4a-d36fa3eab050%22&rows=50&wt=json"
response = requests.get(query)

print(response.json())