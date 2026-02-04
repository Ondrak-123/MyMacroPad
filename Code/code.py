import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB, AnimationModes

# Initialize the keyboard
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# -------------------------------------------------------------------------
# 1. LED LIGHTING (RGB) - FIXED
# -------------------------------------------------------------------------
# Corrected to 4 LEDs.
# Connected to GPIO2 (SCK pin on your schematic).
rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=4,   # <--- Updated this to 4
    val_limit=100,  # Limits brightness to roughly 40% (saves your eyes)
    hue_default=120, # 120 is Green/Cyan. 0 is Red, 170 is Blue.
    sat_default=255,
    val_default=100,
    animation_mode=AnimationModes.BREATHING, # Nice slow pulse
    refresh_rate=30,
)
keyboard.extensions.append(rgb)

# -------------------------------------------------------------------------
# 2. PIN DEFINITIONS
# -------------------------------------------------------------------------
# Cols: C1(26), C2(27), C3(28) + C4(29) for encoders
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)

# Rows: R1(6), R2(7), R3(0), R4(1)
keyboard.row_pins = (board.GP6, board.GP7, board.GP0, board.GP1)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# -------------------------------------------------------------------------
# 3. ENCODER SETUP
# -------------------------------------------------------------------------
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Mapping the matrix logic for the encoders (using Column 4)
encoder_handler.pins = [
    ((keyboard.col_pins[3], keyboard.row_pins[0], keyboard.row_pins[1]),), # Encoder 1 (Top)
    ((keyboard.col_pins[3], keyboard.row_pins[3], keyboard.row_pins[2]),), # Encoder 2 (Bottom)
]

# Encoder 1: Volume
# Encoder 2: Page Scroll
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD), (KC.PGUP, KC.PGDN)),
]

# -------------------------------------------------------------------------
# 4. OLED DISPLAY
# -------------------------------------------------------------------------
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

# -------------------------------------------------------------------------
# 5. KEYMAP
# -------------------------------------------------------------------------
keyboard.keymap = [
    [   # Layer 0
        # Col 1     Col 2     Col 3     Col 4 (Encoders)
        KC.N7,    KC.N8,    KC.N9,    KC.NO,  # Row 1
        KC.N4,    KC.N5,    KC.N6,    KC.NO,  # Row 2
        KC.N1,    KC.N2,    KC.N3,    KC.NO,  # Row 3
        
        # Row 4: Encoder clicks + Key 0
        KC.MUTE,  KC.ENT,   KC.N0,    KC.NO,  
    ]
]

if __name__ == '__main__':
    keyboard.go()
