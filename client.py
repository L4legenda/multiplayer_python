import pygame
import sys
import pickle
import socket

soc = socket.socket()
soc.connect(("localhost", 5000))

nickname = input("nickname: ")

sc = pygame.display.set_mode((600, 400))

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)



player = {
    "move": {
        "nickname": nickname,
        "speed": 4,
        "cord": {
            "x": 0,
            "y": 0
        }
    },

    "image": {
        "idle": pygame.image.load("image/idle.png")
    }
}

while True:

    soc.send(pickle.dumps(player["move"]))

    data = soc.recv(1024)

    playerPos = pickle.loads(data)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    sc.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player["move"]["cord"]["y"] -= player["move"]["speed"]
    if keys[pygame.K_s]:
        player["move"]["cord"]["y"] += player["move"]["speed"]
    if keys[pygame.K_a]:
        player["move"]["cord"]["x"] -= player["move"]["speed"]
    if keys[pygame.K_d]:
        player["move"]["cord"]["x"] += player["move"]["speed"]

    for p in playerPos:
        fontNickname = myfont.render(playerPos[p]["nickname"], False, (0, 0, 0))
        sc.blit(fontNickname, (playerPos[p]["cord"]["x"], playerPos[p]["cord"]["y"] - 40))
        sc.blit(player["image"]["idle"], (playerPos[p]["cord"]["x"], playerPos[p]["cord"]["y"]))

    pygame.display.update()
    pygame.time.delay(25)
