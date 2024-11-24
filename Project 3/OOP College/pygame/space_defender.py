import pygame
import random
import sys

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Defender Ultra")
clock = pygame.time.Clock()


# Picture
background = pygame.image.load("picture/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load("picture/player.png")
player_img = pygame.transform.scale(player_img, (50, 30))
meteor_img = pygame.image.load("picture/meteor.png")
meteor_img = pygame.transform.scale(meteor_img, (40, 40))



# Sound
shoot_sound = pygame.mixer.Sound("sound/shoot.wav")
explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
gameover_sound = pygame.mixer.Sound("sound/game-over.wav")

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Player(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = player_img
        self.speed = 7
        self.lives = 5

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
    
    def shoot(self):
        shoot_sound.play()
        return Bullet(self.rect.centerx, self.rect.top, 5, 10, GREEN)

class Meteor(GameObject):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color)
        self.image = meteor_img
        self.speed = speed 
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def fall(self):
        self.rect.y += self.speed

class Bullet(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.speed = -10
    
    def move(self):
        self.rect.y += self.speed


def main():

    player = Player(WIDTH // 2, HEIGHT - 60, 50, 30, BLUE)

    meteors = []
    bullets = []

    score = 0
    running = True
    game_over = False

    # Inisialisasi Font untuk Pesan Game Over
    font = pygame.font.SysFont(None, 74)

    while running:
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        player.move(keys)

        if random.randint(1, 50) == 1:
            meteors.append(Meteor(random.randint(0, WIDTH - 40), 0, 40, 40, RED, random.randint(3, 7)))

        for meteor in meteors[:]:
            meteor.fall()
            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)
                player.lives -= 1
                if player.lives <= 0:
                    gameover_sound.play()
                    print(f"Game Over! Your Score: {score}")
                    pygame.time.delay(6000)
                    running = False

        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        for bullet in bullets[:]:
            for meteor in meteors[:]:
                if bullet.rect.colliderect(meteor.rect):
                    explosion_sound.play()
                    bullets.remove(bullet)
                    meteors.remove(meteor)
                    score += 1
                    break

        player.draw(screen)
        for meteor in meteors:
            meteor.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
    else:
        #Menampilkan pesan Game Over
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

if __name__== "__main__":
    main()