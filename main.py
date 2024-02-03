divide = lambda x,y:x//y
print(divide(15,3)) # 5

write = lambda car,year: print(f"{car} was made in {year}")
write("Citroen",2012) # Citroen was made in 2012

write = lambda name="Halit Turan",surname="ARICAN": f"my name is {name} {surname}"
print(write()) # my name is Halit Turan ARICAN
print(write(name="Halide",surname="Tuğba")) # my name is Halide Tuğba

def op(num_1,num_2,operand):
    print(operand(num_1,num_2))
    
op(20,2,lambda x,y:x//y) # 10