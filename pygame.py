import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("player.png").convert_alpha()
shell_img = pygame.image.load("shell.png").convert_alpha()

player_img = pygame.transform.scale(player_img, (40, 40))
shell_img = pygame.transform.scale(shell_img, (40, 40))

font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 60)

player_speed = 6
shell_speed = 6
NUM_SHELLS = 3   # 🔥 change this for difficulty

def reset_game():
    player = pygame.Rect(180, 550, 40, 40)
    shells = []
    for _ in range(NUM_SHELLS):
        shell = pygame.Rect(
            random.randint(0, 360),
            random.randint(-600, -40),
            40, 40
        )
        shells.append(shell)
    score = 0
    return player, shells, score

player, shells, score = reset_game()

game_over = False
running = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, shells, score = reset_game()
                game_over = False
            if event.key == pygame.K_q:
                running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < 360:
            player.x += player_speed

        # Move shells
        for shell in shells:
            shell.y += shell_speed

            if shell.y > 600:
                shell.y = random.randint(-200, -40)
                shell.x = random.randint(0, 360)
                score += 1

            if player.colliderect(shell):
                game_over = True

        # Draw game
        screen.blit(player_img, player)
        for shell in shells:
            screen.blit(shell_img, shell)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
        # Lose screen
        lose_text = big_font.render("YOU LOSE", True, (255, 0, 0))
        score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))

        screen.blit(lose_text, (100, 200))
        screen.blit(score_text, (110, 270))
        screen.blit(restart_text, (90, 330))
        screen.blit(quit_text, (110, 370))

    pygame.display.flip()

pygame.quit()
