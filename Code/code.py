import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB, AnimationModes

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# leds pinout
rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=5,   
    val_limit=100,  
    hue_default=120, 
    sat_default=255,
    val_default=100,
    animation_mode=AnimationModes.BREATHING,
    refresh_rate=30,
)
keyboard.extensions.append(rgb)

# pin definition
# collums
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)

# rows
keyboard.row_pins = (board.GP3, board.GP4, board.GP29)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.GP1, board.GP0, None, False),
)

# encoder settings
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]

# display
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.STATIC,1:["Mode"]},
        corner_four={0:OledReactionType.STATIC,1:["Numpad"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    sda=board.GP6,
    scl=board.GP7,
    flip=False, 
)
keyboard.extensions.append(oled_ext)

# mapped keys
keyboard.keymap = [
    [   
        KC.N7,    KC.N8,    KC.N9,
        KC.N4,    KC.N5,    KC.N6,
        KC.N1,    KC.N2,    KC.N3,
    ]
]

if __name__ == '__main__':
    keyboard.go()
