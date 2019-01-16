import curses
import RPi.GPIO as GPIO
import time

# set GPIO mode
GPIO.setmode(GPIO.BOARD)

# stepper assignment
ControlPin = [3, 5, 7, 8]
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
seq = [[1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 1]]

ControlPin2 = [10, 11, 12, 13]
for pin in ControlPin2:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
# seq2 = [[1, 0, 0, 0],
#        [1, 1, 0, 0],
#        [0, 1, 0, 0],
#        [0, 1, 1, 0],
#        [0, 0, 1, 0],
#        [0, 0, 1, 1],
#        [0, 0, 0, 1],
#        [1, 0, 0, 1]]

ControlPin3 = [15, 16, 18, 19]
for pin in ControlPin3:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
# seq = [[1, 0, 0, 0],
#        [1, 1, 0, 0],
#        [0, 1, 0, 0],
#        [0, 1, 1, 0],
#        [0, 0, 1, 0],
#        [0, 0, 1, 1],
#        [0, 0, 0, 1],
#        [1, 0, 0, 1]]

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()

# exit the program
        if char == ord('q'):
            break

# wrist motion
        elif char == ord('p'):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                time.sleep(0.001)

        elif char == ord('o'):
            for halfstep in range(8 - 1, -1, -1):
                for pin in range(4 - 1, -1, -1):
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                time.sleep(0.001)

# elbow
        elif char == curses.KEY_DOWN:
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin2[pin], seq[halfstep][pin])
                time.sleep(0.001)

        elif char == curses.KEY_UP:
            for halfstep in range(8 - 1, -1, -1):
                for pin in range(4 - 1, -1, -1):
                    GPIO.output(ControlPin2[pin], seq[halfstep][pin])
                time.sleep(0.001)

# shoulder
        elif char == curses.KEY_RIGHT:
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin3[pin], seq[halfstep][pin])
                time.sleep(0.001)

        elif char == curses.KEY_LEFT:
            for halfstep in range(8 - 1, -1, -1):
                for pin in range(4 - 1, -1, -1):
                    GPIO.output(ControlPin3[pin], seq[halfstep][pin])
                time.sleep(0.001)

finally:
    # Close down curses, turn echo back on, cleanup gpio
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
