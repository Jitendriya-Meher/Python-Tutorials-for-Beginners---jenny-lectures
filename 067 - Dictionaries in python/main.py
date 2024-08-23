phone_no = {
    "Ram":1234,
    "amit":5678,
    'jit':1357
}

# phone_no = dict({
#     "Ram":1234,
#     "amit":5678,
#     'jit':1357,
#     "jitendriya":2468
# })

# phone_no = dict([
#     ("amit",12),
#     ("jit",20)
# ])

print(phone_no)
print(phone_no["amit"]) 

# dictionary are mutable
phone_no["amit"] = 1234567890
phone_no["amit"] = {
    1234567890,
    123
}
print(phone_no)

print("amit",phone_no.get("amit"))

print(phone_no.get("abc"))

data = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f"
}

print(data[1])

# delete the key
del data[1]
print(data)

print(data.pop(2))
print(data)

# delete the last element
print(data.popitem())
print(data)

# delete all elements
# data.clear()
# print(data)

print(data.keys())

print(data.values())

print(data.items())

for i in data:
    print(i,data[i])

for i in data.items():
    print(i)

datas = data.copy()
print(datas)

print(len(datas))