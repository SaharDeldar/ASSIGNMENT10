from ast import With
from calendar import c
import random
from typing_extensions import Self
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5


class Snake:
    pass

class Apple(arcade.Sprite):
    def __init__(self):
           super().__init__()
           self.color=arcade.color.RED
           self.radius=8
           self.center_x= random.randint(0,500)
           self.center_y= random.randint(0,400)  
    def draw(self)    :
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,self.color)



    

class player(arcade.Sprite):
    def __init__(self):
           super().__init__()
           self.color=arcade.color.DARK_GREEN
           self.width=16
           self.height=16

           self.center_x= 250
           self.center_y= 200 
    def draw(self)    :
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=400,title="SNAKE GAME")
        self._background_color=arcade.color.KHAKI
        self.food=Apple()
        self.player=player()

    def on_draw(self):   
        arcade.start_render( )
        self.food.draw()
        self.player.draw()


class MyGame(arcade.Window):


    def __init__(self, width, height, title):
        

 
        super().__init__(width, height, title)

        self.player_list = None

        self.player = None
        self.Apple_list = None

        self.Apple = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        
        self.player = arcade.SpriteList()

   
        self.player = Player(":resources:images/animated_characters/female_person/"
                                    "femalePerson_idle.png", SPRITE_SCALING)
        self.player.center_x = 50
        self.player.center_y = 50
        self.player.append(self.player)

    def on_draw(self):
       

        
        self.clear()

        
        self.player_list.draw()

    def update(self):
       
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
            
    def on_update(self, delta_time):
        
        self.player_list.update()
        self.Apple_list.update()

    def on_key_press(self, key, modifiers):
        

       
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        

  
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0



g=Game()
arcade.run()

    
    


