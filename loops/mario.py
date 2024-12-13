def main():
    print_col(3)
    print_square(5)

def print_col(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("#" * width)

def print_square(size):
    for i in range(size):
        print_row(size)


main()