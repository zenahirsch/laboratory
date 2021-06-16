from lifxlan import LifxLAN

NUM_LIGHTS = 4

lan = LifxLAN(NUM_LIGHTS)

charizard = lan.get_device_by_name('Charizard')
bulbasaur = lan.get_device_by_name('Bulbasaur')
blastoise = lan.get_device_by_name('Blastoise')
pikachu = lan.get_device_by_name('Pikachu')

laboratory = lan.get_devices_by_group("Laboratory")
