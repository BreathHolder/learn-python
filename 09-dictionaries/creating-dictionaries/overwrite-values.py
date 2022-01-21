# Add the key "Supporting Actress" and set the value to "Viola Davis".

# Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best Picture" to "Moonlight".

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners.update({'Supporting Actress':'Viola Davis'})
oscar_winners.update({'Best Picture':'Moonlight'})
print(oscar_winners)