import os
import time
import keyboard
import random
import sys

from modules import installCR as installCR
from modules import clearScreen as clearScreen
from modules import mainMenu as mainMenu
from modules import gameTitle as gameTitle
from modules import snakeMove as snakeMove
from modules import printStage as printStage
from modules import saveGame as saveGame
from modules import saveProgress as saveProgress
from modules import goBack as goBack
from modules import endGame as endGame
from modules import update as update



def snakeGame():
    while True:
        num = mainMenu()

        tail = []
        heads = 0
        count = 3
        special = False
        if num == 1:
            HEIGHT = 25
            WIDTH = 50
            speed_x = 0.08
            speed_y = 0.12
            score = 0
            snake_x = random.randint(WIDTH//3, WIDTH//2)
            snake_y = random.randint(HEIGHT//3, HEIGHT//2)
            food_x = random.randint(1, WIDTH-3)
            food_y = random.randint(1, HEIGHT-3)
            clearScreen()
            print("[w,a,s,d] to move the snake")
            time.sleep(0.3)
            snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special)
        elif num == 2:
            HEIGHT = 25
            WIDTH = 50
            speed_x = 0.06
            speed_y = 0.09
            score = 0
            snake_x = random.randint(WIDTH//3, WIDTH//2)
            snake_y = random.randint(HEIGHT//3, HEIGHT//2)
            food_x = random.randint(1, WIDTH-3)
            food_y = random.randint(1, HEIGHT-3)
            clearScreen()
            print("[w,a,s,d] to move the snake")
            time.sleep(0.3)
            snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special)
        elif num == 3:
            HEIGHT = 25
            WIDTH = 50
            speed_x = 0.04
            speed_y = 0.06
            score = 0
            snake_x = random.randint(WIDTH//3, WIDTH//2)
            snake_y = random.randint(HEIGHT//3, HEIGHT//2)
            food_x = random.randint(1, WIDTH-3)
            food_y = random.randint(1, HEIGHT-3)
            clearScreen()
            print("[w,a,s,d] to move the snake")
            time.sleep(0.3)
            snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special)
        elif num == 4:
            HEIGHT = 25
            WIDTH = 50
            speed_x = 0.04
            speed_y = 0.06
            score = 0
            snake_x = random.randint(WIDTH//3, WIDTH//2)
            snake_y = random.randint(HEIGHT//3, HEIGHT//2)
            food_x = random.randint(1, WIDTH-3)
            food_y = random.randint(1, HEIGHT-3)
            special = "True"
            clearScreen()
            print("[w,a,s,d] to move the snake")
            time.sleep(0.3)
            snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special)
        elif num == 5:
            part = 0
            list1 = []
            fileHandle = open("gameData.txt", "r")

            if os.stat("gameData.txt").st_size != 0:   #kapag may laman yung file then saka niya lang ilo-load
                for line in fileHandle:
                    # list1.append([])
                    if part == 0:
                        list1.append(line[:-1].split("|"))
                        score = int(list1[part][0])
                        HEIGHT = int(list1[part][1])
                        WIDTH = int(list1[part][2])
                        speed_x = float(list1[part][3])
                        speed_y = float(list1[part][4])
                        heads = int(list1[part][5])
                        count = int(list1[part][6])
                        special = list1[part][7]
                        food_x = random.randint(1, WIDTH-3)
                        food_y = random.randint(1, HEIGHT-3)
                    else:
                        tail.append(line[:-1].split("|"))
                    part += 1
                for i in range(len(tail)):
                    tail[i][0] = int(tail[i][0])
                    tail[i][1] = int(tail[i][1])
                    if i == len(tail)-1:
                        snake_x = tail[i][0]
                        snake_y = tail[i][1]
                # time.sleep(4)
                fileHandle.close()
                clearScreen()
                print("[w,a,s,d] to move the snake")
                time.sleep(0.3)
                snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special)
            else:
                print()
                print()
                print("No Save File Exists")
                print()
                time.sleep(1.5)
                clearScreen()

        elif num == 0:
            sys.exit()



        # elif num == 0:
            # sys.exit()


installCR()

clearScreen()
snakeGame()
