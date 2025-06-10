import pygame
import random

CELL_SIZE = 20
MAZE = [
    "11111111111111111111",
    "10000000000000000001",
    "10111111111111111001",
    "10100000000000101001",
    "10101111111010101001",
    "10101000001010101001",
    "10101011101010101001",
    "10101010001010101001",
    "10101110111010101001",
    "10000000000000000001",
    "11111111111111111111"
]

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Bezpečná start pozice
        self.direction = (20, 0)  # Směr doprava
        self.food = self.spawn_food()
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.maze_walls = self.create_walls()

    def create_walls(self):
        walls = []
        for row_index, row in enumerate(MAZE):
            for col_index, cell in enumerate(row):
                if cell == '1':
                    x = col_index * CELL_SIZE
                    y = row_index * CELL_SIZE
                    walls.append((x, y))
        return walls

    def spawn_food(self):
        free_spaces = []
        for row in range(len(MAZE)):
            for col in range(len(MAZE[0])):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                if MAZE[row][col] == '0' and (x, y) not in self.snake:
                    free_spaces.append((x, y))
        return random.choice(free_spaces)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP and self.direction != (0, 20):
                    self.direction = (0, -20)
                elif event.key == pygame.K_DOWN and self.direction != (0, -20):
                    self.direction = (0, 20)
                elif event.key == pygame.K_LEFT and self.direction != (20, 0):
                    self.direction = (-20, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-20, 0):
                    self.direction = (20, 0)

    def update(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        # Kontrola kolize s hadem nebo zdmi
        if new_head in self.snake or new_head in self.maze_walls:
            self.running = False

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for wall in self.maze_walls:
            pygame.draw.rect(self.screen, (100, 100, 100), (*wall, CELL_SIZE, CELL_SIZE))

        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, CELL_SIZE, CELL_SIZE))

        score_text = self.font.render(f"Skóre: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

def run_snake_game():
    pygame.init()
    width = len(MAZE[0]) * CELL_SIZE
    height = len(MAZE) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Had v bludišti")
    game = SnakeGame(screen)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    run_snake_game()
