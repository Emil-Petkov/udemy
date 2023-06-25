def band_name(city: str, pet_name):
    return f"Your band name could be: {city} {pet_name}"


print("Welcome to the band name generator.")
city = input("Which city did you grow up it?\n")
pet_name = input("What is the name of a pet?\n")

print(band_name(city, pet_name))

# print("Welcome to the band name generator.")
# city = input("Which city did you grow up it?")
# pet= input("What is the name of a pet?")

# print("Your band name could be " + city + " " + pet)
