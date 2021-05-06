import pygame
import random
# from snake import *


class Apple:
    def init(self):
        self.r = 10
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.color = (255, 0, 0)

    def show(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


class Snake:
    def init(self):
        self.w = 16
        self.h = 16
        self.x = width/2
        self.y = height/2
        self.color = (0, 127, 0)
        self.speed = 2
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []

    def show(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])

        for i in self.body:
            pygame.draw.rect(screen, self.color, i)

    def move(self):
        
        if self.x_change == -1:
            self.x -= self.speed
            # counter=self.w
            # for i in self.body:
            #     i[0]=i[0]-self.speed -counter
            #     counter=counter+counter

        elif self.x_change == 1:
            self.x += self.speed
            # counter=self.w
            # for i in self.body:
            #     i[0]=i[0]+self.speed+counter
            #     counter=counter+counter
            # self.body[:,[0]]+= self.speed

        elif self.y_change == 1:
            self.y += self.speed
            # counter=self.w
            # for i in self.body:
            #     i[1]=i[1]+self.speed+counter
            #     counter=counter+counter
            # self.body[:,[1]]+= self.speed

        elif self.y_change == -1:
            self.y -= self.speed
            # counter=self.w
            # for i in self.body:
            #     i[1]=i[1]-self.speed-counter
            #     counter=counter+counter
            # self.body[:,[1]]-= self.speed


    def eat(self):
        if apple.x-apple.r <= self.x <= apple.x+apple.r and apple.y-apple.r <= self.y <= apple.y+apple.r:
            self.score += 1
            return True
        else:
            return False


if name == "main":
    width = 600
    height = 400

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    # snake.x -= 1
                    snake.x_change = -1
                    snake.y_change = 0

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    # snake.x += 1
                    snake.x_change = +1
                    snake.y_change = 0

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    # snake.y -= 1
                    snake.y_change = -1
                    snake.x_change = 0

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    # snake.y += 1
                    snake.y_change = +1
                    snake.x_change = 0
        snake.move()
        if snake.eat():
            apple = Apple()
            snake.body.append([snake.x-snake.score, snake.y-snake.score, snake.w, snake.h])

        screen.fill((0, 255, 0))
        snake.show()
        apple.show()
        pygame.display.update()
        clock.tick(30)