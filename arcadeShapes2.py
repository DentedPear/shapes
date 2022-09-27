import arcade

arcade.open_window(1000, 900, "More Shapes")

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(50, 150, 200, 50, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_outline(300, 800, 300, 60, arcade.color.ORANGE, 4)

arcade.draw_xywh_rectangle_outline(10, 10, 380, 260, arcade.color.ORANGE, 4)

arcade.draw_arc_filled(100, 100, 300, 300, arcade.color.CATALINA_BLUE, 400, 200, 500, 300)

arcade.draw_triangle_outline(300, 400, 700, 800, 600, 400, arcade.color.BANANA_MANIA, 8)
arcade.draw_triangle_filled(300, 700, 100, 700, 100, 400, arcade.color.WHITE)
arcade.finish_render()

arcade.run()