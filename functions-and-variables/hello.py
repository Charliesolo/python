def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="Bob"):
    to = to.strip().title()
    print("hello,", to)

main()