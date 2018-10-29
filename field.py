class Field:
    field = []
    def __init__(self, xRange, yRange):
        for x in range(0, xRange):
            temp = {}
            for y in range(0, yRange):
                print(x, "x  ", y, "y")
                temp = {}
            self.field.append()

    def main(self):
        print(self.field)

field = Field(10,10)
field.main()