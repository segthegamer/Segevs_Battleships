import pygame
import socket

import utils

# Pygame start
pygame.init()

# Game title & icon
pygame.display.set_caption("Segev's Battleships - Server")
icon = pygame.image.load('subicon.png')
pygame.display.set_icon(icon)

# Game window
Screen_Width = 1200
Screen_Height = 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))

# Constants
Black = (0, 0, 0)
Blue = (0, 0, 128)
Red = (256, 0, 0)
LeftMouse = 1
MiddleMouse = 2
RightMouse = 3

# Variables
reply = 1

# Random generation of ship locations
Ship1X, Ship1Y, Ship2X, Ship2Y, Ship3X, Ship3Y, Ship4X, Ship4Y = utils.GlobalShips()


# Background image
def RedrawWindow():
    backround = pygame.image.load('background.png')
    screen.blit(backround, (0, 0))
    pygame.display.update()


# Printing the ships
def MakeShip1():
    pygame.draw.rect(screen, Blue, (Ship1X, Ship1Y, 60, 60))
    pygame.display.update()


def MakeShip2():
    pygame.draw.rect(screen, Blue, (Ship2X, Ship2Y, 60, 60))
    pygame.display.update()


def MakeShip3():
    pygame.draw.rect(screen, Blue, (Ship3X, Ship3Y, 60, 60))
    pygame.display.update()


def MakeShip4():
    pygame.draw.rect(screen, Blue, (Ship4X, Ship4Y, 60, 60))
    pygame.display.update()


def UpdateScreen():
    RedrawWindow()
    MakeShip1()
    MakeShip2()
    MakeShip3()
    MakeShip4()


# Game loop
def main():
    RemainingShipsServer = 4
    Yourturn = False
    UpdateScreen()
    IP = '127.0.0.1'
    PORT = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP, PORT))
    except socket.error as e:
        str(e)

    server_socket.listen(1)
    print("Server Start")

    client, (ip, port) = server_socket.accept()
    print("Connected")

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        while Yourturn is True:
            for event in pygame.event.get():
                if RemainingShipsServer == 0 or RemainingShipsServer < 0:
                    print('You lost!')
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LeftMouse:
                    MousePos = pygame.mouse.get_pos()
                    print('sum')
                    utils.DrawOnEnemy(MousePos)
                    print('sending ', MousePos)
                    utils.SendHitPosFromServer(MousePos, client)
                    print('sent')
                    Yourturn = False
        try:
            length = client.recv(4).decode('utf-8')
            message = client.recv(int(length)).decode('utf-8')
            print(message)
            utils.DrawOnFriendly(message)
            message = message.split(', ')

            MessageMouseX = int(message[0].replace('(', '').replace(')', ''))
            MessageMouseY = int(message[1].replace('(', '').replace(')', ''))
            for i in range(8):
                if 680 + (i * 60) < MessageMouseX < 680 + ((i + 1) * 60):
                    MessageMouseX = 40 + (i * 60)
            for i in range(8):
                if 80 + (i * 60) < MessageMouseY < 80 + ((i + 1) * 60):
                    MessageMouseY = 80 + (i * 60)
            if MessageMouseX == Ship1X or MessageMouseX == Ship2X or MessageMouseX == Ship3X or MessageMouseX == Ship4X:
                if MessageMouseY == Ship1Y or MessageMouseY == Ship2Y or MessageMouseY == Ship3Y or MessageMouseY == Ship4Y:
                    RemainingShipsServer -= 1
                    utils.DestroyShip(MessageMouseX, MessageMouseY)
            if MessageMouseY == Ship1Y or MessageMouseY == Ship2Y or MessageMouseY == Ship3Y or MessageMouseY == Ship4Y:
                if MessageMouseY == Ship1Y or MessageMouseY == Ship2Y or MessageMouseY == Ship3Y or MessageMouseY == Ship4Y:
                    RemainingShipsServer -= 1
                    utils.DestroyShip(MessageMouseX, MessageMouseY)
            if not message:
                print("Disconnected")
                break
            else:
                print("Received", message)
                print("Your turn")
                Yourturn = True
        except Exception as e:
            print('exeptian')
            print(e)
            break

    print("You Win")
    client.close()


main()
