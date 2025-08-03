class ColorPalette:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    def __repr__(self):
        return f"{self.name}: {', '.join(self.colors)}"


class Monokai(ColorPalette):
    def __init__(self):
        super().__init__("Monokai", ["#272822", "#F8F8F2", "#75715E", "#66D9EF", "#A6E22E", "#FD971F"])


class OneDark(ColorPalette):
    def __init__(self):
        super().__init__("Colorful Dark", ["#282C34", "#61AFEF", "#98C379", "#56B3FA", "#C678DD", "#E06C75"])


class SolarizedLight(ColorPalette):
    def __init__(self):
        super().__init__("Solarized Light", ["#FDF6E3", "#B58900", "#2AA198", "#268BD2", "#D33682", "#DC322F"])


class SolarizedDark(ColorPalette):
    def __init__(self):
        super().__init__("Solarized Dark", ["#073642", "#B58900", "#2AA198", "#268BD2", "#D33682", "#DC322F"])

class DarkColorPalette(ColorPalette):
    def __init__(self):
        super().__init__("DarkColorPalette", ["#1a1a1a", "#222831", "#393e46", "#454545", "#5c636e", "#bdbdbd"])

class LightColorPalette(ColorPalette):
    def __init__(self):
        super().__init__("LightColorPalette", ["#ffffff", "#f8f9fa", "#e0e0e0", "#bdbdbd", "#757575", "#424242"])

class WhitePalette(ColorPalette):
    def __init__(self):
        super().__init__("WhitePalette", ["#ffffff", "#f1f1f1", "#eaeaea", "#dddddd", "#cccccc", "#bbbbbb"])

class VibrantPalette(ColorPalette):
    def __init__(self):
        super().__init__("VibrantPalette", ["#ff6f61", "#ffb400", "#00b894", "#0984e3", "#6c5ce7", "#fd79a8"])


def get_all_color_palettes():
    return [
        Monokai(),
        OneDark(),
        SolarizedLight(),
        SolarizedDark(),
        DarkColorPalette(),
        LightColorPalette(),
        WhitePalette(),
        VibrantPalette(),
    ]