class Ins:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def info(self):
        print(f"name = {self.name}, address = {self.address}")

    def fullname(self,lname):
        return f"{self.name} {lname}"


i1 = Ins("amit","khariar")
i1.info()

i2 = Ins("amit meher","khariar,nuapada")
i2.info()

i3 = Ins("amit","khariar")
i3.info()
print(i3.fullname("Meher"))