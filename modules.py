import os
import time
import keyboard
import random
import sys
import platform

def clearScreen():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')

def installCR():
    try:
        os.system('pip install --upgrade pip')
        os.system('pip install keyboard')
    except:
        os.system('pip install "'+os.getcwd()+'\\_commonredist\\keyboard-master.zip"')


def mainMenu():
    print("Welcome to:")
    gameTitle()
    print()
    print("  Select Your Game Mode:")
    print("    [1] Easy")
    print("    [2] Medium")
    print("    [3] Hard")
    print("    [4] Special Level")
    print("    [5] Load Previous Game")
    print("    [0] Exit")
    while True:
        if keyboard.is_pressed('1'):
            return 1
        elif keyboard.is_pressed('2'):
            return 2
        elif keyboard.is_pressed('3'):
            return 3
        elif keyboard.is_pressed('4'):
            return 4
        elif keyboard.is_pressed('5'):
            return 5
        elif keyboard.is_pressed('0'):
            return 0

def gameTitle():
    fileHandle = open("highscore.txt", "r")
    highscore = fileHandle.read()   #reads the file to display the highscore
    time.sleep(0.2)
    #artwork credits to: http://patorjk.com/software/taag/#p=display&h=2&v=3&f=ANSI%20Shadow&t=Snake%20Game
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(0.2)
    print("░                                                                                    ░")
    time.sleep(0.2)
    print("░ ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗ ░")
    time.sleep(0.2)
    print("░ ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝ ░")
    print("░ ███████╗██╔██╗ ██║███████║█████╔╝ █████╗      ██║  ███╗███████║██╔████╔██║█████╗   ░")
    time.sleep(0.2)
    print("░ ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   ░")
    time.sleep(0.2)
    print("░ ███████║██║ ╚████║██║  ██║██║  ██╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗ ░")
    # time.sleep(0.2)
    print("░ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ░")
    time.sleep(0.2)
    print("░                                                                                    ░")
    time.sleep(0.2)
    print("░ Highscore: " , highscore.rstrip() , "                                                                   ░")
    time.sleep(0.2)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(0.5)

def snakeMove(HEIGHT, WIDTH, speed_x, speed_y, snake_x, snake_y, tail, heads, count, food_x, food_y, num, score, special):
    # global food_x
    # global food_y

    while True:

        if keyboard.is_pressed('s'):
            while True:     #para continuous na magloop/magmove yung snake forward
                if keyboard.is_pressed('a') or keyboard.is_pressed('d'):    #the loop will break kapag napress yung other keys; para magbago rin yung direction ng snake
                    break
                    time.sleep(0.05)
                elif keyboard.is_pressed('q'):     #pressing q will save the game progress
                    saveProgress(HEIGHT, WIDTH, tail, score, speed_x, speed_y, heads, count, special)
                snake_y += 1    #move downwards
                tail, heads = update(snake_x, snake_y, tail, heads, count)
                if snake_y+2 == HEIGHT: #kapag tumama na sa border
                    endGame(HEIGHT, WIDTH, score, tail)
                    break
                os.system('clear')
                food_x, food_y, heads, count, tail, score = printStage(HEIGHT, WIDTH, snake_x, snake_y, tail, food_x, food_y, heads, count, num, score, special)
                time.sleep(speed_y) #basically yung 'frame rate' ng game; speed ng snake

        elif keyboard.is_pressed('w'):
            while True:
                if keyboard.is_pressed('a') or keyboard.is_pressed('d'):
                    break
                    time.sleep(0.05)
                elif keyboard.is_pressed('q'):
                    saveProgress(HEIGHT, WIDTH, tail, score, speed_x, speed_y, heads, count, special)
                snake_y -= 1
                tail, heads = update(snake_x, snake_y, tail, heads, count)
                if snake_y < 0:
                    endGame(HEIGHT, WIDTH, score, tail)
                    break
                os.system('clear')
                food_x, food_y, heads, count, tail, score = printStage(HEIGHT, WIDTH, snake_x, snake_y, tail, food_x, food_y, heads, count, num, score, special)
                time.sleep(speed_y)

        elif keyboard.is_pressed('d'):
            while True:
                if keyboard.is_pressed('s') or keyboard.is_pressed('w'):
                    break
                    time.sleep(0.05)
                elif keyboard.is_pressed('q'):
                    saveProgress(HEIGHT, WIDTH, tail, score, speed_x, speed_y, heads, count, special)
                snake_x += 1
                tail, heads = update(snake_x, snake_y, tail, heads, count)
                if snake_x+2 == WIDTH:  #applicable lang sa special level
                    for hollow in range((HEIGHT//2)-3,(HEIGHT//2)+2):    #selects the 6 blocks in the middle para maging hollow
                        if snake_y == hollow and special == "True":
                            snake_x = 0     #tatagos yung snake sa screen ang lalabas sa kabila
                            break
                    else:
                        endGame(HEIGHT, WIDTH, score, tail)
                os.system('clear')
                food_x, food_y, heads, count, tail, score = printStage(HEIGHT, WIDTH, snake_x, snake_y, tail, food_x, food_y, heads, count, num, score, special)
                time.sleep(speed_x)

        elif keyboard.is_pressed('a'):
            while True:
                if keyboard.is_pressed('s') or keyboard.is_pressed('w'):
                    break
                    time.sleep(0.05)
                elif keyboard.is_pressed('q'):
                    saveProgress(HEIGHT, WIDTH, tail, score, speed_x, speed_y, heads, count, special)
                snake_x -= 1
                tail, heads = update(snake_x, snake_y, tail, heads, count)
                if snake_x < 0:
                    for hollow in range((HEIGHT//2)-3,(HEIGHT//2)+2):
                        if snake_y == hollow and special == "True":
                            snake_x += WIDTH-1
                            break
                    else:
                        endGame(HEIGHT, WIDTH, score, tail)
                os.system('clear')
                food_x, food_y, heads, count, tail, score = printStage(HEIGHT, WIDTH, snake_x, snake_y, tail, food_x, food_y, heads, count, num, score, special)
                time.sleep(speed_x)

def printStage(HEIGHT, WIDTH, x1, y1, tail, food_x, food_y, heads, count, level, score, special):

    x2 = food_x
    y2 = food_y
    score = count*level

    print("░"*WIDTH)    #upper line sa box
    for row in range(HEIGHT-2): #initialize yung pag print ng rows

        #hollow left side
        for hollow in range((HEIGHT//2)-3,(HEIGHT//2)+2):  #selects the hollow area ng snake game
            if row == hollow and special == "True":     #activates kapag special level yung pinili
                print("|", end='')
                break
        else:
            print("░", end='')  #otherwise, solid siya

        for column in range(WIDTH-2):   #initialize para sa columns naman

            for num in range(1,count+1):
                if heads > count and row == tail[heads-num][1] and column == tail[heads-num][0]: #keeps track of the previous coordinates
                    print("█", end='') #prints the head and tail
                    break
                if num > 3 and tail[heads-num][1] == tail[heads-1][1] and tail[heads-num][0] == tail[heads-1][0]:   #kapag nag collide yung snake sa body niya
                    endGame(HEIGHT, WIDTH, score, tail)

                if (WIDTH//2)-1 == tail[heads-1][0] and special == "True":  #checks if sinelect yung special level
                    for solid in range((HEIGHT//2)-5,(HEIGHT//2)+4):    #creates an obstacle sa gitna ng stage
                        if tail[heads-1][1] == solid:   #pag tumama yung head sa obstacle, then endgame na
                            endGame(HEIGHT, WIDTH, score, tail)

            else:       #after all those checking and printing, saka ilalagay yung food. P.S. Idk how this worked din nag trial and error lang ako :<
                if row == y2 and column == x2:  #ipiprint yung food based sa coordinate niya
                    print("o", end='')
                else:
                    for solid in range((HEIGHT//2)-5,(HEIGHT//2)+4):    #sts the size of the obstacle in the middle
                        if row == solid and column == (WIDTH//2)-1 and special == "True":   #checks kung naka special level
                            print("░", end='')  #solid
                            break
                    else:
                        print(" ", end='')  #hollow

            if row == y2 and column == x2:
                if y2 == tail[heads-1][1] and x2 == tail[heads-1][0]:   #if kinain ng snake yung food
                    count += 1      #counter for the number of heads
                    food_x = random.randint(1,WIDTH-3)  #set the new x coordinate of the food
                    food_y = random.randint(1,HEIGHT-3) #new y cordinate
                    if special == "True":
                        while food_x == (WIDTH//2)-1:   #if the food is in the path of the obstacle
                            food_x = random.randint(1,HEIGHT-3) #set new x value

        #hollow right side
        for hollow in range((HEIGHT//2)-3,(HEIGHT//2)+2):
            if row == hollow and special == "True":
                print("|")
                break
        else:
            print("░")
    print("░"*WIDTH)
    print(" "*((WIDTH//2)-5) +"Score: ", score)
    return food_x, food_y, heads, count, tail, score

def saveGame(tail, score, height, width, speed_x, speed_y, heads, count, special):
    fileHandle = open("gameData.txt", "w")
    fileHandle.write(str(score) + '|' + str(height) + "|" + str(width) + "|" + str(speed_x) + "|" + str(speed_y) + "|" + str(heads) + "|" + str(count) + "|" + str(special) + '\n')
    for i in range(len(tail)):
        fileHandle.write(str(tail[i][0]) + "|" + str(tail[i][1]) + "\n")
    fileHandle.close()

def saveProgress(height, width, tail, score, speed_x, speed_y, heads, count, special):
    print("\n"*5)
    print(" "*((width//2)-22)+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" "*((width//2)-22)+"░    Continue Playing?    [y]es |  [n]o    ░")
    print(" "*((width//2)-22)+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print()
    print()
    while True:
        if keyboard.is_pressed('y'):
            saveGame(tail, score, height, width, speed_x, speed_y, heads, count, special)
            time.sleep(1)
            os.system('clear')
            break
        elif keyboard.is_pressed('n'):
            saveGame(tail, score, height, width, speed_x, speed_y, heads, count, special)
            os.system('clear')
            from snake import snakeGame as snakeGame
            snakeGame()

def goBack(len, height):
    for i in range(height-5):
        print(" ")
    time.sleep(1)
    print(" "*((len//2)-22)+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" "*((len//2)-22)+"░  Go back to main menu?    [y]es |  [n]o  ░")
    print(" "*((len//2)-22)+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print()
    print()
    while True:
        if keyboard.is_pressed('y'):
            os.system('clear')
            from snake import snakeGame as snakeGame
            snakeGame()
        elif keyboard.is_pressed('n'):
            # saveGame(tail, score)
            sys.exit()

def endGame(height,width, score, tail):
    fileHandle = open("gameData.txt", "w")
    fileHandle.write("")    #overwrites the file pag nataya na
    fileHandle.close()

    fileHandle = open("highscore.txt", "r")
    highscore = fileHandle.read()
    highscore = int(highscore.strip())  #para mawala yung white spaces
    fileHandle.close()

    if score > highscore:
        print("Congrats! You beat the current high score!")
        fileHandle = open("highscore.txt", "w")
        fileHandle.write(str(score))
        fileHandle.close()
    time.sleep(1)
    len = width
    height = ((height//2)-3)
    width = ((width//2)-14)
    os.system('clear')
    print("\n"*(height-5) + " "*(width) + "╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗") #28
    time.sleep(0.2)
    print(" "*(width) + "║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝")
    time.sleep(0.2)
    print(" "*(width) + "╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═")
    print()
    print(" "*(width+8) + "Score: ", score)
    goBack(len, height)
#clcepe@up.edu.ph

def update(x1,y1,tail, heads, count):
    tail.append([])
    tail[heads].append(x1)
    tail[heads].append(y1)
    heads += 1
    if heads > count+1:
        tail.pop(1)
        heads -= 1
    return tail, heads
