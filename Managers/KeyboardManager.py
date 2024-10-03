from pynput.keyboard import Key, Controller
import time

class KeyboardManager:
    def __init__(self):
        self.keyboard = Controller()

    def tap_key(self, key):
        """
        Tap a single key.
        
        Parameters:
        key (str or Key): The key to tap.
        """
        self.keyboard.tap(key)

    def tap_keys(self, keys): 
        """
        Tap multiple keys in sequence without delay.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        """
        for key in keys:
            self.keyboard.tap(key)
            
    def tap_keys_with_delay(self, keys, delay):
        """
        Tap multiple keys in sequence with a delay between each tap.
        
        Parameters:
        keys (list of str or Key): A list of keys to tap.
        delay (float): The delay in seconds between each key tap.
        """
        for key in keys:
            self.keyboard.tap(key)
            time.sleep(delay)