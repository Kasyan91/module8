import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats=[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
print(type(cats))

def convert_list(cats):
    cats_list=list()
    for i in cats:
        if isinstance(i,dict):
            cats_list.append(Cat(i["nickname"],i["age"],i["owner"]))
        else:
            cats_dict={}
            cats_dict["nickname"]=i.nickname
            cats_dict["age"]=i.age
            cats_dict["owner"]=i.owner
            cats_list.append(cats_dict)
    return cats_list

print(convert_list(cats))
