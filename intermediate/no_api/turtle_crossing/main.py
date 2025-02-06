import time
from turtle import Turtle,Screen
from character import Character
from car import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)

tim  = Character()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(tim.move,"Up")

is_game_on = True


while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    #Detect collision with cars

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            is_game_on = False
            tim.go_to_start()
            car_manager.clear_the_road()
            scoreboard.game_over()

    #Sucessuful crossing
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.add_score()



screen.exitonclick()