# global variables
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# user input
color1 = input("Enter the first color (red, blue, yellow): ")
color2 = input("Enter the second color (red, blue, yellow): ")

# valid inouts
if color1 != RED and color1 != BLUE and color1 != YELLOW:
    print("Error: Invalid Color1")
elif color2 != RED and color2 != BLUE and color2 != YELLOW:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are the same")

    # mix colors and show second color
if color1 == RED:
    if color2 == BLUE:
        print("purple")
    else:
        print("orange")

elif color1 == BLUE:
    if color2 == RED:
        print("purple")
    else:
        print("green")
else:  # color1 == YELLOW
        if color2 == RED:
            print("orange")
        else:
            print("green")
