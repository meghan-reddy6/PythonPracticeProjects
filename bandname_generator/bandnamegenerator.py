while True:
    print("Welcome to the Band Name Generator!")
    city = input("Enter the name of the city you grew up in: ")
    pet = input("Enter the name of your first pet: ")
    band_name = f"{city} {pet}"
    print(f"Your band name could be: {band_name}")
    restart = input("Would you like to generate another band name? (yes/no): ")
    if restart.lower() != 'yes':
        print("Thank you for using the Band Name Generator. Goodbye!")
        break