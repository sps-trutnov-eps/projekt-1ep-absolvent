import pygame
import random

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.cell_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = (20, 0)
        self.food = self.spawn_food()
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    def spawn_food(self):
        while True:
            x = random.randint(0, 39) * self.cell_size
            y = random.randint(0, 29) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

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
                elif event.key == pygame.K_LEFT and self.direction != (0, 0):
                    self.direction = (-20, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-20, 0):
                    self.direction = (20, 0)

    def update(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if new_head in self.snake or new_head[0] < 0 or new_head[0] >= 800 or new_head[1] < 0 or new_head[1] >= 600:
            self.running = False

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill((30, 30, 30))
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0], self.food[1], self.cell_size, self.cell_size))
        
        score_text = self.font.render(f"Skóre: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hadí hra")
    game = SnakeGame(screen)
    game.run()
    pygame.quit()
