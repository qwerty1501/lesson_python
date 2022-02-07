# class Laptop:
#
#     def __init__(self, name, cpu, ram, graph_card, hdd, screensize):
#         self.name = name
#         self.cpu = cpu
#         self.ram = ram
#         self.graph_card = graph_card
#         self.hdd = hdd
#         self.screensize = screensize
#
#     def get_dict(self):
#         dict1 = {
#             'Название ноутбука': self.name,
#             'Процессор': self.cpu,
#             'Оперативная память': f'{self.ram} гб',
#             'Видеокарта': self.graph_card,
#             'Размер диска': self.hdd,
#             'Диагональ экрана': self.screensize,
#         }
#         return dict1
#
#     def output(self):
#         some_dict = Laptop.get_dict(self).items()
#         for k, v in some_dict:
#             print(k, ':', v)
#
#
# aser = Laptop('Acer Aspire 7', 'Intel Core i7', 16, 'nvidia geforce gtx 1650', 512, 15.6)
# dell = Laptop('Dell Inspiron', 'i7 ', 32, '1660 Ti', 2000, 15.6)
# aser.output()
# dell.output()

##### Data #1:
# colors = {
# "black": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,255,1],
# "hex": "#000"
# }
# },
# "white": {
# "category": "value",
# "type": "primary",
# "code": {
# "rgba": [0,0,0,1],
# "hex": "#FFF"
# }
# },
# "red": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,0,0,1],
# "hex": "#FF0"
# }
# },
# "blue": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [0,0,255,1],
# "hex": "#00F"
# }
# },
# "yellow": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,0,1],
# "hex": "#FF0"
# }
# },
# "green": {
# "category": "hue",
# "type": "secondary",
# "code": {
# "rgba": [0,255,0,1],
# "hex": "#0F0"
# }
# }
# }
# class Dict1:
#
#     def keys_tuple(self):
#         a = []
#         a += colors.keys()
#         print(tuple(a))
#
#     def values_tuple(self):
#         a = []
#         a += colors.values()
#         print(tuple(a))
#
#     def keys_list(self):
#         a = []
#         a += colors.keys()
#         print(list(a))
#
#     def values_list(self):
#         a = []
#         a += colors.values()
#         print(list(a))
#
#     def keys_set(self):
#         a = []
#         a += colors.keys()
#         print(set(a))
#
#     def values_set(self):
#         a = []
#         a += colors.values()
#         print(set(a))
#
# a = Dict1()
# a.keys_tuple()
# a.values_tuple()
# a.keys_list()
# a.values_list()
# a.keys_set()
# a.values_set()



##### Data #2:
data = {
"markers": [
{
"name": "Rixos The Palm Dubai",
"position": [25.1212, 55.1535],
},
{
"name": "Shangri-La Hotel",
"location": [25.2084, 55.2719]
},
{
"name": "Grand Hyatt",
"location": [25.2285, 55.3273]
}
]
}
# class Data2:
#     def names(self):
#
print(data.get('name'))
print(data.keys())
print(data.values())