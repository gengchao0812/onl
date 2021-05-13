import cx_Oracle
import yaml
# conn = cx_Oracle.connect('ops_uat', 'ops_uat', '22.188.46.141:1521/APSONL')
# cursor = conn.cursor()
# result = cursor.execute('select * from apply_main_appi mc where mc.appi_mc_id_number="110101197305084276"')
# print(result)


with open('../Data/PcNew.yaml', encoding='utf-8') as f:
    abc = yaml.safe_load(f)
print (abc.values())

# if __name__ == '__main__':
#     b = ClassA()
#     c = b.a()
#     print(type(c))
#     print(c)
#     print(v[0])
# # print(abc)
# for key in abc:
#      print(key)
# print(abc('firstname1'))
# print(abc['firstname1'])
# for k,v in abc.items():
#     print(v)
# with open('../Data/PcNew.yaml', encoding='utf-8') as f:
#     abc = yaml.safe_load(f)
# return (abc['new'])
# print(abc['new']['firstname1'])
# for k, v in abc.items():
#     for key,value in abc[k].items():
#         print(abc[k][key])
# def val():
#     with open('../Data/PcNew.yaml', encoding='utf-8') as f:
#         abc = yaml.safe_load(f)
#     for k, v in abc.items():
#         for key, value in abc[k].items():
#             yield (abc[k])
#
# if __name__ == '__main__':
#     a=val()
#     print(next(a))
#     print(next(a))
# ccc = abc['new']
# print(type(ccc))
#
# print('**********')
# print(ccc)
#
# print('**********')
# # for key in ccc:
# #     print(ccc[key])
# for k,v in ccc.items():
#     print(v)