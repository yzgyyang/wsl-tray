import subprocess

from functools import partial

from . import wsl_operations as wsl
from .systray import SysTrayIcon
from .systray.win32_adapter import WM_LBUTTONDBLCLK, WM_RBUTTONUP

APP = "wsl-tray"
APP_DISPLAY = "WSL Tray"


# Actions
def say_hello(systray):
    print("Hello, World!")


def toggle_wsl_state(distro_name, systray):
    return wsl.toggle_state(distro_name)


def open_about(systray):
    cmd = 'explorer "https://github.com/yzgyyang/wsl-tray"'
    subprocess.run(cmd)


def no_action(systray):
    pass


def update_menu(systray):
    # Distros
    info = wsl.get_all_states()
    menu_options = tuple([(f"[{v['state']}] {name}", None, partial(toggle_wsl_state, name)) for name, v in info.items()])
    menu_options += (("-----", None, no_action),)

    # Start/Stop all
    menu_options += (("Terminate All", None, wsl.shutdown_all),)
    menu_options += (("Shutdown All + WSL 2 Backend", None, wsl.shutdown_all),)
    menu_options += (("-----", None, no_action),)

    # About
    menu_options += (("About", None, open_about),)

    systray.update(menu_options=menu_options)


NOTIFY_DICT = {
    WM_LBUTTONDBLCLK: say_hello,
    WM_RBUTTONUP: update_menu,
}


def main():
    systray = SysTrayIcon("icon.ico",
                          APP_DISPLAY,
                          menu_options=tuple(),
                          on_quit=no_action,
                          notify_dict=NOTIFY_DICT)
    systray.start()
