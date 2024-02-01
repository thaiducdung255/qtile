from os import path
from libqtile.command import lazy
from libqtile.config import Key, Group

TERM = "kitty --title=term"
ALT = "mod1"
HOME = path.expanduser("~")
QTILE_DIR = HOME + "/.config/qtile"
CONTROL = "control"
WIN = "mod4"
SHIFT = "shift"
MOUSE_MOV_DIFF = 20


def next_win(qtile):
    lazy.cmd_spawn('notify-send "hola"')


group_keys = {
    "1": "n",
    "2": "e",
    "3": "i",
    "4": "o",
    "5": "l",
    "6": "u",
    "7": "y",
    "8": "semicolon",
}

group_names = [
    ("Nergal", {"layout": "max"}),
    ("Emma-O", {"layout": "max"}),
    ("Ishtar", {"layout": "max"}),
    ("O-Yama", {"layout": "max"}),
    ("Loki", {"layout": "max"}),
    ("Ukobach", {"layout": "max"}),
    ("Yaotzin", {"layout": "max"}),
    ("Purah", {"layout": "max"}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

keys = [
    # The essentials
    Key([ALT], "Return", lazy.spawn(TERM), desc="Launch default terminal"),
    Key(
        [ALT],
        "Escape",
        lazy.spawn(HOME + "/.config/rofi/scripts/menu.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [CONTROL],
        "Escape",
        lazy.spawn(HOME + "/.config/rofi/scripts/cmd.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [ALT],
        "Tab",
        lazy.spawn(HOME + "/.config/rofi/scripts/index.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [ALT],
        "b",
        lazy.spawn("qutebrowser"),
        desc="Start web browser",
    ),
    Key(
        [ALT],
        "f",
        lazy.next_layout(),
        desc="Toggle through layouts",
    ),
    Key(
        [ALT, SHIFT],
        "o",
        lazy.window.kill(),
        desc="Kill active window",
    ),
    Key(
        [ALT],
        "q",
        lazy.window.kill(),
        desc="Kill active window",
    ),
    Key(
        [ALT, SHIFT],
        "r",
        lazy.restart(),
        desc="Restart Qtile",
    ),
    Key(
        [ALT, SHIFT],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    # Switch focus of monitors
    Key(
        [ALT],
        "o",
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),
    # Window controls
    Key(
        [ALT],
        "h",
        lazy.function(next_win),
        desc="Move focus left in current stack pane",
    ),
    # Key(
    #     [ALT],
    #     CUSTOM_KEYMAP["right"],
    #     lazy.layout.right(),
    #     desc="Move focus right in current stack pane",
    # ),
    Key(
        [ALT],
        "e",
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key(
        [ALT],
        "n",
        lazy.layout.up(),
        desc="Move focus up in current stack pane",
    ),
    Key(
        [ALT, SHIFT],
        "h",
        lazy.layout.swap_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [ALT, SHIFT],
        "i",
        lazy.layout.swap_right(),
        desc="Move windows right in current stack",
    ),
    Key(
        [ALT, SHIFT],
        "n",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [ALT, SHIFT],
        "e",
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [ALT, SHIFT],
        "period",
        lazy.layout.increase_nmaster(),
        desc="increase number in master pane (Tile)",
    ),
    Key(
        [ALT, SHIFT],
        "comma",
        lazy.layout.decrease_nmaster(),
        desc="decrease number in master pane (Tile)",
    ),
    Key(
        [ALT],
        "period",
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        desc="increase number in master pane (Tile)",
    ),
    Key(
        [ALT],
        "comma",
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        desc="decrease number in master pane (Tile)",
    ),
    Key(
        [ALT],
        "k",
        lazy.layout.normalize(),
        desc="normalize window size ratios",
    ),
    Key(
        [ALT],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key(
        [WIN, CONTROL],
        "m",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen",
    ),
    # Group controls
    Key(
        [WIN],
        "m",
        lazy.screen.next_group(),
        desc="navigate to next group",
    ),
    Key(
        [WIN],
        "k",
        lazy.screen.prev_group(),
        desc="navigate to previous group",
    ),
    # Stack controls
    Key(
        [ALT, SHIFT],
        "space",
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [ALT, CONTROL],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Volume control
    Key(
        [WIN],
        "c",
        lazy.spawn(QTILE_DIR + "/.init-scripts/volume-mute-toggle.sh"),
        desc="Toggle mute/unmute",
    ),
    Key(
        [WIN],
        "z",
        lazy.spawn("amixer set Master 3%-"),
        lazy.spawn("pactl set-sink-volume 0 -3%"),
        desc="Decrease volume",
    ),
    Key(
        [WIN],
        "x",
        lazy.spawn("amixer set Master 3%+"),
        lazy.spawn("pactl set-sink-volume 0 +3%"),
        desc="Increase volume",
    ),
    Key(
        [WIN, SHIFT],
        "3",
        lazy.spawn("sh " + QTILE_DIR + "/.init-scripts/toggle-touchpad.sh 0"),
        desc="disable touchpad",
    ),
    Key(
        [WIN],
        "3",
        lazy.spawn("sh " + QTILE_DIR + "/.init-scripts/toggle-touchpad.sh 1"),
        desc="enable touchpad",
    ),
    # Brightness control
    # monitor #1
    Key(
        [WIN],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh inc 0"),
        desc="Increase brightness",
    ),
    Key(
        [WIN, SHIFT],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh des 0"),
        desc="Decrease brightness",
    ),
    Key(
        [WIN, CONTROL],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh dim 0"),
        desc="Dim screen",
    ),
    # monitor #2
    Key(
        [WIN],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh inc 1"),
        desc="Increase brightness",
    ),
    Key(
        [WIN, SHIFT],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh des 1"),
        desc="Decrease brightness",
    ),
    Key(
        [WIN, CONTROL],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh dim 1"),
        desc="Dim screen",
    ),
    # Power control
    Key(
        [WIN],
        "q",
        lazy.spawn("dm-tool lock"),
        desc="Lock screen",
    ),
    Key(
        [WIN],
        "Escape",
        lazy.spawn("/usr/bin/zsh " + QTILE_DIR + "/.init-scripts/power-v2.sh"),
        desc="Power management",
    ),
    # Mouse control
    Key(
        [ALT],
        "semicolon",
        lazy.spawn("xdotool click 1"),
        desc="Move left click",
    ),
    Key(
        [ALT, CONTROL],
        "semicolon",
        lazy.spawn("xdotool click 3"),
        desc="Move right click",
    ),
    Key(
        [ALT],
        "j",
        lazy.spawn(f"xdotool mousemove_relative -- -{MOUSE_MOV_DIFF} 0"),
        desc="Move mouse left",
    ),
    Key(
        [ALT],
        "l",
        lazy.spawn(f"xdotool mousemove_relative 0 {MOUSE_MOV_DIFF}"),
        desc="Move mouse up",
    ),
    Key(
        [ALT],
        "u",
        lazy.spawn(f"xdotool mousemove_relative 0 -{MOUSE_MOV_DIFF}"),
        desc="Move mouse down",
    ),
    Key(
        [ALT],
        "y",
        lazy.spawn(f"xdotool mousemove_relative {MOUSE_MOV_DIFF} 0"),
        desc="Move mouse right",
    ),
    # Keyboard layout control
    Key(
        [WIN],
        "a",
        lazy.spawn(QTILE_DIR + "/.init-scripts/keyboard-layout"),
        desc="Switch keyboard layout",
    ),
]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key(
            [WIN],
            group_keys[str(i)],
            lazy.group[name].toscreen(),
        )
    )

    keys.append(
        Key(
            [WIN, CONTROL],
            group_keys[str(i)],
            lazy.window.togroup(name),
            lazy.restart(),
        )
    )
