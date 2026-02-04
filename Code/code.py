import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB, AnimationModes

# code for "MyMacroPad"
# initalization 
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# leds pinout + connection
rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=4,   
    val_limit=100,  
    hue_default=120, 
    sat_default=255,
    val_default=100,
    animation_mode=AnimationModes.BREATHING,
    refresh_rate=30,
)
keyboard.extensions.append(rgb)

# pin definition
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)

keyboard.row_pins = (board.GP6, board.GP7, board.GP0, board.GP1)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# encoder

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# matrix

encoder_handler.pins = [
    ((keyboard.col_pins[3], keyboard.row_pins[0], keyboard.row_pins[1]),), 
    ((keyboard.col_pins[3], keyboard.row_pins[3], keyboard.row_pins[2]),), 
]

# encoder values (Controlling volume and page scrolling).
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD), (KC.PGUP, KC.PGDN)),
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
    flip=False, 
)
keyboard.extensions.append(oled_ext)

# mapped keys

keyboard.keymap = [
    [   
        KC.N7,    KC.N8,    KC.N9,    KC.NO,  
        KC.N4,    KC.N5,    KC.N6,    KC.NO,  
        KC.N1,    KC.N2,    KC.N3,    KC.NO,  
        
        KC.MUTE,  KC.ENT,   KC.N0,    KC.NO,  
    ]
]

if __name__ == '__main__':
    keyboard.go()
