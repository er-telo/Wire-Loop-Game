import RPi.GPIO as GPIO
import os
import time
from loop_game_sm import LGEvent, LGStateMachine

GPIO.setmode(GPIO.BOARD)
main_loop = 11 # Board pin
end_point = 13
start_point = 15
GPIO.setup(main_loop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(end_point, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(start_point, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


sm = LGStateMachine(touches=8)


def on_touch_event(channel):
    print(f"{time.time()} Touched {channel}")
    if channel == main_loop:
        sm.on_event(LGEvent.TOUCH_MAIN)
    if channel == end_point:
        sm.on_event(LGEvent.TOUCH_END)
    if channel == start_point:
        sm.on_event(LGEvent.TOUCH_START)

db_time = 750

GPIO.add_event_detect(main_loop, GPIO.RISING, callback=on_touch_event, bouncetime=db_time)
GPIO.add_event_detect(end_point, GPIO.RISING, callback=on_touch_event, bouncetime=db_time)
GPIO.add_event_detect(start_point, GPIO.RISING, callback=on_touch_event, bouncetime=db_time)

while True:
    time.sleep(1)



