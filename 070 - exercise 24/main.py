data = [
    {
        "name": "jit",
        "age":21
    },
    {
        "name": "amit",
        "age":22
    }
]

print(data)

def add( data,name,age):
    data.append({
        "name": name,
        "age": age
    })
    print(data)

add(data,"abcdef",123)

# data.append({
#     "name": "abc",
#     "age":23
# })

# print(data)