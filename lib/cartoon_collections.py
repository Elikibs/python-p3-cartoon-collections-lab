def roll_call_dwarves(names):
    for i, name in enumerate (names, start=1):
        print(f"{i}. {name}")

roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy", "Ken"])

# Assignment 2
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
def summon_captain_planet(list):
    return [f"{item.capitalize()}!" for item in list]
        
print(summon_captain_planet(planeteer_calls))

# Assignment 3
short_words = ["puff", "go", "two", "primitive"]
def long_planeteer_calls(list):
    return any(len(item) > 4 for item in list)

print(long_planeteer_calls(short_words))

# Assignment 4
snacks = ["cheddar", "gouda", "thyme"]
def find_the_cheese(snacks_list):
    types_of_cheese = ["cheddar", "gouda", "camembert"]

    for snack in snacks_list:
        if snack in types_of_cheese:
            return snack
        
    return None

print(find_the_cheese(snacks))