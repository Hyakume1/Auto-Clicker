import pyautogui
from pynput.keyboard import Listener, KeyCode, Key
from Gui import App  # Import the GUI module
import threading

# Call the create_gui function to create the GUI
app = App()
app.mainloop()
# with Listener(on_press=toggle_event, on_release=stop_listening) as listener:
#     listener.join()
