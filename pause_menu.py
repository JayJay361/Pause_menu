import pygame, time, sys
from buttons import Button

class Main_Menu:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Main Menu")
        self.screen = pygame.display.set_mode([1920, 1080])

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("arialblack", 30)
        self.TEXT_COL = (255, 255, 255)

        self.resume_img = pygame.image.load("Button_images/button_resume.png").convert_alpha()
        self.options_img = pygame.image.load("Button_images/button_options.png").convert_alpha()
        self.quit_img = pygame.image.load("Button_images/button_quit.png").convert_alpha()
        self.video_img = pygame.image.load("Button_images/button_video.png").convert_alpha()
        self.audio_img = pygame.image.load("Button_images/button_audio.png").convert_alpha()
        self.keys_img = pygame.image.load("Button_images/button_keys.png").convert_alpha()
        self.back_img = pygame.image.load("Button_images/button_back.png").convert_alpha()

        self.resume_button = Button(856, 255, self.resume_img, 1.5)
        self.options_button = Button(845, 455, self.options_img, 1.5)
        self.quit_button = Button(895, 655, self.quit_img, 1.5)
        self.video_button = Button(856, 355, self.video_img, 1)
        self.audio_button = Button(856, 455, self.audio_img, 1)
        self.keys_button = Button(876, 555, self.keys_img, 1)
        self.back_button = Button(876, 655, self.back_img, 1)


        self.game_paused = False
        self.menu_state = "main"

    def draw_text(self, text, text_col, surface, pos):
        img = self.font.render(text, True, text_col)
        surface.blit(img, pos)

    def run (self):
        while True:
            self.screen.fill((0, 0, 0))

            if self.game_paused == True:
                if self.menu_state == "main":
                    if self.resume_button.draw(self.screen):
                        self.game_paused = False
                    if self.options_button.draw(self.screen):
                        self.menu_state = "options"
                    if self.quit_button.draw(self.screen):
                        pygame.quit()
                        sys.exit()
                if self.menu_state == "options":
                    if self.video_button.draw(self.screen):
                        print("Video Settings")
                    if self.audio_button.draw(self.screen):
                        print("Audio Settings")
                    if self.keys_button.draw(self.screen):
                        print("Change Key Bindings")
                    if self.back_button.draw(self.screen):
                        self.menu_state = "main"

            else:
                self.draw_text("≡", self.TEXT_COL, self.screen, (10, 7))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_paused = True

            pygame.display.update()
            self.clock.tick(60)

Main_Menu().run()


