# String Format 

"""
a = "Good Morning, Rei"

user_input = input("What is your name?")

print(user_input)
print(a)

"""

"""
user_input = input("What is your name?")
a = "Good Morning, {}. How are you? {}".format(user_input, "Hello!")
print(user_input)
print(a)
"""

"""
age = 24
f_name = "Rei"
l_name = "San"


txt = "I am {f_name} {l_name}. I am {age} years old.".format(l_name=l_name, f_name=f_name, age=age)
print(txt)
"""

age = 25
f_name = "Rei"
l_name = "San"

txt = f"I am {f_name} {l_name}. I'm {age} years old"
print(txt)