import json

stylesheet_dark = """
    * {{
        font-family: monospace;
    }}
    QWidget {{
        background-color: {background};
        color: {foreground};
    }}
    QPushButton {{
        background-color: {gray};
        color: {white};
        border: 1px solid {gray};
        padding: 5px;
        border-radius: 4px;
    }}
    QPushButton:hover {{
        background-color: {blue};
    }}
    QLabel#tile {{
        border: 3px solid {tile-border};
        background-color: {background};
        color: {foreground};
        font-size: 32px;
        font-weight: bold;
    }}
    QLabel.best-label {{
        font-size: 11px;
        color: {white};
    }}
    QLabel.bits-label, QLabel.poss-label {{
        font-size: 10px;
        color: {foreground};
    }}
    QComboBox {{
        background-color: {gray};
        color: {white};
        border: 1px solid {gray};
        padding: 5px;
        border-radius: 4px;
    }}
    QComboBox:hover {{
        background-color: {blue};
    }}
    QComboBox::drop-down {{
        border: none;
        width: 20px;
    }}
    QComboBox::down-arrow {{
        width: 0;
        height: 0;
        border-left: 6px solid transparent;
        border-right: 6px solid transparent;
        border-top: 1px solid {foreground};
        margin-right: 6px;
    }}
"""

stylesheet_light = """
    * {{
        font-family: monospace;
    }}
    QWidget {{
        background-color: {background};
        color: {foreground};
    }}
    QPushButton {{
        background-color: {background};
        color: {gray};
        border: 1px solid {gray};
        padding: 5px;
        border-radius: 4px;
    }}
    QPushButton:hover {{
        background-color: {blue};
        color: {white};
    }}
    QLabel#tile {{
        border: 3px solid {tile-border};
        background-color: {background};
        color: {foreground};
        font-size: 32px;
        font-weight: bold;
    }}
    QLabel.best-label {{
        font-size: 11px;
        color: {white};
    }}
    QLabel.bits-label, QLabel.poss-label {{
        font-size: 10px;
        color: {foreground};
    }}
    QComboBox {{
        background-color: {background};
        color: {gray};
        border: 1px solid {gray};
        padding: 5px;
        border-radius: 4px;
    }}
    QComboBox:hover {{
        background-color: {blue};
    }}
    QComboBox::drop-down {{
        border: none;
        width: 20px;
    }}
    QComboBox::down-arrow {{
        width: 0;
        height: 0;
        border-left: 6px solid transparent;
        border-right: 6px solid transparent;
        border-top: 1px solid {gray};
        margin-right: 6px;
    }}
"""

styles = {
    "nord": {
        "colors": {
            "background": "#2E3440",
            "foreground": "#D8DEE9",
            "red": "#BF616A",
            "green": "#A3BE8C",
            "yellow": "#EBCB8B",
            "blue": "#81A1C1",
            "magenta": "#B48EAD",
            "cyan": "#88C0D0",
            "white": "#E5E9F0",
            "gray": "#4C566A",
            "tile-border": "#3B4252",
        },
        "stylesheet": stylesheet_dark
    },

    "solarized-light": {
        "colors": {
            "background": "#FDF6E3",
            "foreground": "#657B83",
            "red": "#DC322F",
            "green": "#859900",
            "yellow": "#B58900",
            "blue": "#268BD2",
            "magenta": "#D33682",
            "cyan": "#2AA198",
            "white": "#EEE8D5",
            "gray": "#93A1A1",
            "tile-border": "#93A1A1",
        },
        "stylesheet": stylesheet_light
    },

    "dracula": {
        "colors": {
            "background": "#282A36",
            "foreground": "#F8F8F2",
            "red": "#FF5555",
            "green": "#50FA7B",
            "yellow": "#F1FA8C",
            "blue": "#6272A4",
            "magenta": "#BD93F9",
            "cyan": "#8BE9FD",
            "white": "#FFFFFF",
            "gray": "#44475A",
            "tile-border": "#6272A4",
        },
        "stylesheet": stylesheet_dark
    },

    "gruvbox-dark": {
        "colors": {
            "background": "#282828",
            "foreground": "#EBDBB2",
            "red": "#CC241D",
            "green": "#98971A",
            "yellow": "#D79921",
            "blue": "#458588",
            "magenta": "#B16286",
            "cyan": "#689D6A",
            "white": "#FBF1C7",
            "gray": "#928374",
            "tile-border": "#3C3836",
        },
        "stylesheet": stylesheet_dark
    },

    "gruvbox-light": {
        "colors": {
            "background": "#FBF1C7",
            "foreground": "#3C3836",
            "red": "#9D0006",
            "green": "#79740E",
            "yellow": "#B57614",
            "blue": "#076678",
            "magenta": "#8F3F71",
            "cyan": "#427B58",
            "white": "#F9F5D7",
            "gray": "#928374",
            "tile-border": "#D5C4A1",
        },
        "stylesheet": stylesheet_light
    },

    "monokai": {
        "colors": {
            "background": "#272822",
            "foreground": "#F8F8F2",
            "red": "#F92672",
            "green": "#A6E22E",
            "yellow": "#E6DB74",
            "blue": "#66D9EF",
            "magenta": "#FD5FF0",
            "cyan": "#A1EFE4",
            "white": "#F8F8F0",
            "gray": "#75715E",
            "tile-border": "#49483E",
        },
        "stylesheet": stylesheet_dark
    },

    "one-dark": {
        "colors": {
            "background": "#282C34",
            "foreground": "#ABB2BF",
            "red": "#E06C75",
            "green": "#98C379",
            "yellow": "#E5C07B",
            "blue": "#61AFEF",
            "magenta": "#C678DD",
            "cyan": "#56B6C2",
            "white": "#FFFFFF",
            "gray": "#5C6370",
            "tile-border": "#3E4451",
        },
        "stylesheet": stylesheet_dark
    },

    "material-dark": {
        "colors": {
            "background": "#263238",
            "foreground": "#ECEFF1",
            "red": "#FF5252",
            "green": "#69F0AE",
            "yellow": "#FFD740",
            "blue": "#40C4FF",
            "magenta": "#FF4081",
            "cyan": "#18FFFF",
            "white": "#FAFAFA",
            "gray": "#90A4AE",
            "tile-border": "#37474F",
        },
        "stylesheet": stylesheet_dark
    },

    "tomorrow-night": {
        "colors": {
            "background": "#1D1F21",
            "foreground": "#C5C8C6",
            "red": "#CC6666",
            "green": "#B5BD68",
            "yellow": "#F0C674",
            "blue": "#81A2BE",
            "magenta": "#B294BB",
            "cyan": "#8ABEB7",
            "white": "#FFFFFF",
            "gray": "#969896",
            "tile-border": "#282A2E",
        },
        "stylesheet": stylesheet_dark
    },

    "high-contrast": {
        "colors": {
            "background": "#000000",
            "foreground": "#FFFFFF",
            "red": "#FF0000",
            "green": "#00FF00",
            "yellow": "#FFFF00",
            "blue": "#0000FF",
            "magenta": "#FF00FF",
            "cyan": "#00FFFF",
            "white": "#FFFFFF",
            "gray": "#7F7F7F",
            "tile-border": "#FFFFFF",
        },
        "stylesheet": stylesheet_dark
    },

    "tango": {
        "colors": {
            "background": "#2E3436",
            "foreground": "#D3D7CF",
            "red": "#CC0000",
            "green": "#4E9A06",
            "yellow": "#C4A000",
            "blue": "#3465A4",
            "magenta": "#75507B",
            "cyan": "#06989A",
            "white": "#EEEEEC",
            "gray": "#888A85",
            "tile-border": "#555753",
        },
        "stylesheet": stylesheet_dark
    },

    "zenburn": {
        "colors": {
            "background": "#3F3F3F",
            "foreground": "#DCDCCC",
            "red": "#CC9393",
            "green": "#7F9F7F",
            "yellow": "#F0DFAF",
            "blue": "#6CA0A3",
            "magenta": "#DC8CC3",
            "cyan": "#93E0E3",
            "white": "#FFFFFF",
            "gray": "#6F6F6F",
            "tile-border": "#5F5F5F",
        },
        "stylesheet": stylesheet_dark
    },

    "arc-dark": {
        "colors": {
            "background": "#2F343F",
            "foreground": "#D3DAE3",
            "red": "#D52753",
            "green": "#23974A",
            "yellow": "#DF631C",
            "blue": "#275FE4",
            "magenta": "#823FF1",
            "cyan": "#27618D",
            "white": "#FFFFFF",
            "gray": "#404552",
            "tile-border": "#3C4048",
        },
        "stylesheet": stylesheet_dark
    },
        "one-light": {
        "colors": {
            "background": "#FAFAFA",
            "foreground": "#383A42",
            "red": "#E45649",
            "green": "#50A14F",
            "yellow": "#C18401",
            "blue": "#4078F2",
            "magenta": "#A626A4",
            "cyan": "#0184BC",
            "white": "#FFFFFF",
            "gray": "#9E9E9E",
            "tile-border": "#CCCCCC",
        },
        "stylesheet": stylesheet_light
    },

    "material-light": {
        "colors": {
            "background": "#FAFAFA",
            "foreground": "#263238",
            "red": "#E53935",
            "green": "#43A047",
            "yellow": "#FDD835",
            "blue": "#1E88E5",
            "magenta": "#8E24AA",
            "cyan": "#00ACC1",
            "white": "#FFFFFF",
            "gray": "#BDBDBD",
            "tile-border": "#E0E0E0",
        },
        "stylesheet": stylesheet_light
    },

    "solarized-dark": {
        "colors": {
            "background": "#002B36",
            "foreground": "#839496",
            "red": "#DC322F",
            "green": "#859900",
            "yellow": "#B58900",
            "blue": "#268BD2",
            "magenta": "#D33682",
            "cyan": "#2AA198",
            "white": "#EEE8D5",
            "gray": "#586E75",
            "tile-border": "#073642",
        },
        "stylesheet": stylesheet_dark
    },

    "github-light": {
        "colors": {
            "background": "#FFFFFF",
            "foreground": "#24292E",
            "red": "#D73A49",
            "green": "#28A745",
            "yellow": "#DBAB09",
            "blue": "#0366D6",
            "magenta": "#6F42C1",
            "cyan": "#1B7C83",
            "white": "#F6F8FA",
            "gray": "#6A737D",
            "tile-border": "#E1E4E8",
        },
        "stylesheet": stylesheet_light
    },

    "github-dark": {
        "colors": {
            "background": "#0D1117",
            "foreground": "#C9D1D9",
            "red": "#F85149",
            "green": "#56D364",
            "yellow": "#E3B341",
            "blue": "#58A6FF",
            "magenta": "#BC8CFF",
            "cyan": "#39C5CF",
            "white": "#FFFFFF",
            "gray": "#484F58",
            "tile-border": "#21262D",
        },
        "stylesheet": stylesheet_dark
    },

    "ayu-dark": {
        "colors": {
            "background": "#0A0E14",
            "foreground": "#B3B1AD",
            "red": "#F07178",
            "green": "#B8CC52",
            "yellow": "#E6B450",
            "blue": "#59C2FF",
            "magenta": "#D2A6FF",
            "cyan": "#95E6CB",
            "white": "#FFFFFF",
            "gray": "#3D424D",
            "tile-border": "#131721",
        },
        "stylesheet": stylesheet_dark
    },

    "ayu-light": {
        "colors": {
            "background": "#FAFAFA",
            "foreground": "#5C6773",
            "red": "#F07171",
            "green": "#86B300",
            "yellow": "#F2AE49",
            "blue": "#399EE6",
            "magenta": "#A37ACC",
            "cyan": "#4CBF99",
            "white": "#FFFFFF",
            "gray": "#ABB0B6",
            "tile-border": "#D9D9D9",
        },
        "stylesheet": stylesheet_light
    },

    "papercolor-light": {
        "colors": {
            "background": "#EEEEEE",
            "foreground": "#444444",
            "red": "#AF0000",
            "green": "#008700",
            "yellow": "#5F8700",
            "blue": "#0087AF",
            "magenta": "#878787",
            "cyan": "#005F87",
            "white": "#FFFFFF",
            "gray": "#808080",
            "tile-border": "#CCCCCC",
        },
        "stylesheet": stylesheet_light
    },

    "papercolor-dark": {
        "colors": {
            "background": "#1C1C1C",
            "foreground": "#D0D0D0",
            "red": "#AF005F",
            "green": "#5FAF00",
            "yellow": "#D7AF5F",
            "blue": "#5FAFD7",
            "magenta": "#808080",
            "cyan": "#5FAFAF",
            "white": "#FFFFFF",
            "gray": "#585858",
            "tile-border": "#303030",
        },
        "stylesheet": stylesheet_dark
    },

    "tokyo-night": {
        "colors": {
            "background": "#1A1B26",
            "foreground": "#A9B1D6",
            "red": "#F7768E",
            "green": "#9ECE6A",
            "yellow": "#E0AF68",
            "blue": "#7AA2F7",
            "magenta": "#BB9AF7",
            "cyan": "#7DCFFF",
            "white": "#C0CAF5",
            "gray": "#565F89",
            "tile-border": "#2A2C3C",
        },
        "stylesheet": stylesheet_dark
    }
}


def get_current_style():
    with open("settings.json", "r") as file:
        settings = json.load(file)
    return settings["style"]


def set_current_style(style: str):
    with open("settings.json", "w") as file:
        json.dump({"style": style}, file, indent = 4)

def get_stylesheet(style_name: str) -> str:
    style = styles[style_name]
    return style["stylesheet"].format(**style["colors"])

