'''
Created on 2018/11/26

@author: tom_uda
'''
dict = {
    "udagawa":
        {
        "kenichi":53,
        "yuko":53,
        "tomohiro":27,
        "akihiro":24,
        "kerry":16

        }
}

family_list = list(dict.keys())#リスト化
family_len = len(family_list)
print(family_len)

def search_dict(dic,key):
    value_keys = dic.get(key)
    value_keys_list =list(dic.keys())
    value_keys_len = len(value_keys_list)
    for i in range(value_keys_len):
        print("-----" + value_keys_list[i])

for i in range(family_len):
#for i in dict:
    search_name = family_list[i]
    print(family_list[i])
    #print(family_list[i].keys())
    breed = dict.get(search_name)
    search_dict(breed,search_name)
    # print(i)



