from lifxlan import LifxLAN

NUM_LIGHTS = 3

lan = LifxLAN(NUM_LIGHTS)

for light in lan.get_lights():
    pass

light = lan.get_device_by_name('Charizard')
print(light)