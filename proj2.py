#countdown timer with sound  alerts
import time
import numpy as np 
import sound_device as sd

def play_beep(frequency=1000, duration=1, samplerate=44100):
    t = np.linespace(0, duration, int(samplerate * duration), endpoint = False) 
    wave = 0.5 * np.sin(2 * np.pi *frequency * t)
    sd.play(wave, samplerate)
    sd.wait()

def countdown(seconds):
    while seconds:
        mins, secs = divmod(second,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -=1

#play beep sound
        play_beep()

        #Example usage
        countdown(10)#countdown for 10 seconds



