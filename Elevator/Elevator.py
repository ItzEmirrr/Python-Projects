import pygame
import sys

class Lift:
    def __init__(self):
        pygame.init()

        self.width, self.height = 800, 600
        self.image_width, self.image_height = 50, 50
        self.panel_color = (150, 150, 150)
        self.text_color = (0, 0, 0)
        self.font_size = 56
        self.black = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Elevator3000")

        self.lift = pygame.image.load('lift.png')
        self.bg = pygame.image.load('liftbg.png')

        self.lift_x, self.lift_y = self.width // 1.6 - self.image_width // 2, self.height // 1.45 - self.image_height // 2

        self.target_x, self.target_y = self.lift_x, self.lift_y

        self.font = pygame.font.Font(None, self.font_size)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in range(1, 5):
                        text_rect = self.get_text_rect(i)
                        if text_rect.collidepoint(event.pos):
                            self.set_target_coordinates(i)

            self.update_lift_position()
            self.draw_screen()

    def get_text_rect(self, i):
        text_surface = self.font.render(str(i), True, self.text_color)
        text_rect = text_surface.get_rect(
            center=(self.width // 8, self.height// 3 + (i - 1) * self.font_size)
        )
        return text_rect

    def set_target_coordinates(self, i):
        self.target_x = 480
        self.target_y = 385 - (i - 1) * 119

    def update_lift_position(self):
        dx, dy = self.target_x - self.lift_x, self.target_y - self.lift_y
        distance = pygame.math.Vector2(dx, dy).length()
        speed = 5
        if distance > speed:
            direction = pygame.math.Vector2(dx, dy).normalize()
            self.lift_x += direction.x * speed
            self.lift_y += direction.y * speed
        else:
            self.lift_x, self.lift_y = self.target_x, self.target_y


    def draw_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.lift, (int(self.lift_x), int(self.lift_y)), (0, 0, 150, 154))


        for i in range(1, 5):
            text_surface = self.font.render(str(i), True, self.text_color)
            text_rect = self.get_text_rect(i)
            pygame.draw.rect(self.screen, self.panel_color, text_rect)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    Lift = Lift()
    Lift.run()