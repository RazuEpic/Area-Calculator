import math

#2D shape surface area

def SQU_AREA():
    length = int(input("Enter the length of the square: "))
    width = int(input("Enter the width of the square: "))
    def calc_SQ(length, width):
        return length * width
    print("The area of the square is: ", calc_SQ(length, width), "units")
    input("\nPress enter to close the program...\n")

def TRI_AREA():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    def calc_TRI(base, height):
        return math.ceil((base * height) / 2)
    print("The area of the triangle is: ", int(calc_TRI(base, height)), "units")
    input("\nPress enter to close the program...\n")

def CIRC_AREA():
    radius = int(input("Enter the radius of the circle: "))
    def calc_CIRC(radius):
        return math.ceil(math.pi*radius) ** 2
    print("The area of the circle is: ", int(calc_CIRC(radius)), "units")
    input("\nPress enter to close the program...\n")

def TRAP_AREA():
    base_One = int(input("Enter base one of the trapazoid: "))
    base_Two = int(input("Enter base two of the trapazoid: "))
    height = int(input("Enter the height of the trapazoid: "))
    def calc_TRAP(base_One, base_Two, height):
        return math.ceil((((base_One + base_Two) / 2) * height))
    print("The area of the trapazoid is: ", int(calc_TRAP(base_One, base_Two, height)), "units")
    input("\nPress enter to close the program...\n")

#3D shape surface area

def CUBE_AREA():
    side = int(input("Enter the sides of the cube: "))
    def calc_CUBE(side):
        return 6 * side ** 2
    print("The surface area of the cube is: ", calc_CUBE(side), "units")
    input("\nPress enter to close the program...\n")

def CONE_AREA():
    radius = int(input("Enter the radius of the cone: "))
    height = int(input("Enter the height of the cone: "))
    def calc_CONE(radius, height):
        return math.ceil((math.pi * radius * (radius + math.sqrt((height ** 2) + (radius ** 2)))) )
    print("The surface area of the cone is: ", calc_CONE(radius, height), "units")
    input("\nPress enter to close the program...\n")

def TORUS_AREA():
    major_radius = int(input("Enter the major radius of the torus: "))
    minor_radius = int(input("Enter the minor radius of the torus: "))
    def calc_TORUS(major_radius, minor_radius):
        return math.ceil((2 * math.pi * major_radius) * (2 * math.pi * minor_radius))
    print("The surface area of the torus is: ", calc_TORUS(major_radius, minor_radius), "units")
    input("\nPress enter to close the program...\n")

while True:
    choices = {
        "1": SQU_AREA,
        "2": TRI_AREA,
        "3": CIRC_AREA,
        "4": TRAP_AREA,
        "5": CUBE_AREA,
        "6": CONE_AREA,
        "7": TORUS_AREA,
    }
    choice = input("""
    What would you like to calculate?
    1) Area of a square?
    2) Area of a triangle?
    3) Area of a circle?
    4) Area of a trapazoid?
    --------------------------------------
    5) Surface area of a cube?
    6) Surface area of a cone?
    7) Surface area of a torus (doughnut)?
    >>""")
    if choice in choices:
        choices[choice]()
        break
    else:
        print("Invalid choice")
