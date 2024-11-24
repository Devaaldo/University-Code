import pygame
import random
import sys

pygame.init()

# Konfigurasi dasar
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Defender Deluxe")
clock = pygame.time.Clock()

# Muat gambar
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load("player.png")
meteor_img = pygame.image.load("meteor.png")
bullet_img = pygame.image.load("bullet.png")

# Muat suara
shoot_sound = pygame.mixer.Sound("shoot.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

# Kelas objek
class GameObject:
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(image, (width, height))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameObject):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.speed = 7
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        shoot_sound.play()
        return Bullet(self.rect.centerx - 5, self.rect.top, 10, 20, bullet_img)

class Meteor(GameObject):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed

    def fall(self):
        self.rect.y += self.speed

class Bullet(GameObject):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.speed = -10

    def move(self):
        self.rect.y += self.speed

# Fungsi utama
def main():
    player = Player(WIDTH // 2, HEIGHT - 80, 50, 50, player_img)
    meteors = []
    bullets = []
    score = 0
    level = 1
    running = True

    # Background animasi
    background_y = 0

    while running:
        # Animasi latar belakang
        background_y += 2
        if background_y >= HEIGHT:
            background_y = 0

        screen.blit(background, (0, background_y - HEIGHT))
        screen.blit(background, (0, background_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Tambah meteor
        if random.randint(1, 50) == 1:
            meteors.append(Meteor(random.randint(0, WIDTH - 40), 0, 40, 40, meteor_img, random.randint(3, 3 + level)))

        # Perbarui meteors
        for meteor in meteors[:]:
            meteor.fall()
            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)
                player.lives -= 1
                if player.lives <= 0:
                    gameover_sound.play()
                    print(f"Game Over! Your Score: {score}")
                    running = False

        # Perbarui bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Tabrakan
        for bullet in bullets[:]:
            for meteor in meteors[:]:
                if bullet.rect.colliderect(meteor.rect):
                    explosion_sound.play()
                    bullets.remove(bullet)
                    meteors.remove(meteor)
                    score += 1
                    if score % 10 == 0:
                        level += 1
                    break

        # Gambar objek
        player.draw(screen)
        for meteor in meteors:
            meteor.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        # Tampilkan skor dan level
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
        screen.blit(level_text, (10, 90))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
