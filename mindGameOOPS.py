import random, time, turtle
import colorPallette as cP
import tkinter as tk
class mindGameOOPS:
    def __init__(self) -> None:
        self.colors = ['red','orange','yellow','green','blue','indigo']
        self.score = 0
        self.levelNo = 1
        self.theFont = ('Arial',25,'bold')
        self.highSc = mindGameOOPS.readDatabase()#Initializing the Database
        self.screen = turtle.Screen()

    @staticmethod
    def readDatabase():
        try:
            handler = open('/Users/tarunprakash/Documents/Python Codes/Projects/Mind Game/highScoretracker.txt', 'r')
            highSc = int(handler.read())
            handler.close()
        except:
            handlew = open('/Users/tarunprakash/Documents/Python Codes/Projects/Mind Game/highScoretracker.txt', 'w')
            handlew.write(str(0))
            highSc = 0
            handlew.close()
        return highSc

    def createTurtles(self):
        self.timerTurtle = turtle.Turtle()
        self.timerTurtle.hideturtle()
        self.colorTurtle = turtle.Turtle()
        self.colorTurtle.hideturtle()
        self.endTurtle = turtle.Turtle()
        self.endTurtle.color('white')
        self.endTurtle.hideturtle()
        self.scoreTurtle = turtle.Turtle()
        self.scoreTurtle.hideturtle()
        self.highScoreTurtle = turtle.Turtle()
        self.highScoreTurtle.hideturtle()
        self.pen = turtle.Turtle()
        self.pen.hideturtle()

    def startUp(self):
        self.scoreTurtle.color('white')
        self.scoreTurtle.penup()
        self.scoreTurtle.goto(350,350)
        self.scoreTurtle.pendown()

        self.highScoreTurtle.color('white')
        self.highScoreTurtle.penup()
        self.highScoreTurtle.goto(350,300)
        self.highScoreTurtle.pendown()

        self.timerTurtle.color('white')
        self.pen.color('white')

        self.screen.setup(height=800,width=1200)
        self.screen.bgcolor('black')
        self.screen.title('Mind Game')

        self.pen.penup()
        self.pen.goto(0,300)
        self.pen.pendown()
        self.pen.write('Mind Games',font=('Arial',60,'bold'),align='center') 

    def timer(self,message,t):
        self.timerTurtle.penup()
        self.timerTurtle.goto(0,0)
        self.timerTurtle.pendown()

        for i in range(3,0,-1):
            self.timerTurtle.write(message + str(i),font=('Arial',30,'normal'),align='center')
            time.sleep(t)
            self.timerTurtle.clear()
        self.timerTurtle.write('Go!',font=('Arial',30,'normal'),align='center')
        time.sleep(t)
        self.timerTurtle.clear()

    def colorGen(self):
        self.colorAns = []
        for i in range(self.levelNo):
            self.col = random.choice(self.colors)
            self.screen.bgcolor(self.col)
            self.colorTurtle.write(self.col.capitalize(),font=('Arial',30,'normal'),align='center')
            time.sleep(1)
            self.colorTurtle.clear()
            self.screen.bgcolor('black')
            time.sleep(.5)
            self.colorAns.append(self.col.capitalize())

    def inputColors(self):
        self.obj = cP.colorPallette()
        self.obj.createPallette()
        self.obj.mainLoop()
        self.data = self.obj.dataList

    def checkAnswers(self):
        if self.colorAns == self.data:
            self.score = self.levelNo * 10 + self.score
            self.levelNo = self.levelNo + 1
            self.scoreBoard()
            self.advance()
        else:
            self.endTurtle.write('Your Score is ' + str(self.score) + '\nClick anywhere to restart', font=self.theFont,align='center')

            self.screen.listen()
            turtle.onscreenclick(self.restart)

    def scoreBoard(self):
        self.highScore()
        self.scoreTurtle.clear()
        self.highScoreTurtle.clear()
        self.scoreTurtle.write('Score:' + str(self.score),font=self.theFont,align='left')
        self.highScoreTurtle.write('High Score:' + str(self.highSc),font=self.theFont,align='left')

    def highScore(self):
        if self.score >= self.highSc:
            self.highSc = self.score
            self.writeData(self.highSc)
        else:
            self.highSc = self.highSc

    def writeData(self):
        handlew = open('/Users/tarun/Documents/Python Codes/Games/Mind Game/highScoretracker.txt', 'w')
        handlew.write(str(self.highSc))
        handlew.close()

    def startGame(self):
        self.createTurtles()
        self.startUp()
        self.timer('The game begins in ',1)
        self.scoreBoard()
        self.colorGen()
        self.inputColors()
        self.checkAnswers()

    def restart(self,x,y):
        self.score = 0
        self.levelNo = 1
        self.endTurtle.clear()
        self.timer('The game begins in ',1)
        self.scoreBoard()
        self.colorGen()
        self.inputColors()
        self.checkAnswers()

    def advance(self):
        self.timer('The level begins in ',0.5)
        self.colorGen()
        self.inputColors()
        self.checkAnswers()
        
mindGame = mindGameOOPS()
mindGame.startGame()
turtle.done()