import json
import csv

with open('tw.json', 'r') as f:
    tw_codes = json.load(f)

with open('species_joined.json', 'r') as f:
    species_data = json.load(f)

filtered_data = [species for species in species_data if species['speciesCode'] in tw_codes]

headers = ['中文俗名', '學名', '英文俗名', 'comNameCodes', 'sciNameCodes', 'bandingCodes', 'familySciName']
json_keys = ['comNameZh', 'sciName', 'comName', 'comNameCodes', 'sciNameCodes', 'bandingCodes', 'familySciName']

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in filtered_data:
        row = [str(item[key]) if isinstance(item[key], (str, int, float)) else ','.join(item[key]) for key in json_keys]
        writer.writerow(row)