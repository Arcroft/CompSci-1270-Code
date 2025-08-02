# Ashlyn Croft
# 29Jul25
# Lab 10
# Chimp Refactor
# Reminds me of those early 2000's ads where the premise is exactly this

import os
import pygame

class NoneSound:
    def play(self):
        pass




class Entity(pygame.sprite.Sprite):
    def __init__(self, name, data_dir, colorkey=None, scale=1):
        pygame.sprite.Sprite.__init__(self)
        fullname = os.path.join(data_dir, name)
        image = pygame.image.load(fullname)
        image = image.convert()
        image = pygame.transform.scale_by(image, scale)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        self.image = image
        self.rect = image.get_rect()





class Fist(Entity):
    def __init__(self, data_dir):
        super().__init__("fist.png", data_dir, -1)
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punching = False





class Chimp(Entity):
    def __init__(self, data_dir):
        super().__init__("chimp.png", data_dir, -1, 4)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image


# I feel like I'm having dejavu. I havn't seen these in at least a decade, and man, they used to be as common in ads as those stupid "little guy picks up +1 point, attacks 3400 power enemy and dies, can you do better?" ads that are everywhere now


def load_sound(name, data_dir):
    if not pygame.mixer.get_init():
        return NoneSound()

    try:
        fullname = os.path.join(data_dir, name)
        sound = pygame.mixer.Sound(fullname)
        return sound
    except (FileNotFoundError, pygame.error):
        print(f"Error: Could not load sound file {name}")
        return NoneSound()





def main():
    pygame.init()
    
    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")
    
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    font = pygame.Font(None, 64)
    text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    whiff_sound = load_sound("whiff.wav", data_dir)
    punch_sound = load_sound("punch.wav", data_dir)
    chimp = Chimp(data_dir)
    fist = Fist(data_dir)
    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.Clock()

    going = True
    while going:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()
                    chimp.punched()
                else:
                    whiff_sound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()





if __name__ == "__main__":
    main()