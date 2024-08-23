class Instructor:
    def __init__(self,name="??",address="??"):
        print("constructor called")
        self.name = name
        self.address = address

ins_1 = Instructor("12","a12b")
ins_1.name = "abc"
ins_1.address = "ABC"

print(ins_1.name)
print(ins_1.address)


ins_2 = Instructor("12","a12b")

print(ins_2.name)
print(ins_2.address)


ins_3 = Instructor()

print(ins_3.name)
print(ins_3.address)