import argparse
import time
import threading
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

class MouseClicker:
    def __init__(self, num_clicks, delay):
        self.num_clicks = num_clicks
        self.delay = delay
        self.click_position = None
        self.stop_clicking = False
        self.clicking_done = threading.Event()

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"Mouse clicked at ({x}, {y})")
            self.click_position = (x, y)
            # Stop listener
            return False

    def capture_click_position(self):
        print("Waiting for a left mouse click to get the position")
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def perform_clicks(self):
        if self.click_position:
            x, y = self.click_position
            for n in range(self.num_clicks):
                if self.stop_clicking:
                    print("Clicking stopped by user")
                    break
                print(f"Click number: {n + 1}")
                mouse_controller = Controller()
                mouse_controller.position = (x, y)
                mouse_controller.click(Button.left, 1)
                time.sleep(self.delay)
            print(f"Done clicking total {n + 1} times")
        self.clicking_done.set()

    def stop_clicking_by_esc(self):
        def on_press(key):
            if key == keyboard.Key.esc:
                self.stop_clicking = True
                self.clicking_done.set()
                return False

        with keyboard.Listener(on_press=on_press) as listener:
            self.clicking_done.wait()
            listener.stop()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Simulate mouse clicks at a captured position.")
    parser.add_argument('-c', type=int, default=200, help='Number of clicks to simulate (default is 200)')
    parser.add_argument('-i', type=float, default=0.0, help='Delay between two clicks (default is 0.0)')
    args = parser.parse_args()

    # Create a MouseClicker instance
    clicker = MouseClicker(num_clicks=args.c, delay=args.i)

    # Capture the click position
    clicker.capture_click_position()

    # Start the clicking process in a separate thread
    click_thread = threading.Thread(target=clicker.perform_clicks)
    click_thread.start()

    # Start the key listener to stop clicking
    keyboard_listener_thread = threading.Thread(target=clicker.stop_clicking_by_esc)
    keyboard_listener_thread.start()

    # Wait for the clicking process and key listener to finish
    click_thread.join()
    keyboard_listener_thread.join()

if __name__ == "__main__":
    main()
