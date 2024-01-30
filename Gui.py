from CTkMessagebox import CTkMessagebox
import customtkinter
from pynput.keyboard import Listener, KeyCode, Key
import time
import Functions


class ButtonsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, border_width=2)

        self.buttons = [
            {"text": "Get coordinates", "command": Functions.click_coordinates},
            {"text": "Register hotkey", "command": Functions.msg_press_key},
            {"text": "Show coordinates", "command": Functions.show_coordinates},
            {"text": "Help", "command": Functions.show_help},
            {"text": "Clear", "command": Functions.clear}
        ]

        # Create buttons using a loop
        for i, button_config in enumerate(self.buttons):
            customtkinter.CTkButton(self, width=200, height=40, text=button_config["text"],
                                    command=button_config["command"]).grid(row=i, column=0, padx=20, pady=15,
                                                                           sticky="w")


class App(customtkinter.CTk):
    toggle_button = None
    stop_button = Key.esc
    coordinates = []

    customtkinter.set_default_color_theme("green")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_widget_scaling(1.2)  # widget dimensions and text size
    customtkinter.set_window_scaling(1.2)  # window geometry dimensions

    def __init__(self):
        super().__init__()

        self.title("Auto Clicker")
        self.geometry("1000x450")
        self.resizable(False, False)
        self.wm_attributes('-type', 'dialog')  # tells i3 to start as floating instead of tiled
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(row=0, column=0, padx=15, pady=(20, 20), sticky="nw")

        self.button = customtkinter.CTkButton(self, text="Begin Automation", command=Functions.button_test)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
