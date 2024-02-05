#############################
# INHERITANCE               #
#############################

class Electronics:
    def __init__(self, type, make, model):
        self.type = type
        self.make = make
        self.model = model
    
    def made_in(self,country):
        return f"made in {country}"
    
class Phone(Electronics):
    def __init__(self, type, make, model, sub_model, year, price):
        super().__init__(type, make, model)
        self.sub_model=sub_model
        self.year=year
        self.price=price
    
    def built_in(self):
        return f"built in {self.year}"
    
huawei_laptop = Electronics("laptop","huawei","d15")
print(huawei_laptop.made_in("china")) # made in china

huawei_phone = Phone("phone","huawei","nova9","se",2022,8000)
print(huawei_phone.made_in("china")) # made in china
print(huawei_phone.built_in()) # built in 2022