# i = 0 
# while i < 3:
#     print("meow")
#     i += 1

# list = range(5)
# for _ in list:
#     print("woof")

# print("meow\n" * 4, end="")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

animal = {"felix": "cat"}
print(animal["felix"])