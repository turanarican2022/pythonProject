####################################################
# reading from and writing to files                #
####################################### to Joshua...

# write to a file: (the second "w" parameter should be used)
with open("file.md", "w") as file:
    file.write("This line is written by Python script")

# read from a file: (the second argument is by default "r", it can be omitted)
with open("file.md") as file:
    print(file.read())
    # This line is written by Python script
    
# read from a multiline file:

with open("multiline_file.md") as multiline_file:
    for line in multiline_file:
        print(line)

# title



# this is a multiline .md file



# what else?



