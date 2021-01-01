import os
import re
import socket
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, extension
from libqtile.lazy import lazy
from typing import List

mod = "mod1"
super_mod = "mod4"
myTerm = "termite"
home = os.path.expanduser('~')
qtile_dir = home + "/.config/qtile"
myConfig = home + "/.config/qtile/config.py"

keys = [
    ### The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key([mod], "Escape",
        lazy.spawn("rofi -show drun -display-drun \"Apps\" -display-run \"Cmd\" -display-window \"Windows\""),
        desc='Rofi show running applications'
        ),
    Key([mod], "Tab",
        lazy.spawn("rofi -show window -display-drun \"Apps\" -display-run \"Cmd\" -display-window \"Windows\""),
        desc='Rofi show running applications'
        ),
    Key([mod], "b",
        lazy.spawn("brave"),
        desc='Start web browser'
        ),
    Key([mod], "space",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod, "shift"], "semicolon",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key([super_mod], "r",
        lazy.spawn("xmodmap " + qtile_dir + "/.init-scripts/xmodmap"),
        desc='restore xmodmap'
        ),

    ### Switch focus of monitors
    Key([mod], "semicolon",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),

    ### Window controls
    Key([mod], "h",
        lazy.layout.left(),
        desc='Move focus left in current stack pane'
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc='Move focus right in current stack pane'
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "h",
        lazy.layout.swap_left(),
        desc='Move windows left in current stack'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.swap_right(),
        lazy.layout.left(),
        desc='Move windows right in current stack'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "period",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "comma",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([super_mod], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    Key([mod], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),

    ### Stack controls
    Key([mod, "shift"], "space",
        lazy.layout.rotte(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),

    ### Volume control
    Key([], "F1",
        lazy.spawn(qtile_dir + "/.init-scripts/volume-mute-toggle.sh"),
        desc='Toggle mute/unmute'
        ),
    Key([], "F2",
        lazy.spawn("amixer set Master 5%-"),
        desc='Decrease volume'
        ),
    Key([], "F3",
        lazy.spawn("amixer -q set Master 5%+"),
        desc='Increase volume'
        ),

    ### Brightness control
    ## monitor #1
    Key([super_mod], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh inc 0"),
        desc='Increase brightness'
        ),
    Key([super_mod, "shift"], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh des 0"),
        desc='Decrease brightness'
        ),
    Key([super_mod, "control"], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh dim 0"),
        desc='Dim screen'
        ),

    ## monitor #2
    Key([super_mod], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh inc 1"),
        desc='Increase brightness'
        ),
    Key([super_mod, "shift"], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh des 1"),
        desc='Decrease brightness'
        ),
    Key([super_mod, "control"], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh dim 1"),
        desc='Dim screen'
        ),

    ### Power control
    Key([super_mod], "x",
        lazy.spawn("xscreensaver-command -l"),
        desc='Lock screen'
        ),
    Key([super_mod], "Escape",
        lazy.spawn(qtile_dir + "/.init-scripts/power.sh"),
        desc='Power management'
        ),
]

group_names = [
    ("J", {'layout': 'monadtall'}),
    ("K", {'layout': 'monadtall'}),
    ("L", {'layout': 'monadtall'}),
    ("S", {'layout': 'monadtall'}),
    ("U", {'layout': 'monadtall'}),
    ("I", {'layout': 'monadtall'}),
    ("O", {'layout': 'monadtall'}),
    ("P", {'layout': 'monadtall'})]

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

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([super_mod], group_keys[str(i)], lazy.group[name].toscreen()))
    keys.append(Key([super_mod, "shift"], group_keys[str(i)], lazy.window.togroup(name)))

layout_theme = {
    "border_width": 1,
    "margin": 0,
    "border_focus": "green",
    "border_normal": "1D2330",
    "max_ratio": 0.75,
    "min_ratio": 0.25,
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

colors = [
    ["#292d3e", "#292d3e"], # panel background
    ["#434758", "#434758"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font color for group names
    ["#ff5555", "#ff5555"], # border line color for current tab
    ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
    ["#668bd7", "#668bd7"], # color for the even widgets
    ["#1b2c35", "#1b2c35"], # color for the even widgets
    ["#e1acff", "#e1acff"]] # window name

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 16,
    padding = 5,
    background=colors[6],
    foreground = colors[2],
    margin_y = 3,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth = 0, padding = 3),
        widget.CurrentScreen(
            active_text = "◉",
            active_color = colors[3],
            inactive_text = "◉",
            inactive_color = colors[1],
            padding = 2,
            ),

        widget.CurrentLayoutIcon(scale = 0.57, padding = 2),

        widget.GroupBox(
            margin_x = 2,
            padding_y = 2,
            padding_x = 3,
            borderwidth = 1,
            disable_drag = True,
            active = colors[5],
            inactive = colors[2],
            rounded = True,
            hide_unused = True,
            highlight_color = colors[1],
            highlight_method = "border",
            this_current_screen_border = colors[2],
            this_screen_border = colors[4],
            other_current_screen_border = colors[1],
            other_screen_border = colors[1],
            ),

        widget.Sep(linewidth = 0, padding = 20),
        widget.WindowTabs(),
        widget.Sep(linewidth = 0, padding = 20),
        widget.Notify(audiofile = qtile_dir + "/.sounds/notify-sound.mp3"),
        widget.Sep(linewidth = 0, padding = 20),

        widget.Spacer(length = bar.STRETCH),
        widget.Battery(
            discharge_char = "-",
            charge_char = "+",
            unknown_char = "*",
            update_interval = 300,
            # format = "{char}{percent:2.0%} ({hour:d}:{min:02d})",
            format = "{char}{percent:2.0%}",
            ),
        widget.Sep(linewidth = 0),

        widget.Wlan(
            interface = "wlp0s20f3",
            disconnected_message = "W: N/A",
            format = "{essid}",
            ),
        widget.Sep(linewidth = 0),

        widget.Volume(),
        widget.Sep(linewidth = 0),

        widget.Clock(format = "%a, %H:%M (%d/%m)", update_interval = 60),
        widget.Sep(linewidth = 0),
        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=28)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=28))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = []

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'ssh-askpass'},
    {'wname': 'branchdialog'},
    {'wname': 'pinentry'},
    {'wname': 'xmessage'},
])

auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    subprocess.call([qtile_dir + '/autostart.sh'])

wmname = "LG3D"
