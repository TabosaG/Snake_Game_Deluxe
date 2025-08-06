import pygame
import random
import os
import sys

# Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game Deluxe")
font = pygame.font.SysFont(None, 30)
title_font = pygame.font.SysFont(None, 40)

# Constants
HIGHSCORE_FILE = "highscores.txt"
extra_life_interval = 10
record = 0

# Global state
clock = pygame.time.Clock()

# --- Utility Functions ---
def load_highscore():
    """Load the last saved highscore from file"""
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    hight = 0
    with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().rsplit("-", 1)
            if len(parts) == 2:
                try:
                    score = int(parts[1].strip())
                    if score > hight:
                        hight = score
                except ValueError:
                    continue
    return hight

def save_highscore(player_name, score):
    """Append a new highscore to the file"""
    with open(HIGHSCORE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{player_name} - {score}\n")

def get_player_name():
    """Prompt the player to enter their name"""
    name = ""
    typing = True
    while typing:
        screen.fill((0, 0, 0))
        msg1 = title_font.render("Enter your name:", True, (255, 255, 255))
        msg2 = font.render(name, True, (0, 255, 0))
        screen.blit(msg1, msg1.get_rect(center=(400, 200)))
        screen.blit(msg2, msg2.get_rect(center=(400, 250)))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    char = event.unicode
                    if char.isprintable() and len(name) < 20:
                        name += char

def delete_highscores():
    """Clear the highscore file"""
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "w") as f:
            f.write("")  # Deletes all content

def show_highscores():
    """Display the top 5 highscores on screen"""
    width = screen.get_width()
    running = True

    while running:
        screen.fill((0, 0, 0))

        # Title
        title = title_font.render("Highscores", True, (255, 255, 0))
        screen.blit(title, title.get_rect(center=(width // 2, 30)))

        # Show top 5 highscores
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Sort from highest to lowest score
            def extract_score(line):
                parts = line.rsplit("-", 1)
                try:
                    return int(parts[1].strip())
                except:
                    return 0

            highscores = sorted(lines, key=extract_score, reverse=True)[:5]
            for i, line in enumerate(highscores):
                text = font.render(f"{i + 1}. {line.strip()}", True, (255, 255, 255))
                screen.blit(text, text.get_rect(center=(width // 2, 80 + i * 30)))
        else:
            msg = font.render("No highscores saved yet.", True, (255, 255, 255))
            screen.blit(msg, msg.get_rect(center=(width // 2, 100)))

        # Options
        options = font.render("[D] Delete highscores | [M] Main menu", True, (200, 200, 200))
        screen.blit(options, options.get_rect(center=(width // 2, 280)))

        pygame.display.update()

        # Event handling for the highscore screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    running = False  # Return to main menu
                elif event.key == pygame.K_d:
                    delete_highscores()  # Clear the file

def show_main_menu():
    """Display the main menu options"""
    screen.fill((30, 30, 30))
    width = screen.get_width()

    title = title_font.render("Snake Game Deluxe", True, (255, 255, 255))
    instructions = font.render("[SPACE] Play | [R] Highscores | [ESC] Exit", True, (200, 200, 200))

    screen.blit(title, title.get_rect(center=(width // 2, 140)))
    screen.blit(instructions, instructions.get_rect(center=(width // 2, 200)))
    pygame.display.update()

def pause_menu():
    """Display the pause menu"""
    screen.fill((0, 0, 0))
    width = screen.get_width()

    title = title_font.render("Paused", True, (255, 255, 255))
    options = font.render("[C] Continue | [R] Restart | [ESC] Exit", True, (200, 200, 200))

    screen.blit(title, title.get_rect(center=(width // 2, 140)))
    screen.blit(options, options.get_rect(center=(width // 2, 200)))
    pygame.display.update()

def game_over_menu(score):
    """Handle game over screen and menu"""
    name = get_player_name()
    save_highscore(name, score)
    width = screen.get_width()

    while True:
        screen.fill((0, 0, 0))

        title = title_font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Your score: {score}", True, (255, 255, 255))
        options = font.render("[N] New Game | [V] View Highscores | [M] Main Menu | [ESC] Exit", True, (200, 200, 200))

        screen.blit(title, title.get_rect(center=(width // 2, 130)))
        screen.blit(score_text, score_text.get_rect(center=(width // 2, 180)))
        screen.blit(options, options.get_rect(center=(width // 2, 230)))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    return "new"
                elif event.key == pygame.K_v:
                    show_highscores()
                elif event.key == pygame.K_m:
                    return "menu"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def show_congratulations(score):
    """Display the victory screen when player reaches max score"""
    name = get_player_name()  # Reuses the name input logic
    save_highscore(name + " (VICTORY)", score)

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        msg1 = title_font.render("Congratulations!", True, (0, 255, 0))
        msg2 = font.render(f"{name}, you won with {score} points!", True, (255, 255, 255))
        msg3 = font.render("[M] Main Menu  |  [ESC] Exit", True, (200, 200, 200))

        screen.blit(msg1, msg1.get_rect(center=(400, 200)))
        screen.blit(msg2, msg2.get_rect(center=(400, 250)))
        screen.blit(msg3, msg3.get_rect(center=(400, 300)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return "menu"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# --- Main Game Function ---
def play():
    global highscore
    global record

    # Initial state
    snake = [(100, 50)]
    direction = (10, 0)
    food = [(300, 200)]
    lives = 0
    score = 0
    extra_life_counter = 0
    paused = False
    running = True
    base_speed = 15
    max_speed = 30
    speed = base_speed
    max_score = 100
    invulnerable_start_time = 0
    invulnerable = False


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pause_menu()
                elif event.key == pygame.K_UP and direction != (0, 10):
                    direction = (0, -10)
                elif event.key == pygame.K_DOWN and direction != (0, -10):
                    direction = (0, 10)
                elif event.key == pygame.K_LEFT and direction != (10, 0):
                    direction = (-10, 0)
                elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                    direction = (10, 0)

        # Disable invulnerability after 5 seconds (5000ms)
        if invulnerable and pygame.time.get_ticks() - invulnerable_start_time >= 5000:
            invulnerable = False

        # Pause loop
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_r:
                        return True  # Restart game
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        # Update snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        ate_food = False
        for i, f in enumerate(food):
            if new_head == f:
                score += 1
                if score >= max_score:
                    show_congratulations(score)
                    return "menu"
                speed = min(base_speed + (score // 20), max_speed)
                ate_food = True
                food[i] = (random.randrange(0, 800, 10), random.randrange(30, 600, 10))
                break

        if ate_food:
            if score % 20 == 0 and lives < 3:
                lives += 1

            # Increase visible food items every 10 points
            if len(food) < score // 10 + 1:
                food.append((random.randrange(0, 800, 10), random.randrange(30, 600, 10)))
        else:
            snake.pop()

        # Collisions
        # Check if the snake crashed into itself or the wall
        crashed = (
            new_head in snake[1:]
            or new_head[0] < 0 or new_head[0] >= 800
            or new_head[1] < 30 or new_head[1] >= 600
        )

        # Only apply death logic if not invulnerable
        if crashed and not invulnerable:
            if lives > 0:
                lives -= 1
                invulnerable = True
                invulnerable_start_time = pygame.time.get_ticks()

                # Move the snake's head slightly backward to avoid repeat collisions
                x, y = snake[0]
                dx, dy = direction
                snake[0] = (max(0, min(790, x - dx * 2)), max(30, min(590, y - dy * 2)))

            else:
                record = max(record, score)
                return game_over_menu(score)

        # Draw screen
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 800, 30))

        # Centered title bar
        title = title_font.render("Snake Game", True, (0, 255, 0))
        screen.blit(title, title.get_rect(center=(800 // 2, 15)))

        # Score, lives, highscore display
        status_text = font.render(f"Score: {score} | Lives: {lives} | Highscore: {highscore}", True, (255, 255, 255))
        screen.blit(status_text, status_text.get_rect(center=(800 // 2, 45)))

        # Show [P] Pause option
        pause_text = font.render("[P] Pause", True, (255, 255, 255))
        screen.blit(pause_text, pause_text.get_rect(topright=(800 - 10, 32)))

        if not invulnerable or (pygame.time.get_ticks() // 250) % 2 == 0:
            for part in snake:
                pygame.draw.rect(screen, (0, 255, 0), (*part, 10, 10))
        for f in food:
            pygame.draw.rect(screen, (255, 0, 0), (*f, 10, 10))

        pygame.display.update()
        clock.tick(speed)

def main():
    global highscore
    highscore = load_highscore()
    while True:
        show_main_menu()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                    elif event.key == pygame.K_r:
                        show_highscores()
                        show_main_menu()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        action = play()
        if action == "new":
            continue  # start a new game immediately
        elif action == "menu":
            continue  # return to the main menu
        else:
            break  # exit the game

main()
