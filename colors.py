# color is a HSBK list of values:
# [hue (0-65535), saturation (0-65535), brightness (0-65535), Kelvin (2500-9000)]

HUE_ORG = 8500
HUE_GRN = 21845
HUE_CYN = 29814
HUE_BLU = 43634
HUE_PUR = 50000
HUE_PNK = 58275
HUE_RED = 65535

BRIGHTNESS_MUTED = 300
BRIGHTNESS_DIM = 3000
BRIGHTNESS_MID = 31000
BRIGHTNESS_BRT = 65535

SATURATION_MAX = 65535
SATURATION_MIN = 1

KELVIN_MID = 3500

MUTED_ORANGE   =  [HUE_ORG, SATURATION_MAX, BRIGHTNESS_MUTED, KELVIN_MID]
MUTED_BLUE     =  [HUE_BLU, SATURATION_MAX, BRIGHTNESS_MUTED, KELVIN_MID]
MUTED_PURPLE   =  [HUE_PUR, SATURATION_MAX, BRIGHTNESS_MUTED, KELVIN_MID]

DIM_ORANGE     =  [HUE_ORG, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_GREEN      =  [HUE_GRN, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_CYAN       =  [HUE_CYN, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_BLUE       =  [HUE_BLU, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_PURPLE     =  [HUE_PUR, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_PINK       =  [HUE_PNK, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]
DIM_RED        =  [HUE_RED, SATURATION_MAX, BRIGHTNESS_DIM, KELVIN_MID]

MID_ORANGE     =  [HUE_ORG, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_GREEN      =  [HUE_GRN, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_CYAN       =  [HUE_CYN, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_BLUE       =  [HUE_BLU, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_PURPLE     =  [HUE_PUR, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_PINK       =  [HUE_PNK, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]
MID_RED        =  [HUE_RED, SATURATION_MAX, BRIGHTNESS_MID, KELVIN_MID]

BRIGHT_ORANGE  =  [HUE_ORG, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_GREEN   =  [HUE_GRN, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_CYAN    =  [HUE_CYN, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_BLUE    =  [HUE_BLU, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_PURPLE  =  [HUE_PUR, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_PINK    =  [HUE_PNK, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]
BRIGHT_RED     =  [HUE_RED, SATURATION_MAX, BRIGHTNESS_BRT, KELVIN_MID]

MID_RAINBOW = [
    MID_RED,
    MID_ORANGE,
    MID_GREEN,
    MID_CYAN,
    MID_BLUE,
    MID_PURPLE,
]