"""Config Qtile."""
import os
import subprocess
from typing import Any, List

from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Group, Key, Match, Screen

TEXT_FONT_SIZE = 14
ICON_FONT_SIZE = 17
MOUSE_MOV_DIFF = 20
ALT = "mod1"
WIN = "mod4"
CONTROL = "control"
SHIFT = "shift"
TERM = "kitty --title=term"
HOME = os.path.expanduser("~")
QTILE_DIR = HOME + "/.config/qtile"
WIN_TAB_SEP = " -|- "
SELECTED_TAB_CSS = ("<b>[", "]</b>")
FONT = "FiraCode Nerd Font Mono"

CUSTOM_KEYMAP = {
    "left": "h",
    "right": "i",
    "up": "e",
    "down": "n",
    "normal": "k",
    "next_screen": "o",
}


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
        CUSTOM_KEYMAP["next_screen"],
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
        CUSTOM_KEYMAP["next_screen"],
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),
    # Window controls
    # Key(
    #     [ALT],
    #     CUSTOM_KEYMAP["left"],
    #     lazy.function(next_win),
    #     desc="Move focus left in current stack pane",
    # ),
    # Key(
    #     [ALT],
    #     CUSTOM_KEYMAP["right"],
    #     lazy.layout.right(),
    #     desc="Move focus right in current stack pane",
    # ),
    Key(
        [ALT],
        CUSTOM_KEYMAP["up"],
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key(
        [ALT],
        CUSTOM_KEYMAP["down"],
        lazy.layout.up(),
        desc="Move focus up in current stack pane",
    ),
    Key(
        [ALT, SHIFT],
        CUSTOM_KEYMAP["left"],
        lazy.layout.swap_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [ALT, SHIFT],
        CUSTOM_KEYMAP["left"],
        lazy.layout.swap_right(),
        lazy.layout.left(),
        desc="Move windows right in current stack",
    ),
    Key(
        [ALT, SHIFT],
        CUSTOM_KEYMAP["down"],
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [ALT, SHIFT],
        CUSTOM_KEYMAP["up"],
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
        CUSTOM_KEYMAP["normal"],
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
            # lazy.group[name].toscreen()
        )
    )

layout_theme = {
    "border_width": 0,
    "margin": 0,
    "border_focus": "white",
    "border_normal": "1D2330",
    "max_ratio": 0.75,
    "min_ratio": 0.25,
}

layouts = [
    # layout.Tile(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

colors = [
    ["#292d3e", "#292d3e"],
    ["#434758", "#434758"],
    ["#feeeee", "#feeeee"],
    ["#ff5555", "#ff5555"],
    ["#8d62a9", "#8d62a9"],
    ["#668bd7", "#668bd7"],
    ["#1b2c35", "#1b2c35"],
    ["#e1acff", "#e1acff"],
]

# DEFAULT WIDGET SETTINGS #####
widget_defaults = {
    "font": "FiraCode Nerd Font Mono 12",
    "fontsize": TEXT_FONT_SIZE,
    "padding": 5,
    "background": colors[6],
    "foreground": colors[2],
    "margin_y": 3,
}

extension_defaults = widget_defaults.copy()


def shorten_window_name(win_name_str):
    raw_win_names = win_name_str.split(WIN_TAB_SEP)
    win_names = []
    win_name_sep = "-"
    alter_win_name_sep = "|"
    win_name_str = ""

    for win_name in raw_win_names:
        print(win_name)
        win_name = win_name.split(win_name_sep)[-1]
        win_name = win_name.split(alter_win_name_sep)[-1].lower().strip()

        if SELECTED_TAB_CSS[1] in win_name:
            win_name = SELECTED_TAB_CSS[0] + win_name

        win_names.append(win_name)
    return WIN_TAB_SEP.join(win_names)


def init_widgets_list():
    """Status bar config."""
    left_widgets = [
        widget.TextBox(
            fmt=" ",
            fontsize=ICON_FONT_SIZE,
            background=colors[0],
            foreground=colors[0],
            padding=0,
        ),
        widget.CurrentScreen(
            fontsize=ICON_FONT_SIZE,
            active_text="❇",
            active_color=colors[3],
            inactive_text="❇",
            inactive_color=colors[1],
            padding=1,
            background=colors[0],
        ),
        widget.Sep(
            padding=5,
            background=colors[0],
            foreground=colors[0],
        ),
        widget.GroupBox(
            background=colors[0],
            margin_x=5,
            padding_y=2,
            padding_x=7,
            borderwidth=2,
            active=colors[2],
            inactive=colors[3],
            rounded=True,
            hide_unused=True,
            highlight_color=colors[1],
            highlight_method="block",
            block_highlight_text_color=colors[5],
            mouse_callbacks={"Button1": lambda: None},
            font=FONT,
        ),
        widget.TextBox(
            fmt="",
            fontsize=ICON_FONT_SIZE,
            padding=0,
            foreground=colors[0],
            background=colors[1],
        ),
        widget.Sep(
            padding=100,
            background=colors[1],
            foreground=colors[1],
        ),
    ]

    mid_widgets = [
        widget.TextBox(
            fmt="",
            fontsize=ICON_FONT_SIZE,
            padding=0,
            background=colors[1],
            foreground=colors[0],
        ),
        widget.WindowTabs(
            background=colors[0],
            fmt="{}",
            font=FONT,
            padding=30,
            max_chars=0,
            mouse_callbacks={"Button1": lambda: None},
            parse_text=shorten_window_name,
            selected=SELECTED_TAB_CSS,
            separator=WIN_TAB_SEP,
        ),
        widget.TextBox(
            fmt="",
            fontsize=ICON_FONT_SIZE,
            padding=0,
            foreground=colors[0],
            background=colors[1],
        ),
        widget.Sep(
            padding=100,
            background=colors[1],
            foreground=colors[1],
        ),
    ]

    right_widgets = [
        widget.TextBox(
            fmt="",
            fontsize=ICON_FONT_SIZE,
            padding=0,
            background=colors[1],
            foreground=colors[0],
        ),
        widget.Battery(
            fontsize=TEXT_FONT_SIZE,
            discharge_char="  ",
            charge_char="  ",
            full_char="  ",
            unknown_char="  ",
            update_interval=5,
            format="{char}{percent:2.0%}",
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Net(
            fontsize=TEXT_FONT_SIZE,
            format="{down}",
            foreground=colors[2],
            background=colors[0],
            use_bits=False,
            update_interval=21,
        ),
        widget.Volume(
            fmt="󰂚 {}",
            channel="Master",
            foreground=colors[2],
            background=colors[0],
            mouse_callbacks={"Button1": lambda: None},
            update_interval=0.5,
            padding=10,
        ),
        widget.Clock(
            fontsize=TEXT_FONT_SIZE,
            update_interval=61,
            format="%a %m-%d %H:%M",
            foreground=colors[2],
            background=colors[0],
            padding=10,
        ),
        widget.KeyboardLayout(
            fontsize=23,
            configured_keyboards=[
                "us colemak",
                "us intl",
            ],
            display_map={
                "us colemak": "󰢚",
                "us intl": "󰙃",
            },
            mouse_callbacks={"Button1": lambda: None},
        ),
    ]

    # remove battery widget if there is no battery
    check_batt_cmd = os.popen("ls /sys/class/power_supply")
    check_batt_output = check_batt_cmd.read()

    if len(check_batt_output) == 0:
        right_widgets[2] = (
            widget.Sep(
                padding=10,
                background=colors[1],
                foreground=colors[1],
            ),
        )

    return left_widgets + mid_widgets + right_widgets


def init_widgets_screen1():
    """Status bar for screen #1."""
    widgets = init_widgets_list()
    return widgets


def init_widgets_screen2():
    """Status bar for screen #2."""
    widgets = init_widgets_list()
    return widgets


def init_screens():
    """Apply status bars."""
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=22),
        ),
        Screen(
            top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=22),
        ),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse: List[Any] = []

dgroups_key_binder = None
dgroups_app_rules: List[Any] = []
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="xmessage"),
        Match(wm_class="Pavucontrol"),
        Match(wm_class="Blueman-manager"),
        Match(wm_class="Arandr"),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    """Bootstrap qtile."""
    subprocess.call(["/usr/bin/ibus-daemon", "-d"])
    subprocess.call(["/usr/bin/xfce4-power-manager", "--daemon"])
    subprocess.call(["/usr/bin/xmodmap", HOME + "/.config/xmodmap/colemak"])


wmname = "LG3D"
