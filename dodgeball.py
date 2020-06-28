import pygame
import gamebox
camera = gamebox.Camera(600, 600)

# player
player1 = gamebox.from_color(300, 300, 'green', 20, 20)
player2 = gamebox.from_color(300, 300, 'magenta', 20, 20)
# ball
ball = gamebox.from_circle(100, 100, 'red', 5)
ball.speedx = 8
ball.speedy = 7
# arena
arena = [
    gamebox.from_color(0, 300, 'black', 100, 600),
    gamebox.from_color(600, 300, 'black', 100, 600),
    gamebox.from_color(300, 0, 'black', 600, 100),
    gamebox.from_color(300, 600, 'black', 600, 100),
    gamebox.from_color(400, 400, 'black', 50, 50)
]

score1 = 3
score2 = 3
winner = None

def touching(box1, box2):
    '''ww
a    return true if the boxes are touching
    '''
    if box1.right_touches(box2):
        return True
    if box1.left_touches(box2):
        return True
    if box1.top_touches(box2):
        return True
    if box1.bottom_touches(box2):
        return True
    return False

def tick(keys):
    global score1
    global score2
    global winner
    camera.clear('white')
    if pygame.K_RIGHT in keys:
        player1.x += 5
    if pygame.K_LEFT in keys:
        player1.x -= 5
    if pygame.K_UP in keys:
        player1.y -= 5
    if pygame.K_DOWN in keys:
        player1.y += 5

    if pygame.K_d in keys:
        player2.x += 5
    if pygame.K_a in keys:
        player2.x -= 5
    if pygame.K_w in keys:
        player2.y -= 5
    if pygame.K_s in keys:
        player2.y += 5

    # detect player colliding with the ball
    if touching(player1, ball):
        player1.color = 'blue'
        score1 -= 1
        print(score1)
    else:
        player1.color = 'green'

    if touching(player2, ball):
        player2.color = 'blue'
        score2 -= 1
        print(score2)
    else:
        player2.color = 'magenta'

    # if a player has a score <1, the other player wins
    if not winner:
        scoreboard_text = 'Player 1: ' + str(score1) + '   Player 2: ' + str(score2)
        if score1 < 1 and not winner:
            winner = 2
        elif score2 < 1 and winner:
            winner = 1
    else:
        scoreboard_text = 'PLAYER ' + str(winner) + ' WINS!'
    scoreboard = gamebox.from_text(300, 10, scoreboard_text, 30, 'white')

    # make the ball bounce
    for obst in arena + [player1, player2]:
        if obst.left_touches(ball) or obst.right_touches(ball):
            ball.speedx = -ball.speedx
        if obst.top_touches(ball) or obst.bottom_touches(ball):
            ball.speedy = -ball.speedy

    ball.move_speed()
    camera.draw(ball)
    for wall in arena:
        player1.move_to_stop_overlapping(wall)
        player2.move_to_stop_overlapping(wall)
        camera.draw(wall)
    player1.move_to_stop_overlapping(ball)
    player2.move_to_stop_overlapping(ball)
    camera.draw(player1)
    camera.draw(player2)
    camera.draw(scoreboard)
    camera.display()

gamebox.timer_loop(30, tick)