import os
import pgzrun
import random

#Game window position
os.environ["SDL_VIDEO_CENTERED"] = "1"

#window size
WIDTH = 700
HEIGHT = 700

#title
TITLE = "Car Crossing Game"

#actors & actors positions 
cross_road = Actor("cross_road", (350, 350))
player_car = Actor("player_car", (350, 650))
score_bg = Actor("score_bg", (70, 50))
speed_img = Actor("speed", (600, 50))
game_over_img = Actor("game_over", (350, 300))
win_img = Actor("winner", (350, 300))


#left to right npc cars
ltr_npc_black_car = Actor("npc_black_car", (0, 400))
ltr_npc_green_car = Actor("npc_green_car", (0, 400))
ltr_npc_pink_car = Actor("npc_pink_car", (0, 400))
ltr_npc_red_car = Actor("npc_red_car", (0, 400))
ltr_npc_white_car = Actor("npc_white_car", (0, 400))

#right to left npc cars
rtl_npc_black_car = Actor("rtl_npc_black_car", (600, 300))
rtl_npc_green_car = Actor("rtl_npc_green_car", (600, 300))
rtl_npc_pink_car = Actor("rtl_npc_pink_car", (600, 300))
rtl_npc_red_car = Actor("rtl_npc_red_car", (600, 300))
rtl_npc_white_car = Actor("rtl_npc_white_car", (600, 300))


#npc cars list 
ltr_npc_cars = [ltr_npc_black_car,ltr_npc_green_car,ltr_npc_pink_car,ltr_npc_red_car,ltr_npc_white_car]
rtl_npc_cars = [rtl_npc_black_car,rtl_npc_green_car,rtl_npc_pink_car,rtl_npc_red_car,rtl_npc_white_car]
ltr_random_npc_cars = random.choice(ltr_npc_cars)
rtl_random_npc_cars = random.choice(rtl_npc_cars)

#cars speed
rtl_npc_car_speed = 4
ltr_npc_car_speed = 4
player_car_speed = 5

#game status lose : 1 / win : 2 
game_status = 0

#player score
score = 0

#update
def update():
    
    #read variables that are outside of function
    global score , ltr_random_npc_cars , rtl_random_npc_cars , player_car , rtl_npc_car_speed ,ltr_npc_car_speed,game_status,player_car_speed

    #moving npc cars 
    rtl_random_npc_cars.x -= rtl_npc_car_speed
    ltr_random_npc_cars.x += ltr_npc_car_speed
    if rtl_random_npc_cars.x <= -50 :
        rtl_random_npc_cars.x = 750
    elif ltr_random_npc_cars.x >= 750 :
        ltr_random_npc_cars.x = -50
     

    #Moving the player
    if player_car.y <= 0 :
        #score
        score += 1
        
        if score == 8 :
            player_car_speed += 1

        #npc cars speed
        rtl_npc_car_speed += 1
        ltr_npc_car_speed += 1

        player_car.y = 720

    elif player_car.y >= 725 :
        player_car.y = 650
      
    #control Player car
    if keyboard.up :
        player_car.y -= player_car_speed
    elif keyboard.down :
        player_car.y += player_car_speed
    
    #lose
    if player_car.colliderect(rtl_random_npc_cars) :
        game_status = 1
        rtl_npc_car_speed = 0
        ltr_npc_car_speed = 0

    elif player_car.colliderect(ltr_random_npc_cars) :
        game_status = 1
        rtl_npc_car_speed = 0
        ltr_npc_car_speed = 0
        player_car_speed = 0

    #WIN
    if score == 10 :
        game_status = 2
        rtl_npc_car_speed = 0
        ltr_npc_car_speed = 0
        player_car_speed = 0


#draw
def draw():
    cross_road.draw()
    score_bg.draw()
    speed_img.draw()
    screen.draw.text(f"{score}", color = "black" , topleft = (66,41) , fontsize = 30)
    screen.draw.text(f"{player_car_speed}",fontname="digital" , color = "black" , topright = (640,40) , fontsize = 30)
    player_car.draw()
    ltr_random_npc_cars.draw()
    rtl_random_npc_cars.draw()
    
    #lose
    if game_status == 1 :
        screen.fill("white")
        game_over_img.draw()
        screen.draw.text(f"You Lose ! \n Score : {score} \n\n press SPACE to play again",(180, 400),align="center", color="red", shadow=(1.0,1.0), scolor="black", fontsize=40)       

    #win
    if game_status == 2 :
        screen.fill("white")
        win_img.draw()
        screen.draw.text(f"You are Winner ! \n Score : {score} \n\n press SPACE to play again",(180, 400),align="center", color="green", shadow=(1.0,1.0), scolor="black", fontsize=40)       

#Play again
def on_key_down(key):

    #read variables that are outside of function
    global score , player_car , game_status , ltr_random_npc_cars , rtl_random_npc_cars , rtl_npc_car_speed , ltr_npc_car_speed ,player_car_speed
    
    #press space to restart game
    if key == keys.SPACE:
        game_status = 0
        rtl_npc_car_speed = 4
        ltr_npc_car_speed = 4
        player_car_speed = 5
        score = 0 
        ltr_random_npc_cars = random.choice(ltr_npc_cars)
        rtl_random_npc_cars = random.choice(rtl_npc_cars)
        player_car.y = 650
       
pgzrun.go()