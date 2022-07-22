import requests

REMOVE_CHARS = ['N/A', '-', '']

def clean_nodes(data_json):
    for key in list(data_json):
        if type(data_json[key]) == dict:
            data_json[key] = clean_nodes(data_json[key])
        if type(data_json[key]) == list:
            _rtn_list = data_json[key]
            for item in data_json[key]:
                if item in REMOVE_CHARS:
                    _rtn_list.remove(item)
                data_json[key] = _rtn_list
        if data_json[key] in REMOVE_CHARS:
            del data_json[key]
    return data_json

def clean_data():
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
    return clean_nodes(r.json())

print(clean_data())
