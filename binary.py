import sys, pygame
import Snake, Food, Cursor, DBConnect
from random import randint
from pygame.locals import *
pygame.init()
print("initPhase")
black = (0, 0, 0)
white = (255, 255, 255)
size = width, height = 400, 450
screen = pygame.display.set_mode(size)
block = (10, 10)
left = (-10, 0)
right = (10, 0)
up = (0, -10)
down = (0, 10)
clock = pygame.time.Clock()
speed = 15
score = 0

snakeImage = pygame.image.load('snake.png').convert()
foodImage = pygame.image.load('snake.png').convert()
cursorImage = pygame.image.load('cursor.png').convert()
seperatorImage = pygame.image.load('seperator.png').convert()


def main(speed, score):
    print("main")
    intro = True
    screen.fill(black)
    snake = Snake.Snake(snakeImage, 10, 10, 10, 10)
    seperator = Cursor.Cursor(seperatorImage, 0, 410, 450, 10)
    pygame.display.flip()
    direction = (10, 0)
    foodx = (randint(1, 20) - 1) * 10
    foody = (randint(1, 20) - 1) * 10
    food = Food.Food(foodImage, foodx, foody, 10, 10)
    snakeLength = 0
    snakeChain = []
    gameOver = False
    while 1:
        #normal game start
        screen.fill(black)
        if snake.rectPoint[0] == food.rectPoint[0] and snake.rectPoint[1] == food.rectPoint[1]:
            food = None
            snakeChainImage = pygame.image.load('snake.png').convert()
            snakeChain.append(Snake.Snake(snakeChainImage, snake.rectPoint[0], snake.rectPoint[1], 10, 10))
            snakeLength = snakeLength + 1
            score = score + 1
        if food is None:
            foodx = (randint(1, 20)-1)*10
            foody = (randint(1, 20)-1)*10
            food = Food.Food(foodImage, foodx, foody, 10, 10)
            food.move(foodx, foody)
            screen.blit(food.image, food.rectPoint)
        else:
            screen.blit(food.image, food.rectPoint)

        clock.tick(speed)
        temp = directionKey(direction)
        if temp is not None:
            direction = temp
        count = snakeLength
        while (count != 0):
            if count == 1:
                snakeChain[count - 1].setPos(snake.rectPoint[0], snake.rectPoint[1])
            else:
                snakeChain[count - 1].setPos(snakeChain[count - 2].rectPoint[0], snakeChain[count - 2].rectPoint[1])
            screen.blit(snakeChain[count - 1].image, snakeChain[count - 1].rectPoint)
            count = count - 1
        snake.move(direction[0], direction[1])
        if snake.rectPoint[0] < 0 or snake.rectPoint[0] > 400 or snake.rectPoint[1] < 0 or snake.rectPoint[1] > 400:
            gameOver = True
        if selfCollision(snake, snakeChain) == True:
            gameOver = True
        screen.blit(snake.image, snake.rectPoint)
        screen.blit(seperator.image, seperator.rectPoint)
        scoreUp(score)
        pygame.display.update()
        if gameOver == True:
            dbconnection = DBConnect.DBConnect("localhost", "schnake", "schnake", "schnake").connection
            dbcursor = dbconnection.cursor()
            query = ("SELECT count(*), min(score_value), score_name FROM scoreboard ORDER BY score_value DESC LIMIT 10")
            insert = ("INSERT INTO scoreboard(score_name, score_value) VALUES('REN', "+score+")")
            dbcursor.execute(query)
            for a in dbcursor:
                lowestScore = a[1]
                scoreCount = a[0]
            if score > lowestScore or scoreCount < 10:
                largeText = pygame.font.Font('freesansbold.ttf', 30)
                TextSurfHS, TextRectHS = text_objects("NEW HIGHSCORE", largeText)
                TextRectHS.centerx = ((width / 2))
                TextRectHS.centery = ((200))
                screen.blit(TextSurfHS, TextRectHS)

                pygame.display.update()

                dbconnection.close()
                dbcursor.close()
            else:
                largeText = pygame.font.Font('freesansbold.ttf', 30)
                TextSurfGO, TextRectGO = text_objects("Game Over", largeText)
                TextRectGO.centerx = ((width / 2))
                TextRectGO.centery = ((200))
                screen.blit(TextSurfGO, TextRectGO)
                pygame.display.update()
                enter = False
                while enter is not True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == KEYDOWN:
                            if event.key == 13:
                                enter = True
                break
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def gameIntro():
    selfIntro = True
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurfSchnake, TextRectSchnake = text_objects("Schnake", largeText)
    TextRectSchnake.left = ((width / 4))
    TextRectSchnake.centery = ((height / 4))
    TextSurfSchettings, TextRectSchettings = text_objects("Schettings", largeText)
    TextRectSchettings.left = ((width / 4))
    TextRectSchettings.centery = ((height / 2))
    TextSurfSchcoreboard, TextRectSchcoreboard = text_objects("Schcoreboard", largeText)
    TextRectSchcoreboard.left = ((width / 4))
    TextRectSchcoreboard.centery = ((height / 4 * 3))
    menuPoints = ((TextSurfSchnake, TextRectSchnake, "Schnake"), (TextSurfSchettings, TextRectSchettings, "Schettings"), (TextSurfSchcoreboard, TextRectSchcoreboard, "Schcoreboard"))
    cursor = Cursor.Cursor(cursorImage, 10, 10, 25, 25)
    currentCursor = 0
    returnValue = None
    while selfIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == 13:
                    selfIntro = False
                    returnValue = menuPoints[currentCursor][2]
                elif event.key == 27:
                    pygame.quit()
                    quit()
                elif event.key == 274:
                    if currentCursor < (len(menuPoints)-1):
                        currentCursor = currentCursor + 1
                elif event.key == 273:
                    if currentCursor > 0:
                        currentCursor = currentCursor -1
        screen.fill(black)
        count = 0
        while count < len(menuPoints):
            if currentCursor == count:
                cursor.setPos(menuPoints[count][1].left - 26, menuPoints[count][1].top + 2)
            count = count + 1
        screen.blit(cursor.image, cursor.rectPoint)
        screen.blit(TextSurfSchnake, TextRectSchnake)
        screen.blit(TextSurfSchettings, TextRectSchettings)
        screen.blit(TextSurfSchcoreboard, TextRectSchcoreboard)
        pygame.display.update()
        clock.tick(15)
        if returnValue is not None:
            return returnValue

def directionKey(direction):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            #print(event.key)
            if event.key == 276:
                if direction != right:
                    return left
            elif event.key == 275:
                if direction != left:
                    return right
            elif event.key == 274:
                if direction != up:
                    return down
            elif event.key == 273:
                if direction != down:
                    return up
            elif event.key == 27:
                pygame.quit()
                quit()
            else:
                return None

def schettings(oldSpeed):
    selfIntro = True
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurfSchpeed, TextRectSchpeed = text_objects("Schpeed", largeText)
    TextRectSchpeed.left = ((width / 4))
    TextRectSchpeed.centery = ((height / 4))
    TextSurfBonus, TextRectBonus = text_objects("Bonus", largeText)
    TextRectBonus.left = ((width / 4))
    TextRectBonus.centery = ((height / 2))
    menuPoints = ((TextSurfSchpeed, TextRectSchpeed, "Schpeed"),(TextSurfBonus, TextRectBonus, "Bonus"))
    cursor = Cursor.Cursor(cursorImage, 10, 10, 25, 25)
    currentCursor = 0
    returnValue = None
    while selfIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == 13:
                    selfIntro = False
                    returnValue = oldSpeed
                elif event.key == 27:
                    pygame.quit()
                    quit()
                elif event.key == 274:
                    if currentCursor < (len(menuPoints) - 1):
                        currentCursor = currentCursor + 1
                elif event.key == 273:
                    if currentCursor > 0:
                        currentCursor = currentCursor - 1
                elif event.key == 276:
                    oldSpeed = oldSpeed - 1
                elif event.key == 275:
                    oldSpeed = oldSpeed + 1
                elif event.key == 93:
                    oldSpeed = oldSpeed + 10
                elif event.key == 47:
                    oldSpeed = oldSpeed - 10
        screen.fill(black)
        TextSurfSchpeedValue, TextRectSchpeedValue = text_objects(str(oldSpeed), largeText)
        TextRectSchpeedValue.left = (width / 1.5)
        TextRectSchpeedValue.centery = (TextRectSchpeed.centery)
        count = 0
        while count < len(menuPoints):
            if currentCursor == count:
                cursor.setPos(menuPoints[count][1].left - 26, menuPoints[count][1].top + 2)
            count = count + 1
        screen.blit(cursor.image, cursor.rectPoint)
        screen.blit(TextSurfSchpeed, TextRectSchpeed)
        screen.blit(TextSurfSchpeedValue, TextRectSchpeedValue)
        screen.blit(TextSurfBonus, TextRectBonus)
        pygame.display.update()
        clock.tick(15)
        if returnValue is not None:
            return returnValue
def scoreUp(score):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurfSchcore, TextRectSchcore = text_objects("Schcore:", largeText)
    TextRectSchcore.centerx = ((width / 2) - 30)
    TextRectSchcore.centery = (435)
    TextSurfSchcoreValue, TextRectSchcoreValue = text_objects(str(score), largeText)
    TextRectSchcoreValue.centerx = (TextRectSchcore.right + 20)
    TextRectSchcoreValue.centery = (435)
    screen.blit(TextSurfSchcore, TextRectSchcore)
    screen.blit(TextSurfSchcoreValue, TextRectSchcoreValue)

def selfCollision(snake, snakeChain):
    for part in snakeChain:
        if snake.rectPoint[0] == part.rectPoint[0] and snake.rectPoint[1] == part.rectPoint[1]:
            return True

def schcoreboard():
    dbconnection = DBConnect.DBConnect("localhost", "schnake", "schnake", "schnake").connection
    dbcursor = dbconnection.cursor()

    query = ("SELECT * FROM scoreboard ORDER BY score_value DESC LIMIT 10")
    dbcursor.execute(query)
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    screen.fill(black)
    for index in enumerate(dbcursor):

        Surf, Rect = text_objects(str(index[1][1]), largeText)
        Rect.centerx = ((width / 2) - 110)
        Rect.centery = ((height/11)*(1+index[0]))
        screen.blit(Surf, Rect)
        Surf, Rect = text_objects("------", largeText)
        Rect.centerx = ((width / 2))
        Rect.centery = ((height / 11) * (1 + index[0]))
        screen.blit(Surf, Rect)
        Surf, Rect = text_objects(str(index[1][2]), largeText)
        Rect.centerx = ((width / 2) + 100)
        Rect.centery = ((height / 11) * (1 + index[0]))
        screen.blit(Surf, Rect)
        pygame.display.update()

    dbcursor.close()
    dbconnection.close()
    enter = False
    while enter is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == 13:
                    enter = True
    return None

while 1:
    mode = gameIntro()
    if mode is not None:
        if mode == "Schnake":
            main(speed, score)
        elif mode == "Schettings":
            newSpeed = schettings(speed)
            speed = newSpeed
        elif mode == "Schcoreboard":
            schcoreboard()
