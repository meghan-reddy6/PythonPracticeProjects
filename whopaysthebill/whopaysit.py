import random


def collect_names():
    names = []

    print("\n" + "-" * 40)
    print(" Enter names (type 'exit' to finish)")
    print("-" * 40)

    while True:
        name = input("➜ ").strip()

        if name.lower() == "exit":
            break

        if name:
            names.append(name)

    return names


def choose_who_pays(names):
    print("\n" + "=" * 40)

    if not names:
        print(" ⚠️  No names were entered.")
        print("=" * 40)
        return

    chosen = random.choice(names)
    print(f" 🍽️  {chosen} is buying the meal today!")
    print("=" * 40)


def main():
    while True:
        print("\n" + "#" * 40)
        print("   WHO PAYS THE BILL 🎉")
        print("#" * 40)

        names = collect_names()
        choose_who_pays(names)

        again = input("\n Choose again? (yes/no): ").lower()
        if again != "yes":
            print("\n 👋 Thanks for using the app!")
            break


if __name__ == "__main__":
    main()
