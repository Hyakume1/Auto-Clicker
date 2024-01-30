from tkinter import messagebox

import pyautogui
from CTkMessagebox import CTkMessagebox
import tkinter
import customtkinter
from pynput.keyboard import Listener, KeyCode, Key
import time

import Gui


def msg_press_key():
    def on_press(key):
        Gui.App.toggle_button = key
        print('{0} pressed'.format(Gui.App.toggle_button))
        return False

    m = CTkMessagebox(title="Attention!", message="Press the button you want to register coordinates with")
    m.update()
    with Listener(on_press=on_press) as listener:
        listener.join()
    CTkMessagebox(title="Attention!", message="You chose the key {0}".format(Gui.App.toggle_button)).update()
    m.destroy()


def button_test():
    print("button pressed")


def clear():
    Gui.App.coordinates.clear()


def show_coordinates():
    CTkMessagebox(title="Coordinates!", message=Gui.App.coordinates)


def show_help():
    CTkMessagebox(title="Help", message="Register a hotkey to begin recording the places you want to click in,"
                                        "then press it again once done. After you press begin automation, press"
                                        "the hotkey to begin the autoclicker", border_width=5,
                  border_color="green")


def click_coordinates():
    if Gui.App.toggle_button is None:
        CTkMessagebox(title="Attention!", message="Please select a hotkey first")
        return

    def on_press(key):
        if key == Gui.App.toggle_button:
            # Get the coordinates
            x, y = pyautogui.position()
            # Print the coordinates
            print(f"X: {x}, Y: {y}")
            Gui.App.coordinates.append([x, y])
        if key == Key.esc:
            return False

    messagebox.showinfo("Attention!", "Press escape once done!")

    with Listener(on_press=on_press) as listener:
        listener.join()
