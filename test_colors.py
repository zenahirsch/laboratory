from lights import laboratory
from colors import BRIGHT_RED, DIM_PURPLE, MID_CYAN

def test_color(light_or_group, color):
    print(f"Testing color {color} on {light_or_group}")
    light_or_group.set_color(color)

if __name__ == '__main__':
    test_color(laboratory, DIM_PURPLE)
