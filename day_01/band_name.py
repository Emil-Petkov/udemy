def band_name(city: str, pet_name: str):
    return f'Your band name could be {city} {pet_name}'


city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

print(band_name(city, pet_name))
