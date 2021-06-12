from lights import charizard
from colors import BRIGHT_RED, DIM_RED

def test_color(light, color):
    print(f"Testing color {color} on light {light}")
    charizard.set_color(color)

if __name__ == '__main__':
    test_color(charizard, BRIGHT_RED)