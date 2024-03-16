from pyPS4Controller.controller import Controller
from threading import Thread
import time


class MyController(Controller, Thread):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        Thread.__init__(self)
        self.r2 = 0  # in percent
        self.l2 = 0  # in percent

    def run(self):
        self.listen()

    def on_x_press(self):
        pass

    def on_x_release(self):
        pass

    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        value += 32510  # lower bound
        value = 0 if value < 0 else value
        value = 64000 if value > 64000 else value
        self.l2 = int(value / 64000 * 100)

    def on_L2_release(self):
        self.l2 = 0

    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        value += 32510  # lower bound
        value = 0 if value < 0 else value
        value = 64000 if value > 64000 else value
        self.r2 = int(value / 64000 * 100)

    def on_R2_release(self):
        self.r2 = 0

    def on_up_arrow_press(self):
        pass

    def on_up_down_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_right_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass

    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass

    def on_share_press(self):
        """this event is only detected when connecting without ds4drv"""
        pass

    def on_share_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass

    def on_playstation_button_press(self):
        """this event is only detected when connecting without ds4drv"""
        pass

    def on_playstation_button_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.start()

tickspeed = 0.1
deceleration = 70 * tickspeed  # prozent pro sekunde
acceleration = 0
while True:
    if not controller.r2 == 0 and acceleration >= 0:
        acceleration = controller.r2 - controller.l2
    else:
        if acceleration - deceleration > 0:
            acceleration -= deceleration
        else:
            acceleration = 0
    print(f"{int(acceleration)}                                     ", end="\r")
    time.sleep(tickspeed)
