import arcade
import random
from app_objects import Tank, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"

SPEED = 10

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.tank1_score = 0
        self.tank2_score = 0
        self.speed = 10
        self.tank1 = Tank(200, 200, get_random_color())
        self.tank2 = Tank(600, 600, get_random_color())
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT),
                random.randrange(10, 50)
            )
            for _ in range(10)
        ]
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.tank1.shoot(20)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank1.speed = SPEED
        if symbol == arcade.key.W:
            self.tank2.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank1.speed = -SPEED
        if symbol == arcade.key.S:
            self.tank2.speed = -SPEED
        
        if symbol == arcade.key.SPACE:
            self.tank2.shoot(20)

        if symbol == arcade.key.LEFT:
            self.tank1.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank2.angular_speed = -1.5
        if symbol == arcade.key.RIGHT:
            self.tank1.angular_speed = -1.5
        if symbol == arcade.key.A:
            self.tank2.angular_speed = 1.5
            
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S):
            self.tank1.speed = 0
            self.tank2.speed = 0


        if symbol in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.tank1.angular_speed = 0
            self.tank2.angular_speed = 0



    def on_update(self, delta_time: float):
        self.tank1.update(delta_time)
        self.tank2.update(delta_time)
        for e in self.enemies:
            e.detect_collision(self.tank1)
            
        bullets_to_remove = []
        for bullet in self.tank1.bullets:
            if self.tank2.detect_collision_with_bullet(bullet):
                self.tank1_score += 1
                bullets_to_remove.append(bullet)
                
        for bullet in bullets_to_remove:
            self.tank1.bullets.remove(bullet)

        bullets_to_remove.clear()
        for bullet in self.tank2.bullets:
            if self.tank1.detect_collision_with_bullet(bullet):
                self.tank2_score += 1
                bullets_to_remove.append(bullet)
                
        for bullet in bullets_to_remove:
            self.tank2.bullets.remove(bullet)


        
    def on_draw(self):
        arcade.start_render()
        self.tank1.draw()
        self.tank2.draw()
        for e in self.enemies:
            e.draw()
        arcade.draw_text(f"Player 1 Score: {self.tank1_score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)
        arcade.draw_text(f"Player 2 Score: {self.tank2_score}", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)

    
    
if __name__ == "__main__":
    app = App()
    arcade.run()