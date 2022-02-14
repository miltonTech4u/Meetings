# this is a comment
name = 'billy' # you can also do "billy"
age = 25

print(f"{name} is {age} years old!") #prints out "billy is 25 years old!"
print(type(name)) # will indicate type as str
print(type(age)) # will indicate type as int

age = str(age) #casts age variable to a str val
print(type(age)) # will now indicate age as a string
print(len(age)) #since age is a string now, we can use the len() method to see how long "25" is and the result gives us 2.