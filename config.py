import os
import subprocess
from libqtile.config import Key, Screen, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy

mod = "mod1"
secondary_mod = "mod4"
extra_mod = "mod5"
myTerm = "kitty"
home = os.path.expanduser('~')
qtile_dir = home + "/.config/qtile"
myConfig = home + "/.config/qtile/config.py"
keyboardLayout = "colemak"

customKeymap = {
    "left": "h",
    "right": "l",
    "up": "k",
    "down": "j",
    "normal": "n"
}

if keyboardLayout == 'colemak':
    customKeymap = {
        "left": "h",
        "right": "i",
        "up": "e",
        "down": "n",
        "normal": "k"
    }

keys = [
    ### The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
    ),

    Key([mod], "Escape",
        lazy.spawn(home + "/.config/rofi/scripts/menu.sh"),
        desc='Rofi show running applications'
    ),

    Key([mod], "Tab",
        lazy.spawn(home + "/.config/rofi/scripts/index.sh"),
        desc='Rofi show running applications'
    ),

    Key([mod], "c",
        lazy.spawn("google-chrome-stable"),
        desc='Start web browser'
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

    Key([secondary_mod], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),

    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),

    Key([secondary_mod, "shift"], "r",
        lazy.spawn("xmodmap " + qtile_dir + "/.init-scripts/xmodmap"),
        desc='restore xmodmap'
    ),


    ### Switch focus of monitors
    Key([mod], "semicolon",
        lazy.next_screen(),
        desc='Move focus to next monitor'
    ),


    ### Window controls
    Key([mod], customKeymap["left"],
        lazy.layout.left(),
        desc='Move focus left in current stack pane'
    ),

    Key([mod], customKeymap["right"],
        lazy.layout.right(),
        desc='Move focus right in current stack pane'
    ),

    Key([mod], customKeymap["down"],
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),

    Key([mod], customKeymap["up"],
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),

    Key([mod, "shift"], customKeymap["left"],
        lazy.layout.swap_left(),
        desc='Move windows left in current stack'
    ),

    Key([mod, "shift"], customKeymap["left"],
        lazy.layout.swap_right(),
        lazy.layout.left(),
        desc='Move windows right in current stack'
    ),

    Key([mod, "shift"], customKeymap["down"],
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),

    Key([mod, "shift"], customKeymap["up"],
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),

    Key([mod, "shift"], "period",
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),

    Key([mod, "shift"], "comma",
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),

    Key([mod], "period",
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),

    Key([mod], "comma",
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),

    Key([mod], customKeymap["normal"],
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),

    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),

    Key([secondary_mod], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
    ),

    ### Stack controls
    Key([mod, "shift"], "space",
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),

    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),

    ### Volume control
    Key([], "F3",
        lazy.spawn(qtile_dir + "/.init-scripts/volume-mute-toggle.sh"),
        desc='Toggle mute/unmute'
    ),

    Key([], "F1",
        lazy.spawn("amixer set Master 5%-"),
        lazy.spawn("pactl set-sink-volume 0 -5%"),
        desc='Decrease volume'
    ),

    Key([], "F2",
        lazy.spawn("amixer set Master 5%+"),
        lazy.spawn("pactl set-sink-volume 0 +5%"),
        desc='Increase volume'
    ),

    Key([secondary_mod, "shift"], "3",
        lazy.spawn("sh " + qtile_dir + "/.init-scripts/toggle-touchpad.sh 0"),
        desc='disable touchpad'
    ),

    Key([secondary_mod], "3",
        lazy.spawn("sh " + qtile_dir + "/.init-scripts/toggle-touchpad.sh 1"),
        desc='enable touchpad'
    ),


    ### Brightness control
    ## monitor #1
    Key([secondary_mod], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh inc 0"),
        desc='Increase brightness'
    ),

    Key([secondary_mod, "shift"], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh des 0"),
        desc='Decrease brightness'
    ),

    Key([secondary_mod, "control"], "1",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh dim 0"),
        desc='Dim screen'
    ),


    ## monitor #2
    Key([secondary_mod], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh inc 1"),
        desc='Increase brightness'
    ),

    Key([secondary_mod, "shift"], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh des 1"),
        desc='Decrease brightness'
    ),

    Key([secondary_mod, "control"], "2",
        lazy.spawn(qtile_dir + "/.init-scripts/brightness.sh dim 1"),
        desc='Dim screen'
    ),


    ### Power control
    Key([secondary_mod], "x",
        lazy.spawn("dm-tool lock"),
        desc='Lock screen'
    ),

    Key([secondary_mod], "Escape",
        lazy.spawn("/usr/bin/zsh " + qtile_dir + "/.init-scripts/power-v2.sh"),
        desc='Power management'
    ),
]

group_names = [
    ("Javan",     {'layout': 'monadtall'}),
    ("Kemuel",    {'layout': 'monadtall'}),
    ("Laila",     {'layout': 'monadtall'}),
    ("Seraphina", {'layout': 'monadtall'}),
    ("Uriel",     {'layout': 'monadtall'}),
    ("Ieshim",    {'layout': 'monadtall'}),
    ("Orifiel",   {'layout': 'monadtall'}),
    ("Parisa",    {'layout': 'monadtall'})]

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

if keyboardLayout == "colemak":
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
        ("Nakir",     {'layout': 'monadtall'}),
        ("Eleleth",   {'layout': 'monadtall'}),
        ("Israfil",   {'layout': 'monadtall'}),
        ("Orifiel",   {'layout': 'monadtall'}),
        ("Laila",     {'layout': 'monadtall'}),
        ("Uriel",     {'layout': 'monadtall'}),
        ("Yomiel",    {'layout': 'monadtall'}),
        ("Seraphina", {'layout': 'monadtall'})
    ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([secondary_mod], group_keys[str(i)], lazy.group[name].toscreen()))
    keys.append(Key([secondary_mod, "shift"], group_keys[str(i)], lazy.window.togroup(name)))

layout_theme = {
    "border_width":     1,
    "margin":           0,
    "border_focus":     "green",
    "border_normal":    "1D2330",
    "max_ratio":        0.75,
    "min_ratio":        0.25,
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
    ["#e1acff", "#e1acff"]
]

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font        = "Ubuntu Mono",
    fontsize    = 16,
    padding     = 5,
    background  = colors[6],
    foreground  = colors[2],
    margin_y    = 3,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        # 1
        widget.TextBox(
            fmt        = '',
            fontsize   = 23,
            background = colors[0],
            foreground = colors[0],
            padding    = 0
        ),

        # 2
        widget.CurrentScreen(
            active_text     = "◉",
            active_color    = colors[3],
            inactive_text   = "◉",
            inactive_color  = colors[1],
            padding         = 1,
            background      = colors[0],
            fontsize        = 20
        ),

        # 3
        widget.Sep(
            padding    = 5,
            background = colors[0],
            foreground = colors[0]
        ),

        # 4
        widget.GroupBox(
            background                  = colors[0],
            margin_x                    = 5,
            padding_y                   = 2,
            padding_x                   = 7,
            borderwidth                 = 2,
            disable_drag                = True,
            active                      = colors[2],
            inactive                    = colors[3],
            rounded                     = True,
            hide_unused                 = True,
            highlight_color             = colors[1],
            highlight_method            = "border",
            this_current_screen_border  = colors[2],
            this_screen_border          = colors[4],
            other_current_screen_border = colors[1],
            other_screen_border         = colors[1],
        ),

        # 5
        widget.TextBox(
            fmt        = '',
            fontsize   = 23,
            padding    = 0,
            foreground = colors[0],
            background = colors[1]
        ),

        # 6
        widget.Spacer(
            length     = bar.STRETCH,
            background = colors[1]
        ),

        # 7
        widget.TextBox(
            fmt        = '',
            fontsize   = 23,
            padding    = 0,
            background = colors[1],
            foreground = colors[0]
        ),

        # 8
        widget.Net(
            format          = '{down} ↓↑{up}  ',
            padding         = 10,
            foreground      = colors[2],
            background      = colors[0],
            use_bits        = False,
            update_interval = 5,
        ),

        # 9
        widget.Battery(
            discharge_char  = " ",
            charge_char     = " ",
            full_char       = " ",
            unknown_char    = " ",
            update_interval = 5,
            format          = "{char}{percent:2.0%} ",
            foreground      = colors[2],
            background      = colors[0],
            padding         = 10,
        ),

        # 10
        widget.TextBox(
            fmt        = '',
            fontsize   = 23,
            foreground = colors[2],
            background = colors[0],
            padding    = 0,
        ),

        # 11
        widget.Volume(
            channel    = 'Master',
            foreground = colors[2],
            background = colors[0],
            padding    = 10
        ),

        # 12
        widget.Clock(
            update_interval = 60,
            format          = "%a, %H:%M (%d/%m)",
            foreground      = colors[2],
            background      = colors[0],
            padding         = 10
        ),
    ]

    # remove battery widget if there is no battery
    checkBattCmd = os.popen('ls /sys/class/power_supply')
    checkBattOutput = checkBattCmd.read()

    if len(checkBattOutput) == 0:
        widgets_list.pop(8)

    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=28)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=28))]

if __name__ in ["config", "__main__"]:
    screens         = init_screens()
    widgets_list    = init_widgets_list()
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

dgroups_key_binder  = None
dgroups_app_rules   = []
main                = None
follow_mouse_focus  = True
bring_front_click   = True
cursor_warp         = True

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='xmessage'),
    Match(wm_class='Pavucontrol'),
])

auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    subprocess.call([qtile_dir + '/autostart.sh'])

wmname = "LG3D"
