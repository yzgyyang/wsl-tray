from systray import SysTrayIcon
from systray.win32_adapter import *

APP = "wsl-tray"
APP_DISPLAY = "WSL Tray"


def say_hello(systray):
    print("Hello, World!")


def update_menu(systray):
    pass


def on_quit_callback(systray):
    pass


NOTIFY_DICT = {
    WM_LBUTTONDBLCLK: say_hello,
}


if __name__ == "__main__":
    menu_options = (("Say Hello", None, say_hello),)
    systray = SysTrayIcon("icon.ico",
                          APP_DISPLAY,
                          menu_options,
                          on_quit=on_quit_callback,
                          notify_dict=NOTIFY_DICT)
    systray.start()
