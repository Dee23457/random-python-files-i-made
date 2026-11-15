# this script uses raylib to make a nice looking cube!
#TODO: figure out a way to add lighting, and also other things.

# import raylib and math, i forgot what it does.
from pyray import *
import math

# setup for the enviorment.
init_window(680, 480, "very nice rotating specimen.. mheheheheeheheh >:)")
target = load_render_texture(320, 240)
set_target_fps(150)
camthing = Camera3D(Vector3(0.0, 3.0, 5.0), Vector3(0.0, 0.0, 0.0), Vector3(0.0, 1.0, 0.0), 45.0, CAMERA_PERSPECTIVE)
pos = Vector3(0.0, 0.0, 0.0)
whatangle = 0.0

while not window_should_close():
    whatangle += 0.01   
    distance = 5.0
    camthing.position.x = math.sin(whatangle) * distance
    camthing.position.z = math.cos(whatangle) * distance
    camthing.position.y = 3.0
    begin_texture_mode(target)
    clear_background(RAYWHITE) 
    begin_mode_3d(camthing)
    # startup for 3D thing.
    draw_cube_v(pos, Vector3(2.0, 2.0, 2.0), BLUE)
    draw_cube_wires_v(pos, Vector3(2.0, 2.0, 2.0), DARKGRAY)
    end_mode_3d()   
    end_texture_mode()
    begin_drawing()
    clear_background(BLACK)
    
    draw_text(f"FPS: {get_fps()}", 10, 10, 20, RED)
    end_drawing()

# clean up your mess before leaving
unload_render_texture(target)
# after player is done worshipping the cube they can close the window and it will stop.
close_window()