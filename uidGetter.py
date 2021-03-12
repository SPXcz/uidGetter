import json
import requests

query = "http://solr.dk-back.infra.mzk.cz/solr/kramerius/select?q=details%3A%2F.*TitlePage.*%2F%20AND%20collection%3A%22vc%3Ab1adb6f0-01db-45fd-bc4a-d36fa3eab050%22&wt=json"
response = requests.get(query)
noRows = response.json()['response']['numFound']

query = "http://solr.dk-back.infra.mzk.cz/solr/kramerius/select?q=details%3A%2F.*TitlePage.*%2F%20AND%20collection%3A%22vc%3Ab1adb6f0-01db-45fd-bc4a-d36fa3eab050%22&rows={}&wt=json".format(noRows)
response = requests.get(query)



with open('files/uids.txt', 'w+') as f:
    for resp in response.json()['response']['docs']:
        f.write(resp['root_pid']+"\n")
print("Done! UIDs are in your file")