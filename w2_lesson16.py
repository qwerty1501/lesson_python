# import json
# from pprint import pprint as pp
#
# dict_1 = {'login': ''}
# dict_2 = {'email': ''}
# dict_3 = {'age': 1}
# list_new = [dict_1, dict_2, dict_3]
# with open('das.json', 'w') as f:
#     json.dump(list_new, f)
#
# with open('das.json', 'r') as f:
#     data = json.load(f)
#
# for i in range(3):
#     data[i]['language'] = 'ru'
#
# pp(data)
# with open('das.json', 'w') as f:
#     json.dump(data, f)
#
#
# import requests
# import json
# from pprint import pprint as pp
#
# data = requests.get('https://api.github.com/events')
# data = data.json()
# for i in range(len(data)):
#     data[i]['actor'] = 'Kairat Sexy'
#
# with open('kairat_sexy.json', 'w') as f:
#     json.dump(data, f)
#
#
# import requests
# from pprint import pprint as pp
# data = requests.get('https://api.github.com/emojis')
# data = data.json()
# pp(data) # emodzi
#
# import requests
#
# data = requests.post('https://httpbin.org/post', json = {"name": "dastan", "model": "mac"})
# print(data)