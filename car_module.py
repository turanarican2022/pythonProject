def return_car():
    return "return_car() function called"

def main():
    print("once I had a Mazda")
    
if __name__ == "__main__":
    main() # once I had a Mazda
    
# above print_car() function is run if this file
# is executed standalone instead of importing it
# to some other file as a module

# this is a common use case for __name__ and __main__