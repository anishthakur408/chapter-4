# Check that a tuple type cannot be changed in python. 

a = (5,53,"anish",45)

print(a)

print(type(a)) # we can not change a touple lets try

a[1] = 5


print(a) # TypeError: 'tuple' object does not support item assignment