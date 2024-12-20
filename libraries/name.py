import sys

# if len(sys.argv) < 2:
#     sys.exit
# elif len(sys.argv) > 2:
#     sys.exit
# else:
#     print("hello my name is", sys.argv[1] )

for arg in sys.argv[1:]:
    print( "hello my name is ", arg)