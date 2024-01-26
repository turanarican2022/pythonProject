# TUPLES

tuple = 1,2,3,4
print(tuple) # (1, 2, 3, 4)
print(tuple[2])

tuple_2 = tuple, 5,6,7
print(tuple_2) # ((1, 2, 3, 4), 5, 6, 7)


# sequence unpacking
tuple_3 = ("citroen",("alfa romeo","mazda","fiat"),)
was_brand_new, was_used = tuple_3
print(was_brand_new,was_used) # citroen ('alfa romeo', 'mazda', 'fiat')