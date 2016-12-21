
import pygame
import pygame.display as display
import time

SCALE = 20


class CHIP8Display(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((64*SCALE, 32*SCALE))
        self.values = [[0 for _ in xrange(64)] for _ in xrange(32)]
        self.clear_screen()

    def clear_screen(self):
        self.screen.fill((0,0,0))

    def draw_sprite(self, byte_array, x, y, n):
        collision = False

        for byte_index in range(n):
            # byte_array[byte_index]
            for shift in range(8):
                mask = 1 << shift
                # print(mask,byte_array[byte_index],byte_array[byte_index] & mask)
                if (byte_array[byte_index] & mask) != 0:
                    if self.values[x+(7-shift)][y+byte_index] != 0:
                        collision = True
                    self.values[x+(7-shift)][y+byte_index] ^= 1
                    val = self.values[x+(7-shift)][y+byte_index]
                    pygame.draw.rect(self.screen, (val*255,val*255,val*255), pygame.Rect((x+(7-shift))*SCALE, (y+byte_index)*SCALE, SCALE, SCALE))
        display.flip()
        return collision


if __name__ == "__main__":
    pygame.init()

    a = CHIP8Display()
    print(a.draw_sprite(bytearray([0xf0, 0x90, 0x90, 0x90, 0xf0]), 0, 0, 5))
    print(a.draw_sprite(bytearray([0xf0, 0x90, 0x90, 0x90, 0xf0]), 0, 0, 5))
    # a.draw_sprite(bytearray([0xf0]), 0, 0, 1)
