print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepporoni = input("Do ou want pepperoni on your pizza? Y or N:").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

# Calculate base price based on size

match size:
    case 's':
        bill += 15
    case 'm':
        bill += 20
    case 'l':
        bill += 25

if pepporoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f'Your final bill is: ${bill}.')