# You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.

# Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks iterator and turns each tuple pair into a key:value item.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(list(zipped_drinks))

drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)