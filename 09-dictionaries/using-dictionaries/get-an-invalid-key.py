# Run the code. It should throw a KeyError! "energy" does not exist as one of the elements.

# Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Did this resolve the KeyError?


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], 'energy':'Not a Zodiac element'}

print(zodiac_elements["energy"])
