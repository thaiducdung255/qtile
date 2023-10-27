from libqtile import widget, bar
from os import popen
from libqtile.config import Screen

FONT = "FiraCode Nerd Font Mono"
TEXT_FONT_SIZE = 14
ICON_FONT_SIZE = 17

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
    win_name_sep = "-"
    alter_win_name_sep = "|"
    raw_win_names = [win_name_str]
    win_names = []
    win_name_str = ""

    for win_name in raw_win_names:
        win_name = win_name.split(win_name_sep)[-1]
        win_name = win_name.split(alter_win_name_sep)[-1].lower().strip()

        win_names.append(win_name)
    return "".join(win_names)


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
        widget.TaskList(
            background=colors[0],
            fontsize=TEXT_FONT_SIZE,
            icon_size=0,
            font=FONT,
            margin_y=1,
            padding_y=1,
            mouse_callbacks={"Button1": lambda: None},
            parse_text=shorten_window_name,
            highlight_method="block",
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
            discharge_char="-",
            charge_char="+",
            full_char="*",
            unknown_char="!",
            update_interval=5,
            format="{percent:2.0%}{char}",
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Net(
            fontsize=TEXT_FONT_SIZE,
            format="{down:6.2f}{down_suffix:<2}",
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
    check_batt_cmd = popen("ls /sys/class/power_supply")
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
