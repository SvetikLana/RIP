from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square



def main():

    print("\nБулыгина Светлана ИУ5Ц-71Б\n")

    rectangle = Rectangle("синего", 1, 1)
    circle = Circle("зеленого", 1)
    square = Square("красного", 1)

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
