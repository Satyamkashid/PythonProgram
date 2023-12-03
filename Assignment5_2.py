class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the radius :")
        self.Radius = int(input())

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius**2)

    def CalculateCurcumferece(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print("Radius of the circle is :",self.Radius)
        print("Area of the circle is :",self.Area)
        print("Circumference of the circle is :",self.Circumference)

        
def main():
    print("Enter How Many Circle")
    circle=int(input())
    for i in range(circle):
        circle = Circle()

        circle.Accept()

        circle.CalculateArea()
        circle.CalculateCurcumferece()

        circle.display()

if __name__ == "__main__":
    main()
    
        