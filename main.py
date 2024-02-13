# WHEN REMOVING AN ITEM FROM A SET
# two methods can be used;
# remove() method causes error if the item to be removed not found in the set
# however discard() method does not raise an error in such a case

set_ = {"Citroen","Alfa Romeo","Mazda","Fiat"}
set_.discard("BMW") # no output at all

# set_.remove("BMW") # KeyError: 'BMW'