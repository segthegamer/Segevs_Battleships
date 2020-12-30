import random, pygame

# Constants
Black = (0, 0, 0)
Blue = (0, 0, 128)
Red = (255, 0, 0)
LeftMouse = 1
MiddleMouse = 2
RightMouse = 3
Screen_Width = 1200
Screen_Height = 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

def GlobalShips ():
    Ship1RandX = random.randrange(1, 9)
    if Ship1RandX == 1:
        Ship1X = 40
    if Ship1RandX == 2:
        Ship1X = 100
    if Ship1RandX == 3:
        Ship1X = 160
    if Ship1RandX == 4:
        Ship1X = 220
    if Ship1RandX == 5:
        Ship1X = 280
    if Ship1RandX == 6:
        Ship1X = 340
    if Ship1RandX == 7:
        Ship1X = 400
    if Ship1RandX == 8:
        Ship1X = 460
    Ship1RandY = random.randrange(1, 9)
    if Ship1RandY == 1:
        Ship1Y = 80
    if Ship1RandY == 2:
        Ship1Y = 140
    if Ship1RandY == 3:
        Ship1Y = 200
    if Ship1RandY == 4:
        Ship1Y = 260
    if Ship1RandY == 5:
        Ship1Y = 320
    if Ship1RandY == 6:
        Ship1Y = 380
    if Ship1RandY == 7:
        Ship1Y = 440
    if Ship1RandY == 8:
        Ship1Y = 500

    # Ship 2
    Ship2RandX = random.randrange(1, 9)
    while Ship2RandX == Ship1RandX:
        Ship2RandX = random.randrange(1, 9)
    if Ship2RandX == 1:
        Ship2X = 40
    if Ship2RandX == 2:
        Ship2X = 100
    if Ship2RandX == 3:
        Ship2X = 160
    if Ship2RandX == 4:
        Ship2X = 220
    if Ship2RandX == 5:
        Ship2X = 280
    if Ship2RandX == 6:
        Ship2X = 340
    if Ship2RandX == 7:
        Ship2X = 400
    if Ship2RandX == 8:
        Ship2X = 460
    Ship2RandY = random.randrange(1, 9)
    while Ship2RandY == Ship1RandY:
        Ship2RandY = random.randrange(1, 9)
    if Ship2RandY == 1:
        Ship2Y = 80
    if Ship2RandY == 2:
        Ship2Y = 140
    if Ship2RandY == 3:
        Ship2Y = 200
    if Ship2RandY == 4:
        Ship2Y = 260
    if Ship2RandY == 5:
        Ship2Y = 320
    if Ship2RandY == 6:
        Ship2Y = 380
    if Ship2RandY == 7:
        Ship2Y = 440
    if Ship2RandY == 8:
        Ship2Y = 500

    # Ship 3
    Ship3RandX = random.randrange(1, 9)
    while Ship3RandX == Ship1RandX or Ship3RandX == Ship2RandX:
        Ship3RandX = random.randrange(1, 9)
    if Ship3RandX == 1:
        Ship3X = 40
    if Ship3RandX == 2:
        Ship3X = 100
    if Ship3RandX == 3:
        Ship3X = 160
    if Ship3RandX == 4:
        Ship3X = 220
    if Ship3RandX == 5:
        Ship3X = 280
    if Ship3RandX == 6:
        Ship3X = 340
    if Ship3RandX == 7:
        Ship3X = 400
    if Ship3RandX == 8:
        Ship3X = 460
    Ship3RandY = random.randrange(1, 9)
    while Ship3RandY == Ship1RandY or Ship3RandY == Ship2RandY:
        Ship3RandY = random.randrange(1, 9)
    if Ship3RandY == 1:
        Ship3Y = 80
    if Ship3RandY == 2:
        Ship3Y = 140
    if Ship3RandY == 3:
        Ship3Y = 200
    if Ship3RandY == 4:
        Ship3Y = 260
    if Ship3RandY == 5:
        Ship3Y = 320
    if Ship3RandY == 6:
        Ship3Y = 380
    if Ship3RandY == 7:
        Ship3Y = 440
    if Ship3RandY == 8:
        Ship3Y = 500

    # Ship 4
    Ship4RandX = random.randrange(1, 9)
    while Ship4RandX == Ship1RandX or Ship4RandX == Ship2RandX or Ship4RandX == Ship3RandX:
        Ship4RandX = random.randrange(1, 9)
    if Ship4RandX == 1:
        Ship4X = 40
    if Ship4RandX == 2:
        Ship4X = 100
    if Ship4RandX == 3:
        Ship4X = 160
    if Ship4RandX == 4:
        Ship4X = 220
    if Ship4RandX == 5:
        Ship4X = 280
    if Ship4RandX == 6:
        Ship4X = 340
    if Ship4RandX == 7:
        Ship4X = 400
    if Ship4RandX == 8:
        Ship4X = 460
    Ship4RandY = random.randrange(1, 9)
    while Ship4RandY == Ship1RandY or Ship4RandY == Ship2RandY or Ship4RandY == Ship3RandY:
        Ship4RandY = random.randrange(1, 9)
    if Ship4RandY == 1:
        Ship4Y = 80
    if Ship4RandY == 2:
        Ship4Y = 140
    if Ship4RandY == 3:
        Ship4Y = 200
    if Ship4RandY == 4:
        Ship4Y = 260
    if Ship4RandY == 5:
        Ship4Y = 320
    if Ship4RandY == 6:
        Ship4Y = 380
    if Ship4RandY == 7:
        Ship4Y = 440
    if Ship4RandY == 8:
        Ship4Y = 500
    return [Ship1X, Ship1Y, Ship2X, Ship2Y, Ship3X, Ship3Y, Ship4X, Ship4Y]


def DrawOnEnemy (MousePos):

    MouseX = int(MousePos[0])
    MouseY = int(MousePos[1])
    print(MouseX,  '  ', MouseY)

    for i in range(8):
        if 680+(i*60) < MouseX < 680+((i+1)*60):
            MouseX = 680+(i*60)
    for i in range(8):
        if 80+(i*60) < MouseY < 80+((i+1)*60):
            MouseY = 80+(i*60)
    print(MouseX,  '  ', MouseY)
    if MouseX == 680 or 740 or 800 or 860 or 920 or 980 or 1040 or 1100 and MouseY == 80 or 140 or 200 or 260 or 320 or 380 or 440 or 500:
        pygame.draw.rect(screen, Black, (MouseX, MouseY, 60, 60))
        pygame.display.update()

def DrawOnFriendly (MousePos):
    print ("Drawing on friendly")
    MousePos = MousePos.split(', ')
    print (MousePos)

    MouseX = int(MousePos[0].replace('(', '').replace(')', ''))
    MouseY = int(MousePos[1].replace('(', '').replace(')', ''))
    print('', MouseX, ' ', MouseY)

    for i in range(8):
        if 680+(i*60) < MouseX < 680+((i+1)*60):
            MouseX = 40+(i*60)
    for i in range(8):
        if 80+(i*60) < MouseY < 80+((i+1)*60):
            MouseY = 80+(i*60)
    if MouseX == 40 or 100 or 160 or 220 or 280 or 340 or 400 or 460 and MouseY == 80 or 140 or 200 or 260 or 320 or 380 or 440 or 500:
        pygame.draw.rect(screen, Black, (MouseX, MouseY, 60, 60))
        pygame.display.update()

def DestroyShip (MessageMouseX, MessageMouseY):
    print ('Ship hit!')
    pygame.draw.rect(screen, Red, (MessageMouseX, MessageMouseY, 60, 60))
    pygame.display.update()

def SendHitPos (MousePos,server_socket):
    MousePos = str(MousePos)
    print('sendHitPos MousePos: ', MousePos)
    #server_socket.send(str(10).zfill(4).encode('utf-8'))
    server_socket.send(str(len(MousePos)).zfill(4).encode('utf-8'))
    print('sendhitpos content ', MousePos.encode('utf-8'))
    server_socket.send(MousePos.encode('utf-8'))
    print('SendHitPos - sent')

def SendHitPosFromServer (MousePos,client):
    MousePos = str(MousePos)
    print('sendHitPosFromServer MousePos: ', MousePos)
    #server_socket.send(str(10).zfill(4).encode('utf-8'))
    client.send(str(len(MousePos)).zfill(4).encode('utf-8'))
    print('sendhitpos content ', MousePos.encode('utf-8'))
    client.send(MousePos.encode('utf-8'))
    print('SendHitPos - sent')


