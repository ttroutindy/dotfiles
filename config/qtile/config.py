import os
import re
import socket
import subprocess
import owm
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, extension
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
from libqtile.widget import spacer, nvidia_sensors


mod = "mod4"
terminal = guess_terminal("kitty")
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

keys = [
     # Apps
    Key([mod], "w", lazy.spawn("google-chrome-stable"), desc="Launch chrome"),
    #Key([mod], "e", lazy.spawn("emacs"), desc="Launch emacs"),
    #Key([mod], "a", lazy.spawn("pcmanfm"), desc="Launch pcmanfm"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod, "mod1"], "c", lazy.spawn("code"), desc="Launch Visual Studio Code"),
    Key([mod], "s", lazy.spawn("steam"), desc="Launch Steam"),

    # Rofi
    # Key([mod, "shift"], "q", lazy.spawn("rofi -show power-menu -modi power-menu:~/.config/rofi/modules/rofi-power-menu"), desc="Rofi Power Menu"),
    # Key([mod], "s", lazy.spawn("rofi -show drun"), desc="Launch rofi"),

    #KeyChord-emacs
        #  KeyChord([mod],"e", [
        #      Key([], "e",
        #          lazy.spawn("emacsclient -c -a 'emacs'"),
        #          desc='Launch Emacs'
        #          ),
        #      Key([], "d",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
        #          desc='Launch dired inside Emacs'
        #          ),
        #      Key([], "m",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
        #          desc='Launch mu4e inside Emacs'
        #          ),
        #      Key([], "n",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
        #          desc='Launch elfeed inside Emacs'
        #          ),
        #      Key([], "s",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
        #          desc='Launch the eshell inside Emacs'
        #          ),
        #      Key([], "v",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
        #          desc='Launch vterm inside Emacs'),
        #          ]),

    # App control
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(),
    #    desc="Spawn a command using a prompt widget"),

    # Switch between groups
    Key([], 'XF86Back', lazy.screen.prev_group(skip_managed=True, )),
    Key([], 'XF86Forward', lazy.screen.next_group(skip_managed=True, )),
    Key([mod], 'XF86Back', lazy.screen.prev_group(skip_managed=True, )),
    Key([mod], 'XF86Forward', lazy.screen.next_group(skip_managed=True, )),
    Key([mod], 'Left', lazy.screen.prev_group(skip_managed=True, )),
    Key([mod], 'Right', lazy.screen.next_group(skip_managed=True, )),
    Key([mod], 'Escape', lazy.screen.togglegroup()),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod, "control"], "k", lazy.layout.grow(), desc="Grow window"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]

from libqtile.config import Group, Match

groups = [
       Group("1", label="???", layout='monadtall', matches=[Match(wm_class=["signal", "discord", "teams", "ferdi"])]),
       Group("2", label="???", layout='monadtall', matches=[Match(wm_class=["brave"])]),
       Group("3", label="???", layout='monadtall', matches=[Match(wm_class=["kitty", "alacritty", "termite"])]),
       Group("4", label="???", layout='monadtall', matches=[Match(wm_class=["emacs", "code"])]),
       Group("5", label="???", layout='monadtall', matches=[Match(wm_class=["pcmanfm", "calibre", "catfish"])]),
       Group("6", label="???", layout='max', matches=[Match(wm_class=["steam", "lutris", "heroic","virt-manager","virtualbox", "gimp"])]),
       Group("7", label="???", layout='max'),
       Group("8", label="???", layout='monadtall', matches=[Match(wm_class=["deadbeef", "spotify"])]),
       Group("9", label="???", layout='monadwide', matches=[Match(wm_class=["vlc", "mpv"])])
       ]

for i in range(len(groups)):
    keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
    keys.append(
        Key([mod, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=True))
    )

## Monochrome
#colors = [
# ["#000000", "#000000"],  # 0 background
# ["#6b6b6b", "#6b6b6b"],  # 1 foreground
# ["#c4c4c4", "#c4c4c4"],  # 2 background lighter
# ["#b3b3b3", "#b3b3b3"],  # 3 red
# ["#999999", "#999999"],  # 4 green
# ["#717171", "#717171"],  # 5 yellow
# ["#8a8a8a", "#8a8a8a"],  # 6 blue
# ["#b5cabb", "#b5cabb"],  # 7 magenta
# ["#202020", "#202020"],  # 8 cyan
# ["#464646", "#464646"],  # 9 grey
# ["#f8f8f8", "#f8f8f8"],  # 10 white
# ["#eeeeee", "#eeeeee"],  # 11 orange
# ["#7c7c7c", "#7c7c7c"],  # 12 super cyan
# ["#adadad", "#adadad"],  # 13 super blue
# ["#c0c0c0", "#c0c0c0"],  # 14 super dark background
# ["#99ac9e", "#99ac9e"]   # 15 slate grey
#]

# Nord
#colors = [
# ["#2e3440", "#2e3440"],  # 0 background
# ["#f8f8f2", "#f8f8f2"],  # 1 foreground
# ["#3b4252", "#3b4252"],  # 2 background lighter
# ["#bf616a", "#bf616a"],  # 3 red
# ["#a3be8c", "#a3be8c"],  # 4 green
# ["#ebcb8b", "#ebcb8b"],  # 5 yellow
# ["#81a1c1", "#81a1c1"],  # 6 blue
# ["#b48ead", "#b48ead"],  # 7 magenta
# ["#88c0d0", "#88c0d0"],  # 8 cyan
# ["#4c566a", "#4c566a"],  # 9 grey
# ["#e5e9f0", "#e5e9f0"],  # 10 white
# ["#d08770", "#d08770"],  # 11 orange
# ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
# ["#5e81ac", "#5e81ac"],  # 13 super blue
# ["#242831", "#242831"],  # 14 super dark background
# ["#708090", "#708090"]   # 15 slate grey
# ]

# Catpuccin
colors = [
   ["#1a1823", "#1a1823"],  # 0 background
   ["#6e6c7e", "#6e6c7e"],  # 1 foreground
   ["#302d42", "#302d42"],  # 2 background lighter
   ["#f28fad", "#f28fad"],  # 3 red
   ["#abe9b3", "#abe9b3"],  # 4 green
   ["#fae3b0", "#fae3b0"],  # 5 yellow
   ["#96cdfb", "#96cdfb"],  # 6 blue
   ["#e8a2af", "#e8a2af"],  # 7 maroon
   ["#89dceb", "#89dceb"],  # 8 cyan
   ["#c3bac6", "#c3bac6"],  # 9 grey
   ["#d9e0ee", "#d9e0ee"],  # 10 white
   ["#f8bd96", "#f8bd96"],  # 11 orange
   ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
   ["#c9cbff", "#c9cbff"],  # 13 super blue
   ["#131020", "#131020"],  # 14 super dark background
   ["#988ba2", "#988ba2"]   # 15 slate grey
]

layout_theme = {"border_width": 2,
                "margin": 10,
                "border_focus": colors[9],
                "border_normal": colors[0]
                }

layouts = [
    layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    # font='CozetteVector Bold',
    font='mononoki Nerd Font Bold',
    fontsize=11,
    padding=5,
    foreground = colors[15],
    background = colors[0]
    )

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       ),
              widget.TextBox(
                      text = "???",
                      fontsize = 21,
                      foreground = colors[9],
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('code .config')},
                      ),  
              widget.Sep(
                       linewidth = 0,
                       padding = 3,
                       ),                                           
              widget.GroupBox(
                       fontsize = 21,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       inactive = colors[2],
                       active = colors[15],
                       rounded = False,
                       highlight_color = colors[9],
                       highlight_method = "line",
                       this_current_screen_border = colors[15],
                       this_screen_border = colors[15],
                       other_current_screen_border = colors[15],
                       other_screen_border = colors[9],
                       foreground = colors[15],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.Prompt(
                       prompt = prompt,
                       padding = 6,
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.WindowName(
                       padding = 5,
                       fontsize = 10
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.Net(
                      interface = "wlan0",
                      format = 'net {down} ?????? {up}',
                      padding = 5,
                      # ???
                      ),
              widget.Sep(
                      linewidth = 0,
                      padding = 5,
                      ),
              widget.TextBox(
                      text = "|",
                      fontsize = 12,
                      foreground = colors[2],
                      ),
              widget.Memory(
                      format = 'mem {MemUsed: .0f}{mm}',
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bpytop')},
                      padding = 5
                      # ???
                      ),
              widget.Sep(
                      linewidth = 0,
                      padding = 5,
                      ),
              widget.TextBox(
                      text = "|",
                      fontsize = 12,
                      foreground = colors[2],
                      ),
              widget.CPU(
                      padding = 5,
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bpytop')},
                      format = 'cpu {load_percent}%',
                      # ???
                      ),
              widget.Sep(
                      linewidth = 0,
                      padding = 5,
                      ),
              widget.TextBox(
                      text = "|",
                      fontsize = 12,
                      foreground = colors[2],
                      ),
              widget.NvidiaSensors(
                      font='mononoki Nerd Font Bold',
                      fontsize=11,
                      padding=5,
                      foreground = colors[15],
                      background = colors[0],
                      format = 'gpu {temp}??C fan speed {fan_speed}'
              ),                   
              widget.Sep(
                      linewidth = 0,
                      padding = 5,
                      ),
              widget.TextBox(
                      text = "|",
                      fontsize = 12,
                      foreground = colors[2],
                      ),
              owm.OpenWeatherMap(
                        api_key="6588060df1425c900dd65a154f6f94f6",
                        latitude=28.3398326339,
                        longitude=-80.662854212,
                        icon_font="Weather Icons",
                        units="imperial",
                        format="Temp: {temp:.1f}{temp_units} {icon}"
                        ),     
              widget.Sep(
                      linewidth = 0,
                      padding = 5,
                      ),
              widget.TextBox(
                      text = "|",
                      fontsize = 12,
                      foreground = colors[2],
                      ),
              owm.OpenWeatherMap(
                        api_key="6588060df1425c900dd65a154f6f94f6",
                        latitude=28.3398326339,
                        longitude=-80.662854212,
                        icon_font="Weather Icons",
                        units="imperial",
                        format="Wind: {wind_speed:.1f}{wind_units} {wind_direction}"
                        ),                                  
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.TextBox(
                       text = "|",
                       fontsize = 12,
                       foreground = colors[2],
                       ),
              widget.Clock(
                       format = "???  %m.%d.%y -%l:%M %p ",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e calcure')},
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.TextBox(
                       text = "|",
                       fontsize = 12,
                       foreground = colors[2],
                       ),
              widget.Systray(),
              widget.TextBox(
                       text = "|",
                       fontsize = 12,
                       foreground = colors[2],
                       ),              
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       padding = 5,
                       scale = 0.7
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),
              widget.QuickExit(
                       default_text = "???",
                       fontsize = 21,
                       foreground = colors[9],
                       countdown_format = '[{}]',
                       countdown_start = 1
                       ),   
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       ),                                             
            ], 24, ), ),
]

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

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='notification'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
