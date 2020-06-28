import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

player1 = gamebox.from_color(300, 300, 'red', 20, 20)

topwalls = {
    gamebox.from_color(800, 0, 'green', 75, 200),
    gamebox.from_color(1000, 0, 'green', 75, 400),
    gamebox.from_color(1200, 0, 'green', 75, 350),
    gamebox.from_color(1400, 0, 'green', 75, 100),

}
bottom_walls = {
 gamebox.from_color(800, 600, 'green', 75, 600),
 gamebox.from_color(1000, 600, 'green', 75, 400),
 gamebox.from_color(1200, 600, 'green', 75, 450),
 gamebox.from_color(1400, 600, 'green', 75, 700)
 }


score = 0
game_over = False
randomized_height = 0


def touching(player1, wall):
    '''
    return true if the player and walls/pillars are touching
    '''
    if player1.right_touches(wall):
        return True
    if player1.left_touches(wall):
        return True
    if player1.top_touches(wall):
        return True
    if player1.bottom_touches(wall):
        return True

    return False


def tick(keys):
    '''
    Creates the flapping motion of the bird for a flappybird-like game, creates the apparent motion of the walls/pillars
    , and establishes the parameters for the score and losing conditions
    :param keys: allows for keys on the keyboard to be referenced in commands and conditional statements
    '''
    global score
    global flap_timer
    global game_over
    global randomized_height
    camera.clear('white')
    if game_over == False:
        if pygame.K_SPACE in keys:
            player1.yspeed = 0
            player1.yspeed -= 20

        player1.speedy += 1.5
        player1.y = player1.y + player1.yspeed

        for wall in topwalls:
            wall.speedx = -4
            wall.x = wall.x + wall.xspeed
            if wall.right < camera.left:
                wall.x = 800
                randomized_height = random.randint(-100, 200)
                wall.y = randomized_height

            if touching(player1, wall):
                game_over = True
                player1.speedx = 0
                player1.speedy = 0
                wall.speedx = 0

            player1.move_to_stop_overlapping(wall)

        for wall in bottom_walls:
            wall.speedx = -4
            wall.x = wall.x + wall.xspeed
            if wall.right < camera.left:
                wall.x = 800
                wall.y = randomized_height + 600

            if touching(player1, wall):
                game_over = True
                player1.speedx = 0
                player1.speedy = 0
                wall.speedx = 0

            player1.move_to_stop_overlapping(wall)

        if player1.y < camera.top:
            game_over = True
        if player1.y > camera.bottom:
            game_over = True

        keys.clear()

        score += 1

    elif game_over:
        player1.yspeed = 0
        for wall in topwalls:
            wall.speedx = 0

    scoreboard = gamebox.from_text(400, 50, str(score // 30), 30, 'black')
    for wall in topwalls:
        camera.draw(wall)
    for wall in bottom_walls:
        camera.draw(wall)
    camera.draw(player1)
    camera.draw(scoreboard)
    camera.display()


gamebox.timer_loop(30, tick)

