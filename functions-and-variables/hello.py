def hello(to="Bob"):
    to = to.strip().title()
    print("hello,", to)

name = input("What's your name? ")
hello(name)
hello()

