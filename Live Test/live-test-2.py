"""
You're helping a friend plan a small birthday party and keep track of the snacks and budget.

a) Write a function add_snack(snack_list, item) that adds item to snack_list and returns the updated list.

b) Create a dictionary called party with three keys: "host", "snacks" (a list), and "budget" (starts at 500).

c) Write a function add_cost(budget, amount=50) that adds amount to budget and returns the new total. Call it once without passing amount, and once passing amount=100.


"""

def add_snack(snack_list, item):
    snack_list.append(item)
    return snack_list

party = {
    "host": "",
    "snacks": [],
    "budget": 500
    
}

def add_cost(budget, amount=50):
    budget = budget + amount
    return budget

print(add_snack(party["snacks"], "chanachur")) # just to check if the function is working or no


print(add_cost(party["budget"])) # as we seeing it printed the budget after we added the default amount= 50 and printed 550


print(add_cost(party["budget"], amount=100)) # and here we are seeing the budget after we added=100