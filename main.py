def on_button_pressed_a():
    basic.show_string("Hello world!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    basic.show_number(27)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("Hello!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

myImage = images.create_image("""
    . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
""")
myImage.show_image(0, 400)

def on_forever():
    pass
basic.forever(on_forever)
