
import pygame
import time

pygame.init()
import pygame.display
info = pygame.display.Info()
print(info)
mag = 20
screen = pygame.display.set_mode((64*mag, 32*mag))

screen.fill((0,0,0))

data = """11110000
10010000
10010000
10010000
11110000"""
x = 0
y = 0
a = 20
for inx, ch in enumerate(data):
    if ch == "0":
        c = (255,0,0)
    elif ch == "1":
        a+=10
        c = (a,a,a)
        print(x,y)
    else:
        y+=1
        x=0
        continue
    pygame.draw.rect(screen, c , pygame.Rect(x*mag,y*mag,mag,mag))
    x+=1

pygame.display.flip()
time.sleep(10)
# screen.fill((0,0,0))
# pygame.display.flip()

# pygame.display.set_mode(resolution=(10,10), flags=0, depth=0)
