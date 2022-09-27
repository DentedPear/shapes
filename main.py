import random

import arcade

my_window = arcade.open_window(800,600, "first window demo")
arcade.set_background_color(arcade.color.BLACK)

num = random.randrange(1, 500, 300)


arcade.start_render()
#everything else goes here

arcade.draw_line(100, num, 600, 500, arcade.color.WHITE, 4)

#arcade.draw_line([(20,30), ])

arcade.finish_render()

arcade.run()