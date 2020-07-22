from functools import partial

import wsl_operations as wsl

from systray import SysTrayIcon
from systray.win32_adapter import *

APP = "wsl-tray"
APP_DISPLAY = "WSL Tray"


# Actions
def say_hello(systray):
    print("Hello, World!")


def toggle_wsl_state(distro_name, systray):
    return wsl.toggle_state(distro_name)


def update_menu(systray):
    # Distros
    info = wsl.get_all_states()
    menu_options = tuple([(f"[{v['state']}] {name}", None, partial(toggle_wsl_state, name)) for name, v in info.items()])

    # Start/Stop all
    menu_options += (("Terminate All", None, wsl.shutdown_all),)
    menu_options += (("Shutdown All + WSL 2 Backend", None, wsl.shutdown_all),)

    systray.update(menu_options=menu_options)


def on_quit_callback(systray):
    pass


NOTIFY_DICT = {
    WM_LBUTTONDBLCLK: say_hello,
    WM_RBUTTONUP: update_menu,
}


if __name__ == "__main__":
    systray = SysTrayIcon("icon.ico",
                          APP_DISPLAY,
                          menu_options=tuple(),
                          on_quit=on_quit_callback,
                          notify_dict=NOTIFY_DICT)
    systray.start()
