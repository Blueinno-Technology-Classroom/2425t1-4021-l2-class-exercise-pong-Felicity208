import pgzrun
import random


WIDTH = 640
HEIGHT = 480

player1 = Rect(10, 10, 20, 50)
player2 = Rect(WIDTH - 10 - 20, 10, 20, 50)
ball = Rect(WIDTH/2, HEIGHT/2, 20, 20)

y_speed = 5 + random.randint (0, 2)
x_speed = 5 + random.randint (0, 2)

player1_score = 0
player2_score = 0


def update():
    global y_speed, x_speed, player1_score, player2_score

    ball.y = ball.y +y_speed
    ball.x = ball.x +x_speed
    if ball.bottom > HEIGHT or ball.top < 0:
        y_speed = -y_speed
    if ball.right > WIDTH or ball.left < 0:
        
        if ball.right > WIDTH:
            player1_score += 1
        else:
            player2_score += 1
        ball.x = WIDTH/2
        ball.y = HEIGHT/2    


    if keyboard.UP:
        #print ("up")
        player1.y -= 6
    if keyboard.DOWN:
        player1.y += 6
    
    if player1.top < 0:
        player1.top = 0
    if player1.bottom > HEIGHT: 
        player1.bottom = HEIGHT

    if ball.colliderect(player1) or ball.colliderect(player2):
        x_speed = -x_speed
    
    #player2.centery = random.randint(ball.centery-50, ball.centery + 50) 
    if player2.centery > ball.centery:
        player2.y -= random.randint(3, 6)
    else:
        player2.y += random.randint(3, 6) 



def draw():
    screen.clear()
    screen.draw.filled_rect(player1, "white")
    screen.draw.filled_rect(player2, "white")
    screen.draw.filled_rect(ball, "purple")
    screen.draw.text(str(f'{player1_score} : {player2_score}'), center=(WIDTH/2, 10))


pgzrun.go()
