import pygame
import socket

import utils

# Pygame start
pygame.init()

# Game title & icon
pygame.display.set_caption("Segev's Battleships - Client")
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
    RemainingShipsClient = 4
    Yourturn = True
    UpdateScreen()
    IP = '127.0.0.1'
    PORT = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((IP, PORT))
    print('Connected')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        while Yourturn is True:
            for event in pygame.event.get():
                if RemainingShipsClient == 0 or RemainingShipsClient < 0:
                    print('You lost!')
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LeftMouse:
                    MousePos = pygame.mouse.get_pos()
                    print('sum')
                    utils.DrawOnEnemy(MousePos)
                    print('sending')
                    utils.SendHitPos(MousePos, server_socket)
                    print('sent')
                    Yourturn = False

        try:
            print('trying client')
#            server_socket.listen(1)
#            client, (ip, port) = server_socket.accept()
            length = server_socket.recv(4).decode('utf-8')
            print('client received length:', length)
            message = server_socket.recv(int(length)).decode('utf-8')
            print (message)
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
                    RemainingShipsClient -= 1
                    utils.DestroyShip(MessageMouseX, MessageMouseY)
            if MessageMouseY == Ship1Y or MessageMouseY == Ship2Y or MessageMouseY == Ship3Y or MessageMouseY == Ship4Y:
                if MessageMouseY == Ship1Y or MessageMouseY == Ship2Y or MessageMouseY == Ship3Y or MessageMouseY == Ship4Y:
                    RemainingShipsClient -= 1
                    utils.DestroyShip(MessageMouseX, MessageMouseY)
            Yourturn = True
        except Exception as e:
            print(e)
            print('exept')
            break

    print("You Win!")


main()

