import locale
import os

import gi
from enum import Enum

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# path to *.glade files
UI_RESOURCES_PATH = "app/ui/" if os.path.exists("app/ui/") else "/usr/share/demoneditor/app/ui/"

# translation
TEXT_DOMAIN = "demon-editor"
if UI_RESOURCES_PATH == "app/ui/":
    LANG_DIR = UI_RESOURCES_PATH + "lang"
    locale.bindtextdomain(TEXT_DOMAIN, UI_RESOURCES_PATH + "lang")

theme = Gtk.IconTheme.get_default()
_IMAGE_MISSING = theme.load_icon("image-missing", 16, 0) if theme.lookup_icon("image-missing", 16, 0) else None
CODED_ICON = theme.load_icon("emblem-readonly", 16, 0) if theme.lookup_icon(
    "emblem-readonly", 16, 0) else _IMAGE_MISSING
LOCKED_ICON = theme.load_icon("changes-prevent-symbolic", 16, 0) if theme.lookup_icon(
    "system-lock-screen", 16, 0) else _IMAGE_MISSING
HIDE_ICON = theme.load_icon("go-jump", 16, 0) if theme.lookup_icon("go-jump", 16, 0) else _IMAGE_MISSING
TV_ICON = theme.load_icon("tv-symbolic", 16, 0) if theme.lookup_icon("tv-symbolic", 16, 0) else _IMAGE_MISSING
IPTV_ICON = theme.load_icon("emblem-shared", 16, 0) if theme.load_icon("emblem-shared", 16, 0) else None

# Colors
NEW_COLOR = "#ffe6cc"  # Color for new services in the main list
EXTRA_COLOR = "#b3e6cc"  # Color for services with a extra name for the bouquet


class KeyboardKey(Enum):
    """ The raw(hardware) codes of the keyboard keys """
    E = 26
    R = 27
    T = 28
    P = 33
    S = 39
    H = 43
    L = 46
    X = 53
    C = 54
    V = 55
    W = 25
    Z = 52
    INSERT = 118
    HOME = 110
    END = 115
    UP = 111
    DOWN = 116
    PAGE_UP = 112
    PAGE_DOWN = 117
    LEFT = 113
    RIGHT = 114
    F2 = 68
    DELETE = 119
    BACK_SPACE = 22
    CTRL_L = 37
    CTRL_R = 105
    # Laptop codes
    HOME_KP = 79
    END_KP = 87
    PAGE_UP_KP = 81
    PAGE_DOWN_KP = 89

    @classmethod
    def value_exist(cls, value):
        return value in (val.value for val in cls.__members__.values())


# Keys for move in lists. KEY_KP_(NAME) for laptop!!!
MOVE_KEYS = (KeyboardKey.UP, KeyboardKey.PAGE_UP, KeyboardKey.DOWN, KeyboardKey.PAGE_DOWN, KeyboardKey.HOME,
             KeyboardKey.END, KeyboardKey.HOME_KP, KeyboardKey.END_KP, KeyboardKey.PAGE_UP_KP, KeyboardKey.PAGE_DOWN_KP)


class ViewTarget(Enum):
    """ Used for set target view """
    BOUQUET = 0
    FAV = 1
    SERVICES = 2


class BqGenType(Enum):
    """  Bouquet generation type """
    SAT = 0
    EACH_SAT = 1
    PACKAGE = 2
    EACH_PACKAGE = 3
    TYPE = 4
    EACH_TYPE = 5


class Column(Enum):
    """ Column nums in the views """
    # main view
    SRV_CAS_FLAGS = 0
    SRV_STANDARD = 1
    SRV_CODED = 2
    SRV_SERVICE = 3
    SRV_LOCKED = 4
    SRV_HIDE = 5
    SRV_PACKAGE = 6
    SRV_TYPE = 7
    SRV_PICON = 8
    SRV_PICON_ID = 9
    SRV_SSID = 10
    SRV_FREQ = 11
    SRV_RATE = 12
    SRV_POL = 13
    SRV_FEC = 14
    SRV_SYSTEM = 15
    SRV_POS = 16
    SRV_DATA_ID = 17
    SRV_FAV_ID = 18
    SRV_TRANSPONDER = 19
    SRV_TOOLTIP = 20
    SRV_BACKGROUND = 21
    # fav view
    FAV_NUM = 0
    FAV_CODED = 1
    FAV_SERVICE = 2
    FAV_LOCKED = 3
    FAV_HIDE = 4
    FAV_TYPE = 5
    FAV_POS = 6
    FAV_ID = 7
    FAV_PICON = 8
    FAV_TOOLTIP = 9
    FAV_BACKGROUND = 10

    def __index__(self):
        """ Overridden to get the index in slices directly """
        return self.value


if __name__ == "__main__":
    pass
