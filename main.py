# LIST METHODS


# list.append(x)
cars = ["Citroen","Alfa Romeo"]
cars.append("Mazda")
print(cars) # ['Citroen', 'Alfa Romeo', 'Mazda']
cars[len(cars):] = ["Fiat"]
print(cars) # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']


# list.extend(x), extend the list with an iterable
cars.extend(["Honda","Peugeot"])
print(cars)
# ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat', 'Honda', 'Peugeot']
cars.extend("BMW")
print(cars) 
# ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat', 'Honda', 'Peugeot', 'B', 'M', 'W']
cars[len(cars):] = "Audi"
print(cars)
# ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat', 'Honda', 'Peugeot', 'B', 'M', 'W', 'A', 'u', 'd', 'i']


# list.insert(i,x)
# insert the item x at the index i
letters = ["a","b","d","e","f"]
letters.insert(2,"c")
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f']
letters.insert(len(letters),"g")
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] --- similar to append


# list.remove(x) --- remove the first found x
# if not found raises ValueError
cars.remove("Fiat")
print(cars)
# ['Citroen', 'Alfa Romeo', 'Mazda', 'Honda', 'Peugeot', 'B', 'M', 'W', 'A', 'u', 'd', 'i']


# list.pop([i]) --- i is optional
# remove the element at the index i (and return it)
# if i not given remove and return the last element
saved_before_pop = letters.pop()
print(saved_before_pop) # g
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f']


# list.clear() --- remove all elements
cars.clear()
print(cars) #[]


# list.index(x[, start[, end]])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'c','h', 'i', 'j', 'k', 'c', 'd', 'e', 'l', 'm']
print(letters.index("c")) # 2
print(letters.index("c",5)) # 7 ---> search for the argument beginning at index 5
print(letters.index("c",5,11)) # 7 ---> search for the argument beginning at index 5 and ending at index 11 


# list.count(x) 
print(letters.count("c")) # 3


# list.sort() --- sorts in place
letters.sort()
print(letters)
# ['a', 'b', 'c', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


# list.reverse() --- reverses in place
letters.reverse()
print(letters) 
# ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'e', 'd', 'd', 'c', 'c', 'c', 'b', 'a']


# list.copy() --- return a shallow copy ---> equivalent to [:]
cars = ["Mazda","Fiat"]
cars_copy= cars.copy()
print(cars) # ['Mazda', 'Fiat']
print(cars_copy) # ['Mazda', 'Fiat']