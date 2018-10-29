class Food:
    def __init__(self, image, xpos, ypos, width, heigth):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos
        self.rectPoint = image.get_rect().move(xpos, ypos)
        self.width = width
        self.height = heigth

    def move(self, xposSpeed, yposSpeed):
        self.rectPoint = self.rectPoint.move(xposSpeed, yposSpeed)
       # print(self.rectPoint.left)