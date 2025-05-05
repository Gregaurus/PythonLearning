import time
from pynput.keyboard import Controller, Key, Listener

# Initialize the keyboard controller
keyboard = Controller()

# Flag to control the loop
running = True

def auto_key_presser(interval):
    global running
    print("Auto key presser started. Press 'Esc' to stop.")
    try:
        while running:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(interval)  # Wait for the specified interval
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        print("\nAuto key presser stopped.")

def on_press(key):
    global running
    if key == Key.esc:  # Stop when 'Esc' is pressed
        running = False
        return False  # Stop the listener

if __name__ == "__main__":
    # Set the interval in seconds between key presses
    interval = 0.5 # Change this value as needed

    # Start the key listener in a separate thread
    with Listener(on_press=on_press) as listener:
        auto_key_presser(interval)
        listener.join()
        
        
        