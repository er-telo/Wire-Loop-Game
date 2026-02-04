from enum import Enum
import os

SOUND_DIR = '/home/eross/sounds'


def play_sound(name):
    os.system(f"aplay {SOUND_DIR}/{name}.wav")


class LGEvent(Enum):
    TOUCH_START = 0
    TOUCH_MAIN = 1
    TOUCH_END = 2


class LGStateMachine:
    def __init__(self, touches=3):
        self.playing = False
        self.max_touches = touches
        self.touches = 0
        play_sound('xpstartup')

    def on_event(self, event):
        if self.playing:
            match event:
                case LGEvent.TOUCH_MAIN:
                    self.touches += 1
                    if self.touches < self.max_touches:
                        print('Oops!')
                        play_sound('errorsound')
                    else:
                        self.playing = False
                        print('You lose!')
                        play_sound('sadtrombone')

                case LGEvent.TOUCH_END:
                    self.playing = False
                    print('You win!')
                    play_sound('goodjob')
        else:
            match event:
                case LGEvent.TOUCH_START:
                    self.playing = True
                    self.touches = 0
                    play_sound('lets_get_it_on')
                    print('Start!')