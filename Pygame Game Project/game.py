"""
Alex Kim: aak3cf
Noal Zyglowicz: ntz3sw
Taylor Barmak: twb4tr

Get from the bottom of the screen to the top of the screen before your opponent.
The door won't open until you have collected all of the triangles.
Your health is represented by the color of your character (green, yellow, red, dead)
The game goes until 8 levels and you get the level number worth of points for finishing first.
If you don't finish before time runs out, nobody gets points for that level.

Things to fix:
The speed of the enemies gets a little too fast later on.
"""

#Import stuffr
import pygame
import gamebox
import random
import math

camera = gamebox.Camera(800, 600)

# two players
p1 = gamebox.from_color(200, 580, 'green', 20, 20)
p2 = gamebox.from_color(600, 580, 'green', 20, 20)

# moving enemies
enemies = [
   gamebox.from_image(200, 250, "cloud.png"),
   gamebox.from_image(600, 250, "cloud.png"),
   gamebox.from_image(200, 350, "cloud.png"),
   gamebox.from_image(600, 350, "cloud.png"),
   gamebox.from_image(400, 100, "cloud.png"),
   gamebox.from_image(300, 150, "cloud.png")
]

# fix the size of the enemies
for a in enemies:
   a.scale_by(0.05)


# collectibles
cl1 = gamebox.from_image(200, 300, "triangle.png")
cl1.scale_by(0.03)
cl2 = gamebox.from_image(100, 450, "triangle.png")
cl2.scale_by(0.03)
cl3 = gamebox.from_image(300, 150, "triangle.png")
cl3.scale_by(0.03)
cr1 = gamebox.from_image(600, 300, "triangle.png")
cr1.scale_by(0.03)
cr2 = gamebox.from_image(500, 450, "triangle.png")
cr2.scale_by(0.03)
cr3 = gamebox.from_image(700, 150, "triangle.png")
cr3.scale_by(0.03)

# doors that prevent the player from completing the level until they have all of the collectibles
door1 = gamebox.from_color(200, 0, 'grey', 100, 20)
door2 = gamebox.from_color(600, 0, 'grey', 100, 20)

# important variables
game_on = False
level = 0
p1_health = 3
p2_health = 3
ticks = 0
p1_score = 0
p2_score = 0

#Background color
background = 'black'

# walls of the game
# arena = [
#    gamebox.from_color(400, 300,  neon, 20, 600),
#    gamebox.from_color(0, 300, neon, 20, 600),
#    gamebox.from_color(400, 600, neon, 800, 100),
#    gamebox.from_color(800, 300, neon, 20, 600),
#    gamebox.from_color(60, 0, neon, 180, 20),
#    gamebox.from_color(400, 0, neon, 300, 20),
#    gamebox.from_color(740, 0, neon, 180, 20)
# ]

def start_level():
   """
   Resets the state of the game to prepare for the next level.
   """
   global level
   global p1_health
   global p2_health
   global ticks

   level += 1


   # Put the players back at the starting position
   p1.x = 200
   p1.y = 580
   p2.x = 600
   p2.y = 580

   # Give the players their health back
   p1_health = 3
   p2_health = 3

   # ticks variable is used for the timer
   ticks = (35 - (level * 3)) * 30

   # Resets the position of the collectibles
   cl1.y = 300
   cl2.y = 450
   cl3.y = 150
   cr1.y = 300
   cr2.y = 450
   cr3.y = 150

   # Puts the doors back
   door1.y = 0
   door2.y = 0

   # Resets the enemies
   for a in enemies:
       # Give enemies a random direction
       direction = random.randint(1, 2)
       if direction == 1:
           direction = -1
       else:
           direction = 1
       a.speedx = (math.log(level ** 4 * 10)) * direction
       a.speedy = (math.log((level ** 4 - 1) * 10 + 1)) * direction
       # Put enemies in a favorable starting position so players don't get killed right away
       if a.y > 300:
           a.y - 250
       if a.y < 30:
           a.y = 100
       if a.x < 20 or a.x > 780:
           a.x = 400
def touching(item1, item2):
  """
  return true if the boxes are touching
  """
  if item1.right_touches(item2):
      return True
  if item1.left_touches(item2):
      return True
  if item1.top_touches(item2):
      return True
  if item1.bottom_touches(item2):
      return True
  return False
def tick(keys):
   """
   Executes the game.
   """
   # global variables
   global game_on
   global text
   global level
   global p1_health
   global p2_health
   global p1_score
   global p2_score
   global ticks
   global background

    #Changes the color of the walls
   if level % 3 == 1:
       neon = 'orange'
   elif level % 3 == 2:
       neon = 'green'
   else:
       neon = 'purple'

   arena = [
       gamebox.from_color(400, 300, neon, 20, 600),
       gamebox.from_color(0, 300, neon, 20, 600),
       gamebox.from_color(400, 600, neon, 800, 100),
       gamebox.from_color(800, 300, neon , 20, 600),
       gamebox.from_color(60, 0, neon, 180, 20),
       gamebox.from_color(400, 0, neon, 300, 20),
       gamebox.from_color(740, 0, neon, 180, 20)
   ]

   # start the game if the space bar is pressed
   if pygame.K_SPACE in keys and not game_on:
       game_on = True
       start_level()

   # don't let the game go past level 8
   if level > 8:
       game_on = False

   # code of the game
   if game_on:
       camera.clear(background)

       # move the players if they are still alive
       if pygame.K_RIGHT in keys and p2_health > 0:
           p2.x += 7 + level//2
       if pygame.K_LEFT in keys and p2_health > 0:
           p2.x -= 7 + level//2
       if pygame.K_UP in keys and p2_health > 0:
           p2.y -= 7 + level//2
       if pygame.K_DOWN in keys and p2_health > 0:
           p2.y += 7 + level//2
       if pygame.K_d in keys and p1_health > 0:
           p1.x += 5 + level//2
       if pygame.K_a in keys and p1_health > 0:
           p1.x -= 5 + level//2
       if pygame.K_w in keys and p1_health > 0:
           p1.y -= 5 + level//2
       if pygame.K_s in keys and p1_health > 0:
           p1.y += 5 + level//2

       # end the level if the player gets to the top and change the score accordingly
       if p1.top <= camera.top:
           game_on = False
           p1_score += level
       if p2.top <= camera.top:
           game_on = False
           p2_score += level

       # bouncing for enemies and health impacts of players
       for a in enemies:
           if a.right > camera.right or a.left < camera.left:
               a.speedx = -a.speedx
           if a.top < camera.top or a.bottom > camera.bottom:
               a.speedy = -a.speedy
           if a.touches(p1):
               p1_health -= 1
               if 150 < p1.x < 250:
                   p1.x = 300
               else:
                   p1.x = 200
               p1.y = 580
           if a.touches(p2):
               p2_health -= 1
               if 550 < p2.x < 650:
                   p2.x = 700
               else:
                   p2.x = 600
               p2.y = 580
           a.move_speed()
           camera.draw(a)

       # make collectible disappear if it is touched
       if touching(p1, cl1):
           cl1.y = 900
       if touching(p1, cl2):
           cl2.y = 900
       if touching(p1, cl3):
           cl3.y = 900
       if touching(p2, cr1):
           cr1.y = 900
       if touching(p2, cr2):
           cr2.y = 900
       if touching(p2, cr3):
           cr3.y = 900

       # move door if three collectibles are picked up
       if cl1.y == 900 and cl2.y == 900 and cl3.y == 900:
           door1.y = 1200
       if cr1.y == 900 and cr2.y == 900 and cr3.y == 900:
           door2.y = 1200

       # player colors change with their health
       if p1_health == 3:
           p1.color = 'green'
       elif p1_health == 2:
           p1.color = 'yellow'
       elif p1_health == 1:
           p1.color = 'red'
       else:
           p1.color = background
       if p2_health == 3:
           p2.color = 'green'
       elif p2_health == 2:
           p2.color = 'yellow'
       elif p2_health == 1:
           p2.color = 'red'
       else:
           p2.color = background

       # if both players are dead, the level is over
       if p1_health < 1 and p2_health < 1:
           game_on = False

       # code for the countdown
       timer = gamebox.from_text(400,575, str(ticks//30), 55, 'red')
       timerbox = gamebox.from_color(400,575,'black',50,40)
       ticks -= 1
       if ticks < 30:
           game_on = False

       # don't let the player go through the door if it's closed
       p1.move_to_stop_overlapping(door1)
       p2.move_to_stop_overlapping(door1)
       p1.move_to_stop_overlapping(door2)
       p2.move_to_stop_overlapping(door2)

       camera.draw(cl1)
       camera.draw(cl2)
       camera.draw(cl3)
       camera.draw(cr1)
       camera.draw(cr2)
       camera.draw(cr3)
       camera.draw(door1)
       camera.draw(door2)
       camera.draw(p1)
       camera.draw(p2)

       # keep players in the arena
       for a in arena:
           p1.move_to_stop_overlapping(a)
           p2.move_to_stop_overlapping(a)
           camera.draw(a)
       camera.draw(timerbox)
       camera.draw(timer)

   # code for in between levels and end of game
   else:
       camera.clear('black')
       score = "Player 1: " + str(p1_score) + "   Player 2: " + str(p2_score)
       if level == 0:
           instructions = [
               gamebox.from_text(400, 50, "Objective: Collect all items and get from the", 40, "yellow"),
               gamebox.from_text(400, 100, " bottom of the screen to the top of the screen ", 40, "yellow"),
               gamebox.from_text(400, 150, "before your opponent and time runs out.", 40, 'yellow'),
               gamebox.from_text(200, 250, "Player 1: Use WASD ", 40, "yellow"),
               gamebox.from_text(200, 300, "for movement ", 40, "yellow"),
               gamebox.from_text(600, 250, "Player 2: Use the arrow", 40, "yellow"),
               gamebox.from_text(600, 300, " keys for movement", 40, "yellow"),
               gamebox.from_text(400, 400, 'Press space to start', 40, 'yellow'),
               gamebox.from_text(400, 500, "Alex Kim: aak3cf", 30, "yellow"),
               gamebox.from_text(400, 525, "Taylor Barmak: twb4tr", 30, "yellow"),
               gamebox.from_text(400, 550, "Noal Zyglowicz: ntz3sw", 30, "yellow")
           ]
           for a in instructions:
               camera.draw(a)
       elif level < 8:
           text = "Press the spacebar to start level " + str(level + 1) + "."
           instructions = gamebox.from_text(400, 300, text, 50, 'yellow')
           score_board = gamebox.from_text(400, 350, score, 50, 'yellow')
           camera.draw(instructions)
           camera.draw(score_board)
       else:
           if p1_score > p2_score:
               score = 'Player 1 Wins! Score: ' + str(p1_score) + ' - ' + str(p2_score)
           elif p1_score < p2_score:
               score = 'Player 2 Wins! Score: ' + str(p1_score) + ' - ' + str(p2_score)
           else:
               score = 'It\'s a tie! Score: ' + str(p1_score) + ' - ' + str(p2_score)
           score_board = gamebox.from_text(400, 300, score, 70, 'yellow')
           camera.draw(score_board)
   camera.display()

gamebox.timer_loop(30, tick)








#Overall Description
'''
Two players will compete in a split screen competition to get from the bottom of the screen to the top through
moving enemies and obstacles while picking up collectibles. There will be multiple levels and the winner of each
level (fastest) will get a certain number of points depending on the difficulty of the level.
'''
#Required Optional Features(6, because group of 3)
#Enemies
'''
The player(s) will move from the top of the screen to the bottom of the screen while dodging moving enemies.
'''
#Two Player
'''
The game will be a splitscreen where the players race through the enemies from the bottom to the top of the screen.
'''
#Health Bar/Multiple Lives
'''
Player will only be able to take a certain number of hits from enemies/obstacles before dying and having to restart
'''

#Collectibles
'''
Player will need to pick up “stars/coins” in order to complete the level
'''
#Timer
'''
Timer will count downwards for the time the players have to complete the level. If the timer runs out before a player
has completed the level then nobody gets points for that level.
'''
#Multiple Levels
'''
Each level will feature harder (faster/larger quantity) enemies, more collectibles, shorter Timer, etc. For two player,
each level will be worth a certain amount of points based on difficulty. Highest points at the end of all of the
levels wins.
'''


#More features that may be added
#Animation
'''
Player’s and/or enemies may have their own unique movement animations to make the game more aesthetically pleasing
'''
#Multiple game modes?
'''
Game could potentially contain a home interface where different game modes could be selected. The game modes would
involve different scoring systems with importance given to collectibles, health, or time taken to complete the level.
'''

#”Save” Mechanic
'''
Could have a unique code for each level that, once the player completes the level, displays on the screen so that if
the player wants to go back and play that specific level, they don’t have to play the entire game all over again.
'''



