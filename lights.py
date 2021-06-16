from lifxlan import LifxLAN

NUM_LIGHTS = 3

lan = LifxLAN(NUM_LIGHTS)

charizard = lan.get_device_by_name('Charizard')
bulbasaur = lan.get_device_by_name('Bulbasaur')
blastoise = lan.get_device_by_name('Blastoise')

laboratory = lan.get_devices_by_group("Laboratory")
