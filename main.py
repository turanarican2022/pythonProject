####################################################
# safely accessing dictionary elements with .get() #
######################################## to Ethan...

a_dict = {"key1":"value1", "key3":"value3"}

# print(a_dict["key2"]) # KeyError: 'key2'

print(a_dict.get("key1")) # value1
print(a_dict.get("key2")) # None




