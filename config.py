"""Config Qtile."""
import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Group, Key, Match, Screen

MOD = "mod1"
MOD4 = "mod4"
CONTROL = "control"
TERM = "kitty"
home = os.path.expanduser("~")
QTILE_DIR = home + "/.config/qtile"
KEYBOARD_LAYOUT = "colemak"

customKeymap = {
    "left": "h",
    "right": "l",
    "up": "k",
    "down": "j",
    "normal": "n",
    "next_screen": "semicolon",
}

if KEYBOARD_LAYOUT == "colemak":
    customKeymap = {
        "left": "h",
        "right": "i",
        "up": "e",
        "down": "n",
        "normal": "k",
        "next_screen": "o",
    }

keys = [
    # The essentials
    Key([MOD], "Return", lazy.spawn(TERM), desc="Launches My Terminal"),
    Key(
        [MOD],
        "Escape",
        lazy.spawn(home + "/.config/rofi/scripts/menu.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [CONTROL],
        "Escape",
        lazy.spawn(home + "/.config/rofi/scripts/cmd.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [MOD],
        "Tab",
        lazy.spawn(home + "/.config/rofi/scripts/index.sh"),
        desc="Rofi show running applications",
    ),
    Key(
        [MOD],
        "c",
        lazy.spawn("google-chrome-stable"),
        desc="Start web browser",
    ),
    Key(
        [MOD],
        "b",
        lazy.spawn("brave"),
        desc="Start web browser",
    ),
    Key(
        [MOD],
        "t",
        lazy.spawn("neovide"),
        desc="Start web browser",
    ),
    Key(
        [MOD],
        "space",
        lazy.next_layout(),
        desc="Toggle through layouts",
    ),
    Key(
        [MOD, "shift"],
        customKeymap["next_screen"],
        lazy.window.kill(),
        desc="Kill active window",
    ),
    Key(
        [MOD, "shift"],
        "r",
        lazy.restart(),
        desc="Restart Qtile",
    ),
    Key(
        [MOD, "shift"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    # Switch focus of monitors
    Key(
        [MOD],
        customKeymap["next_screen"],
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),
    # Window controls
    Key(
        [MOD],
        customKeymap["left"],
        lazy.layout.left(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [MOD],
        customKeymap["right"],
        lazy.layout.right(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [MOD],
        customKeymap["down"],
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key(
        [MOD],
        customKeymap["up"],
        lazy.layout.up(),
        desc="Move focus up in current stack pane",
    ),
    Key(
        [MOD, "shift"],
        customKeymap["left"],
        lazy.layout.swap_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [MOD, "shift"],
        customKeymap["left"],
        lazy.layout.swap_right(),
        lazy.layout.left(),
        desc="Move windows right in current stack",
    ),
    Key(
        [MOD, "shift"],
        customKeymap["down"],
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [MOD, "shift"],
        customKeymap["up"],
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [MOD, "shift"],
        "period",
        lazy.layout.increase_nmaster(),
        desc="increase number in master pane (Tile)",
    ),
    Key(
        [MOD, "shift"],
        "comma",
        lazy.layout.decrease_nmaster(),
        desc="decrease number in master pane (Tile)",
    ),
    Key(
        [MOD],
        "period",
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        desc="increase number in master pane (Tile)",
    ),
    Key(
        [MOD],
        "comma",
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        desc="decrease number in master pane (Tile)",
    ),
    Key(
        [MOD],
        customKeymap["normal"],
        lazy.layout.normalize(),
        desc="normalize window size ratios",
    ),
    Key(
        [MOD],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key(
        [MOD4],
        "m",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen",
    ),
    # Stack controls
    Key(
        [MOD, "shift"],
        "space",
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [MOD, "control"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Volume control
    Key(
        [MOD4],
        "c",
        lazy.spawn(QTILE_DIR + "/.init-scripts/volume-mute-toggle.sh"),
        desc="Toggle mute/unmute",
    ),
    Key(
        [MOD4],
        "z",
        lazy.spawn("amixer set Master 3%-"),
        lazy.spawn("pactl set-sink-volume 0 -3%"),
        desc="Decrease volume",
    ),
    Key(
        [MOD4],
        "x",
        lazy.spawn("amixer set Master 3%+"),
        lazy.spawn("pactl set-sink-volume 0 +3%"),
        desc="Increase volume",
    ),
    Key(
        [MOD4, "shift"],
        "3",
        lazy.spawn("sh " + QTILE_DIR + "/.init-scripts/toggle-touchpad.sh 0"),
        desc="disable touchpad",
    ),
    Key(
        [MOD4],
        "3",
        lazy.spawn("sh " + QTILE_DIR + "/.init-scripts/toggle-touchpad.sh 1"),
        desc="enable touchpad",
    ),
    # Brightness control
    # monitor #1
    Key(
        [MOD4],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh inc 0"),
        desc="Increase brightness",
    ),
    Key(
        [MOD4, "shift"],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh des 0"),
        desc="Decrease brightness",
    ),
    Key(
        [MOD4, "control"],
        "1",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh dim 0"),
        desc="Dim screen",
    ),
    # monitor #2
    Key(
        [MOD4],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh inc 1"),
        desc="Increase brightness",
    ),
    Key(
        [MOD4, "shift"],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh des 1"),
        desc="Decrease brightness",
    ),
    Key(
        [MOD4, "control"],
        "2",
        lazy.spawn(QTILE_DIR + "/.init-scripts/brightness.sh dim 1"),
        desc="Dim screen",
    ),
    # Power control
    Key(
        [MOD],
        "l",
        lazy.spawn("dm-tool lock"),
        desc="Lock screen",
    ),
    Key(
        [MOD4],
        "Escape",
        lazy.spawn("/usr/bin/zsh " + QTILE_DIR + "/.init-scripts/power-v2.sh"),
        desc="Power management",
    ),
]

group_names = [
    ("Javan", {"layout": "monadtall"}),
    ("Kemuel", {"layout": "monadtall"}),
    ("Laila", {"layout": "monadtall"}),
    ("Seraphina", {"layout": "monadtall"}),
    ("Uriel", {"layout": "monadtall"}),
    ("Ieshim", {"layout": "monadtall"}),
    ("Orifiel", {"layout": "monadtall"}),
    ("Parisa", {"layout": "monadtall"}),
]

group_keys = {
    "1": "j",
    "2": "k",
    "3": "l",
    "4": "semicolon",
    "5": "u",
    "6": "i",
    "7": "o",
    "8": "p",
}

if KEYBOARD_LAYOUT == "colemak":
    group_keys = {
        "1": "a",
        "2": "r",
        "3": "s",
        "4": "t",
        "5": "q",
        "6": "w",
        "7": "f",
        "8": "p",
    }

    group_names = [
        ("Azazel", {"layout": "monadtall"}),
        ("Rahab", {"layout": "monadtall"}),
        ("Samkiel", {"layout": "monadtall"}),
        ("Tagas", {"layout": "monadtall"}),
        ("Qaspiel", {"layout": "monadtall"}),
        ("Wormwood", {"layout": "monadtall"}),
        ("Furfur", {"layout": "monadtall"}),
        ("Purah", {"layout": "monadtall"}),
    ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key(
            [MOD4],
            group_keys[str(i)],
            lazy.group[name].toscreen(),
        )
    )

    keys.append(
        Key(
            [MOD4, "control"],
            group_keys[str(i)],
            lazy.window.togroup(name),
            # lazy.group[name].toscreen()
        )
    )

layout_theme = {
    "border_width": 1,
    "margin": 1,
    "border_focus": "green",
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
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize=16,
    padding=5,
    background=colors[6],
    foreground=colors[2],
    margin_y=3,
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    """Status bar config."""
    widgets_list = [
        # 1
        widget.TextBox(
            fmt="",
            fontsize=23,
            background=colors[0],
            foreground=colors[0],
            padding=0,
        ),
        # 2
        widget.CurrentScreen(
            active_text="❇",
            active_color=colors[3],
            inactive_text="❇",
            inactive_color=colors[1],
            padding=1,
            background=colors[0],
            fontsize=24,
        ),
        # 3
        widget.Sep(padding=5, background=colors[0], foreground=colors[0]),
        # 4
        widget.GroupBox(
            background=colors[0],
            margin_x=5,
            padding_y=2,
            padding_x=7,
            borderwidth=2,
            disable_drag=True,
            active=colors[2],
            inactive=colors[3],
            rounded=True,
            hide_unused=True,
            highlight_color=colors[1],
            highlight_method="border",
            this_current_screen_border=colors[2],
            this_screen_border=colors[4],
            other_current_screen_border=colors[1],
            other_screen_border=colors[1],
        ),
        # 5
        widget.TextBox(
            fmt="",
            fontsize=23,
            padding=0,
            foreground=colors[0],
            background=colors[1],
        ),
        # 6
        widget.Spacer(length=bar.STRETCH, background=colors[1]),
        # 7
        widget.TextBox(
            fmt="",
            fontsize=23,
            padding=0,
            background=colors[1],
            foreground=colors[0],
        ),
        # 8
        widget.Net(
            format="{down} ↕{up}  ",
            padding=10,
            foreground=colors[2],
            background=colors[0],
            use_bits=False,
            update_interval=5,
        ),
        # 9
        widget.Battery(
            discharge_char=" ",
            charge_char=" ",
            full_char=" ",
            unknown_char=" ",
            update_interval=5,
            format="{char}{percent:2.0%} ",
            foreground=colors[2],
            background=colors[0],
            padding=10,
        ),
        # 10
        widget.TextBox(
            fmt="",
            fontsize=23,
            foreground=colors[2],
            background=colors[0],
            padding=0,
        ),
        # 11
        widget.Volume(
            channel="Master",
            foreground=colors[2],
            background=colors[0],
            padding=10,
        ),
        # 12
        widget.TextBox(
            fmt=" ☀",
            fontsize=20,
            foreground=colors[2],
            background=colors[0],
            padding=0,
        ),
        # 13
        widget.Clock(
            update_interval=60,
            format="%a, %H:%M (%d/%m)",
            foreground=colors[2],
            background=colors[0],
            padding=5,
        ),
    ]

    # remove battery widget if there is no battery
    check_batt_cmd = os.popen("ls /sys/class/power_supply")
    check_batt_output = check_batt_cmd.read()

    if len(check_batt_output) == 0:
        widgets_list.pop(8)

    return widgets_list


def init_widgets_screen1():
    """Status bar for screen #1."""
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    """Status bar for screen #2."""
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


def init_screens():
    """Apply status bars."""
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=28),
        ),
        Screen(
            top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=28),
        ),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    """Switch window to prev group."""
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    """Switch window to next group."""
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    """Switch window to prev screen."""
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    """Switch window to next screen."""
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    """Switch screen configs."""
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = []

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="xmessage"),
        Match(wm_class="Pavucontrol"),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    """Bootstrap qtile."""
    subprocess.call([QTILE_DIR + "/autostart.sh"])


wmname = "LG3D"
