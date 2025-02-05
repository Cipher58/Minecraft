import pygame as pg
from camera import Camera
from settings import *
import time
from ChatInput import *

class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)
        self.w_pressed_times = []
        self.chat_input = ChatInputClass()
        self.chat_input_active = False

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def handle_event(self, event):
        # adding and removing voxels with clicks
        if event.type == pg.MOUSEBUTTONDOWN:
            voxel_handler = self.app.scene.world.voxel_handler
            if event.button == 1:
                voxel_handler.add_voxel()
            if event.button == 3:
                voxel_handler.remove_voxel()

    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_control(self):
        w_pressed_times = []
        double_tap_threshold = 2
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time
        if key_state[pg.K_w]:
            current_time = time.time()
            self.w_pressed_times.append(current_time)
            self.w_pressed_times = [t for t in self.w_pressed_times if current_time - t <= double_tap_threshold]

            if len(self.w_pressed_times) >= 2:
                self.run_forward(vel * 3)
                print("Double tap")
            else:
                self.move_forward(vel)

            self.w_pressed_times = []

        if key_state[pg.K_k]:
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
            self.move_forward(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_q]:
            self.move_up(vel)
        if key_state[pg.K_e]:
            self.move_down(vel)
        if key_state[pg.K_SPACE]:
            self.fly_up(vel)
        if key_state[pg.K_LSHIFT]:
            self.fly_down(vel)
        if key_state[pg.K_t]:
            self.chat_input.active = True
        elif self.chat_input_active:
            self.chat_input.handle_event(event)
