'''
You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. This will require a few steps:

1. Define the function to accept a list of strings as a single parameter called names
2. Create a new list of strings
3. Loop through each name in names
4. Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
5. Afterwards, return the new list of strings
'''

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))