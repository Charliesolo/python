food = input("What food is it? " )

match food:
    case "Apple"| "Banana" | "Plum":
        print("fruit")
    case "Carrot" | "Spinach" | "Potato":
        print("vegetable")
    case "Tomato":
        print("It depends")
    case _:
        print("Who knows?")