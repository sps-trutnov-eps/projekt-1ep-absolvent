import random

class Ohen:
    def __init__(self, okno, rozliseni_x, rozliseni_y, fps, cerna, bila, font):
        self.okno = okno
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.fps = fps
        self.ai_timer = 2 * self.fps

        self.cerna = cerna
        self.bila = bila
        self.font = font

    def ai(self, ai_difficulty_ohen, ohen_stage):
        if self.ai_timer > 0:
            self.ai_timer -= 1

        if self.ai_timer <= 0:
            random_number = random.randint(1, 20)
            print(f"{random_number} <= {ai_difficulty_ohen}")

            if random_number <= ai_difficulty_ohen:
                ohen_stage -= 1
                self.ai_timer = 2 * self.fps

            else:
                self.ai_timer = 2 * self.fps

            if ohen_stage <= 0:
                game = False

        text_stage = self.font.render(str(ohen_stage), True, self.bila)
        text_stage_rect = text_stage.get_rect(center=(self.rozliseni_x / 2, self.rozliseni_y / 2))
        self.okno.blit(text_stage, text_stage_rect)

        return ohen_stage