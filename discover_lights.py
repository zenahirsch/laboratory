from lifxlan import LifxLAN

NUM_LIGHTS = 3

lan = LifxLAN(NUM_LIGHTS)

for light in lan.get_lights():
    print(light)
