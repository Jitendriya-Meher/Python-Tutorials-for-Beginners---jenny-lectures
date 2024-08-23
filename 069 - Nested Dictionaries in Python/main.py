student_data = {
    "Ram":{
        "roll_no":1,
        "age":21,
        "course":"python"
    },
    "Amit":{
        "roll_no":2,
        "age":22,
        "course":"C++"
    }
}
print(student_data)

print(student_data["Amit"])
print(student_data["Amit"]["age"])

student_data["Amit"]["phone"] = 811
print(student_data)

student_data["Amit"].pop("phone")
print(student_data)


data = {
    "Gujrat":["a",'b','c'],
    "Mumbai":["d",'e','f']
}

print(data)
print(data["Mumbai"])

data2 = [
    {
        "name":"amit",
        "age":20
    },
    {
        "name":"jit",
        "age":22
    }
]

print(data2)
print(data2[0])