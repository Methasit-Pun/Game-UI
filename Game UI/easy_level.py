import pygame
import sys
import random
import time
wave_number = 0
    # Initialize Pygame

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                pygame.DOUBLEBUF)
pygame.display.set_caption('Space Invaders Wave System')

# Load images
background_img = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\space.png").convert_alpha()
player_img = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\spaceship.png").convert_alpha()
bullet_img = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\bullet.png").convert_alpha()
enemy_img1 = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\alien551.gif").convert_alpha()
enemy_img2 = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\enemy2.png").convert_alpha()
enemy_img3 = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\enemy32.png").convert_alpha()
boss_img = pygame.image.load(r"C:\Users\Asus\Desktop\Game UI\Game\img\spaceboss.gif").convert_alpha()  # Load your boss image


def start_easy_level():
    # Fonts
    wave_font = pygame.font.Font(None, 74)
    score_font = pygame.font.Font(None, 36)

    # Player settings
    player_width, player_height = player_img.get_size()
    player_width-=20
    player_height-=20
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y =700
    player_speed = 10

    # Bullet settings
    bullet_width, bullet_height = bullet_img.get_size()
    bullet_speed = 20
    bullet_state = "ready"
    bullet_x = 0
    bullet_y = 0

    last_bullet_time = 0  # Timestamp of the last bullet fired
    fire_rate = 200  # Milliseconds between shots

    # Enemy settings
    enemy_width, enemy_height = enemy_img2.get_size()
    enemy_speed = 2
    enemies = []

    # Boss settings
    boss_health = 20
    boss_active = False
    boss_x = SCREEN_WIDTH // 2 - enemy_width // 2
    boss_y = 0
    boss_last_shot_time = 0
    boss_shoot_interval = 2000  # milliseconds
    boss_width, boss_height = boss_img.get_size()

    # Wave settings
    wave_number = 0
    enemy_count_increase_per_wave = 2
    initial_enemy_count = 3

    spawn_delay = 3
    spawn_delay_decrease_per_wave = 0.2
    current_enemy_spawn_count = 0
    max_enemies_per_wave = 0
    wave_in_progress = False
    wave_delay = 3
    last_spawn_time = 0
    last_wave_time = 0
    bwave = 5
    # Score
    score = 0
    high_score = 0

    # Movement flags
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    # Game states
    running = True

    # Initialize laser attributes
    boss_laser_visible = False
    boss_laser_last_toggle_time = 0
    laser_orientation = 'horizontal'  # Could be 'horizontal' or 'vertical'
    laser_position = 0  # Position where the laser will be fired
    boss_laser_duration = 3000  # Laser visible for 3000 milliseconds (including warning)
    warning_duration = 2000  # Warning visible for 2000 milliseconds
    laser_size = 100
    running = True


    def spawn_enemy():
        global current_enemy_spawn_count, last_spawn_time, spawn_delay
        if not boss_active:
            if current_enemy_spawn_count < max_enemies_per_wave:
                enemy_type = random.randint(1, 3)  # Assuming type 3 are minions
                if SCREEN_WIDTH > enemy_width:  # Check if there's enough space to spawn the enemy
                    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
                else:
                    enemy_x = 0  # Default to 0 if not enough space
                enemy = {
                    'x': enemy_x,
                    'y': 0,
                    'dx': random.choice([-enemy_speed, enemy_speed]),
                    'dy': enemy_speed,
                    'type': enemy_type,
                }
                enemies.append(enemy)
                current_enemy_spawn_count += 1
                last_spawn_time = pygame.time.get_ticks() #at once
        else:
            enemy_type = random.randint(1, 3)  # Assuming type 3 are minions
            enemy = {
                'x': random.randint(0, SCREEN_WIDTH - enemy_width),
                'y': random.randint(0, 200), #SCREEN_HEIGHT - enemy_height
                'dx': random.choice([-enemy_speed, enemy_speed]),
                'dy': enemy_speed,
                'type': enemy_type
            }
            #for i in range(5):
            enemies.append(enemy)
            spawn_delay = 1
            current_enemy_spawn_count += 1
            last_spawn_time = time.time()


    def boss_attack():
        global boss_laser_visible, boss_laser_last_toggle_time, laser_orientation, laser_position
        current_time = pygame.time.get_ticks()

        # Toggle laser visibility and set warning phase
        if current_time - boss_laser_last_toggle_time > boss_laser_duration + warning_duration:
            boss_laser_visible = not boss_laser_visible
            boss_laser_last_toggle_time = current_time
            # Randomly decide orientation and position of the laser
            laser_orientation = random.choice(['horizontal', 'vertical'])
            if laser_orientation == 'horizontal':
                laser_position = random.randint(0, SCREEN_HEIGHT)
            else:
                laser_position = random.randint(0, SCREEN_WIDTH)

        # Draw warning
        if boss_laser_visible and current_time - boss_laser_last_toggle_time < warning_duration:
            color = (242, 158, 145)  # Warning color
            if laser_orientation == 'horizontal':
                pygame.draw.line(screen, color, (0, laser_position), (SCREEN_WIDTH, laser_position), laser_size)
            else:
                pygame.draw.line(screen, color, (laser_position, 0), (laser_position, SCREEN_HEIGHT), laser_size)

        # Fire the laser after the warning duration
        if boss_laser_visible and current_time - boss_laser_last_toggle_time > warning_duration:
            color = (255, 0, 0)  # Laser color
            if laser_orientation == 'horizontal':
                pygame.draw.line(screen, color, (0, laser_position), (SCREEN_WIDTH, laser_position), laser_size)
                # Check if player is hit by the laser
                if player_y <= laser_position <= player_y + player_height:
                    game_over()
            else:
                pygame.draw.line(screen, color, (laser_position, 0), (laser_position, SCREEN_HEIGHT), laser_size)
                # Check if player is hit by the laser
                if player_x <= laser_position <= player_x + player_width:
                    game_over()

    #####################BULLLLLLEEEEEEEEEETTTTTTTTTTTTTTTTTTTTT
            
    def fire_bullet(x, y):
        global bullet_state, bullet_x, bullet_y
        bullet_state = "fire"
        bullet_x = x + player_width // 2 - bullet_width // 2
        bullet_y = y
            
    ##############WAAVEEEEEEEEEEEEEEEEEEEEEEEEEEE     

    def show_wave_message():
        if time.time() - last_wave_time < wave_delay:
            wave_text = wave_font.render(f"Wave {wave_number}", True, (255, 255, 255))
            screen.blit(wave_text, (SCREEN_WIDTH // 2 - wave_text.get_width() // 2,
                                    SCREEN_HEIGHT // 2 - wave_text.get_height() // 2))
            return True
        return False


    def reset_wave():

        global wave_number, max_enemies_per_wave, current_enemy_spawn_count, last_spawn_time, wave_in_progress, last_wave_time, spawn_delay, enemy_speed, boss_health, boss_active
        wave_number += 1
        if wave_number % 2 == 0:
            boss_health = 20 + (wave_number // 10 * 5)
            boss_active = True
            wave_in_progress = True  # Ensure wave is considered 'in progress' while the boss is active
            max_enemies_per_wave = 20  # No normal enemies this wave
        else:
            boss_active = False
            wave_in_progress = True  # Regular waves are in progress
            max_enemies_per_wave = initial_enemy_count + enemy_count_increase_per_wave * (wave_number - 1)
            enemy_speed += 0.5
            enemy_speed = min(enemy_speed, 10)

        current_enemy_spawn_count = 0
        last_spawn_time = time.time()
        last_wave_time = time.time()
        spawn_delay = max(0.2, spawn_delay - spawn_delay_decrease_per_wave)
        
        
        
        
        
    ##########################SCOREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE 
        
    def update_score(points):
        global score, high_score
        score += points
        high_score = max(high_score, score)

        
        
        
    def display_score():
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
        high_score_text = score_font.render("High Score: " + str(high_score), True,
                                            (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text,
                    (SCREEN_WIDTH - high_score_text.get_width() - 10, 10))
    

        
    def game_over():
        global running
        running = False

        
        
        
        
        
        
        
        
    # MAINnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        
        
        
        
    while running:
        screen.blit(background_img, (0, 0))

        # Boss conditions and drawing
        if boss_active:
            screen.blit(boss_img, (boss_x, boss_y)) #boss_x, boss_y
            #update_boss_position()
            boss_attack()
            if pygame.time.get_ticks() - last_spawn_time > spawn_delay:
                spawn_enemy()
            if bullet_state == "fire":
                if bullet_x < boss_x + boss_width and bullet_x + bullet_width > boss_x and \
                bullet_y < boss_y + boss_height and bullet_y + bullet_height > boss_y:
                    bullet_state = "ready"
                    bullet_y = player_y - bullet_height
                    boss_health -= 1
                    if boss_health <= 0:
                        boss_active = False
                        wave_in_progress = False
                        last_wave_time = time.time()

        # Check if wave is not in progress or if boss is defeated then stop the game#############################3
        if (not wave_in_progress and not boss_active) and (time.time() - last_wave_time > wave_delay):
            reset_wave()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_SPACE and bullet_state == "ready":
                    fire_bullet(player_x, player_y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
            current_time = pygame.time.get_ticks()  # Get the current time

        if move_left:
            player_x -= player_speed
        if move_right:
            player_x += player_speed
        if move_up:
            player_y -= player_speed
        if move_down:
            player_y += player_speed

        player_x = max(0, min(SCREEN_WIDTH - player_width, player_x))
        player_y = max(0, min(SCREEN_HEIGHT - player_height, player_y))

        if bullet_state == "fire":
            bullet_y -= bullet_speed
            if bullet_y <= 0:
                bullet_state = "ready"
                
        if bullet_state == "fire" and boss_active:
            if bullet_x < boss_x + boss_width and bullet_x + bullet_width > boss_x and bullet_y < boss_y + boss_height and bullet_y + bullet_height > boss_y:
                bullet_state = "ready"
                bullet_y = player_y - bullet_height
                boss_health -= 1
                if boss_health <= 0:
                    boss_active = False
                    wave_in_progress = False
                    last_wave_time = time.time()


        if show_wave_message():
            pygame.display.flip()
            continue

        if not wave_in_progress and time.time() - last_wave_time > wave_delay:
            reset_wave()

        if current_enemy_spawn_count < max_enemies_per_wave and time.time() - last_spawn_time > spawn_delay:
            spawn_enemy()
        elif len(enemies) == 0 and current_enemy_spawn_count >= max_enemies_per_wave:
            wave_in_progress = False
            last_wave_time = time.time()

        for enemy in enemies[:]:
            if enemy['type'] == 1:
                enemy['x'] += enemy['dx']
                if enemy['x'] <= 0 or enemy['x'] >= SCREEN_WIDTH - enemy_width:
                    enemy['dx'] *= -1
            elif enemy['type'] == 2:
                enemy['y'] += enemy['dy']
                if enemy['y'] > SCREEN_HEIGHT:
                    enemies.remove(enemy)
            elif enemy['type'] == 3:
                enemy['x'] += enemy['dx']
                enemy['y'] += enemy['dy']
                if enemy['x'] < 0 or enemy['x'] > SCREEN_WIDTH - enemy_width:
                    enemy['dx'] *= -1
                    # Ensure the enemy is within bounds after direction change
                    enemy['x'] = max(0, min(SCREEN_WIDTH - enemy_width, enemy['x']))
                if enemy['y'] < 0 or enemy['y'] > SCREEN_HEIGHT - enemy_height:
                    enemy['dy'] *= -1
                    # Ensure the enemy is within bounds after direction change
                    enemy['y'] = max(0, min(SCREEN_HEIGHT - enemy_height, enemy['y']))

        if bullet_state == "fire":
            for enemy in enemies[:]:
                if bullet_x < enemy['x'] + enemy_width and bullet_x + bullet_width > enemy['x'] and \
                bullet_y < enemy['y'] + enemy_height and bullet_y + bullet_height > enemy['y']:
                    bullet_state = "ready"
                    bullet_y = player_y - bullet_height
                    enemies.remove(enemy)
                    update_score(1)
                    break

        for enemy in enemies[:]:
            if player_x < enemy['x'] + enemy_width and player_x + player_width > enemy['x'] and \
            player_y < enemy['y'] + enemy_height and player_y + player_height > enemy['y']:
                game_over()

        screen.blit(player_img, (player_x, player_y))

        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x, bullet_y))

        for enemy in enemies:
            if enemy['type'] == 1:
                screen.blit(enemy_img1, (enemy['x'], enemy['y']))
            elif enemy['type'] == 2:
                screen.blit(enemy_img2, (enemy['x'], enemy['y']))
            elif enemy['type'] == 3:
                screen.blit(enemy_img3, (enemy['x'], enemy['y']))


        display_score()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    start_easy_level()