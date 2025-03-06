import pygame
import random

pygame.init()

# Настройки экрана
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка иконки
icon = pygame.image.load("img/screen.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_img = pygame.image.load("img/pig.jpg")  
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счет
score = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения счета

# Основной игровой цикл
running = True
while running:
    screen.fill(color)  # Заливка экрана цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка клика мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(f"Клик мыши: ({mouse_x}, {mouse_y})")
            # Проверка, попал ли игрок по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Генерация новых координат для мишени
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  # Увеличиваем счет
                print(f"Попадание! Счет: {score}")  # Для отладки
                print(f"Новые координаты мишени: ({target_x}, {target_y})")  # Отладка координат

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

pygame.quit()