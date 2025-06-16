import pygame
import random
import sys

from master import focusWindow

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 26
PLAYER_SPEED = 3
LANE_HEIGHT = 60
LANE_START_Y = 50
NUM_LANES = 16
CAR_WIDTH = 80
CAR_HEIGHT = 40
FPS_LIMIT = 60

# Paths
TEXTURE_PATH = "textury/hrac/zadni_krok2.png"
ROAD_PATH = "smrt_na_silnici/silnice3.png"
SIDEWALK_PATH = "smrt_na_silnici/chodnik.png"
CAR_IMAGES_PATHS = [
    "smrt_na_silnici/tyrak.png",
    "smrt_na_silnici/kia.png",
    "smrt_na_silnici/f1.png",
    "smrt_na_silnici/911.png",
    "smrt_na_silnici/smart.png",
    "smrt_na_silnici/tyrak-bedna.png",
]


def load_and_scale(path, size=None, flip=False):
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    if flip:
        img = pygame.transform.flip(img, True, False)
    return img


def create_lanes():
    return [{
        'rect': pygame.Rect(0, LANE_START_Y + i * LANE_HEIGHT, SCREEN_WIDTH, LANE_HEIGHT),
        'cars': [],
    } for i in range(NUM_LANES)]


def reset_player():
    return pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - int(1.5 * PLAYER_HEIGHT), PLAYER_WIDTH, PLAYER_HEIGHT)


def main(global_data):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("ŽIVOT")
    pygame.font.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 30)

    # Load images
    player_img = load_and_scale(TEXTURE_PATH, (35, 46))
    sidewalk = pygame.image.load(SIDEWALK_PATH).convert_alpha()
    road = pygame.image.load(ROAD_PATH).convert_alpha()
    car_images = [pygame.image.load(p).convert_alpha() for p in CAR_IMAGES_PATHS]

    # Game state
    player = reset_player()
    lanes = create_lanes()
    lives = 3
    game_over = False

    focusWindow()

    while True:
        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return 0

        # --- Movement ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.top -= PLAYER_SPEED
        if keys[pygame.K_s]:
            player.bottom += PLAYER_SPEED
        if keys[pygame.K_a]:
            player.left = max(0, player.left - PLAYER_SPEED)
        if keys[pygame.K_d]:
            player.right = min(SCREEN_WIDTH, player.right + PLAYER_SPEED)

        # --- Drawing ---
        screen.fill("white")

        # Draw sidewalks
        for x in (0, 1024):
            screen.blit(sidewalk, (x, -80))
            screen.blit(sidewalk, (x, 1010))

        # FPS counter (optional debug)
        screen.blit(font.render(f"{int(clock.get_fps())}", True, (255, 255, 255)), (10, 10))

        # Draw lanes and cars
        for lane in lanes:
            screen.blit(road, lane["rect"])
            if not lane["cars"]:
                speed = random.uniform(3, 6)
                direction = random.choice([-1, 1])
                for i in range(random.randint(1, 3)):
                    img = random.choice(car_images)
                    flipped_img = pygame.transform.flip(img, True, False) if direction == -1 else img
                    x_start = SCREEN_WIDTH + i * random.randint(int(CAR_WIDTH * 1.25), int(CAR_WIDTH * 1.5)) if direction == -1 else \
                              -CAR_WIDTH - i * random.randint(int(CAR_WIDTH * 1.25), int(CAR_WIDTH * 1.5))
                    lane["cars"].append({
                        "rect": pygame.Rect(x_start, lane["rect"].y + 10, CAR_WIDTH, CAR_HEIGHT),
                        "img": flipped_img,
                        "speed": direction * speed
                    })

            for car in lane["cars"][:]:
                car["rect"].x += car["speed"]
                screen.blit(car["img"], car["rect"])

                if car["rect"].colliderect(player):
                    player = reset_player()
                    lives -= 1
                    if lives <= 0:
                        game_over = True

                if car["speed"] > 0 and car["rect"].x > SCREEN_WIDTH:
                    lane["cars"].remove(car)
                elif car["speed"] < 0 and car["rect"].x < -CAR_WIDTH:
                    lane["cars"].remove(car)

        # Draw player
        screen.blit(player_img, (player.x, player.y))

        # Lives display
        lives_text = font.render(f"Životy: {lives}", True, (255, 0, 0))
        screen.blit(lives_text, (10, 10))

        if game_over:
            screen.fill("blue")
            pygame.display.set_caption("NO ŽIVOT")
            global_data["neprechozeno"] = True

        if player.y < 0:
            global_data["prechozeno"] = True
            break

        pygame.display.update()
        clock.tick(FPS_LIMIT)
