# Create a variable called total_exercises and set it equal to 0.

# Iterate through the values in the num_exercises list and add each value to the total_exercises variable.

# Print the total_exercises variable to the console.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for i in num_exercises.values():
  total_exercises += i
print(total_exercises)