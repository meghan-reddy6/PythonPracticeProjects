import random

def main():
    print("\n" + "=" * 40)
    print("   HEADS OR TAILS GAME 🎲")
    print("=" * 40)

    while True:
        value = random.randint(0,1)
        if value == 0:
            print("\nIt's Heads! 🪙")
        else:
            print("\nIt's Tails! 🪙")
        again = input("\nDo you want to flip again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()