import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode
import time
import random


def type_string(kb, text, delay_ms=50):
    """Type a string by pressing and releasing each key."""
    keycode_map = {
        "a": KeyCode.A, "b": KeyCode.B, "c": KeyCode.C, "d": KeyCode.D,
        "e": KeyCode.E, "f": KeyCode.F, "g": KeyCode.G, "h": KeyCode.H,
        "i": KeyCode.I, "j": KeyCode.J, "k": KeyCode.K, "l": KeyCode.L,
        "m": KeyCode.M, "n": KeyCode.N, "o": KeyCode.O, "p": KeyCode.P,
        "q": KeyCode.Q, "r": KeyCode.R, "s": KeyCode.S, "t": KeyCode.T,
        "u": KeyCode.U, "v": KeyCode.V, "w": KeyCode.W, "x": KeyCode.X,
        "y": KeyCode.Y, "z": KeyCode.Z, " ": KeyCode.SPACE,
        "0": KeyCode.N0, "1": KeyCode.N1, "2": KeyCode.N2, "3": KeyCode.N3,
        "4": KeyCode.N4, "5": KeyCode.N5, "6": KeyCode.N6, "7": KeyCode.N7,
        "8": KeyCode.N8, "9": KeyCode.N9,
        ".": KeyCode.DOT, ",": KeyCode.COMMA, "/": KeyCode.SLASH,
        ";": KeyCode.SEMICOLON, "-": KeyCode.MINUS, "=": KeyCode.EQUAL,
    }
    # Characters that require Shift + a base key
    shift_map = {
        ":": KeyCode.SEMICOLON, "?": KeyCode.SLASH, "!": KeyCode.N1,
        "@": KeyCode.N2, "#": KeyCode.N3, "$": KeyCode.N4, "%": KeyCode.N5,
        "^": KeyCode.N6, "&": KeyCode.N7, "*": KeyCode.N8, "(": KeyCode.N9,
        ")": KeyCode.N0, "+": KeyCode.EQUAL, "_": KeyCode.MINUS,
    }
    for ch in text:
        if ch.isupper():
            kb.send_keys([KeyCode.LEFT_SHIFT, keycode_map[ch.lower()]])
        elif ch in shift_map:
            kb.send_keys([KeyCode.LEFT_SHIFT, shift_map[ch]])
        else:
            code = keycode_map.get(ch)
            if code is None:
                continue
            kb.send_keys([code])
        time.sleep_ms(delay_ms)
        kb.send_keys([])  # release
        time.sleep_ms(delay_ms)


kb = KeyboardInterface()
usb.device.get().init(kb, builtin_driver=True)

# Wait for host to enumerate the device
while not kb.is_open():
    time.sleep_ms(100)

time.sleep(1)

kb.send_keys([KeyCode.LEFT_UI, KeyCode.SPACE])
time.sleep_ms(50)
kb.send_keys([])
time.sleep(0.5)

type_string(kb, "chrome")
time.sleep_ms(100)

kb.send_keys([KeyCode.ENTER])
time.sleep_ms(50)
kb.send_keys([])

time.sleep(0.75)
kb.send_keys([KeyCode.LEFT_UI, KeyCode.N])
time.sleep_ms(50)
kb.send_keys([])

time.sleep(1)
type_string(kb, "https://gemini.google.com/", delay_ms=10)
time.sleep_ms(50)
kb.send_keys([KeyCode.ENTER])
time.sleep_ms(50)
kb.send_keys([])
time.sleep(2)

WORDS = [
    "galaxy", "trumpet", "marble", "cactus", "phoenix", "lantern", "breeze", "fossil",
    "velvet", "anchor", "prism", "dagger", "cobalt", "ember", "falcon", "glacier",
    "horizon", "ivory", "jungle", "kettle", "lemon", "mystic", "nebula", "orchid",
    "parrot", "quartz", "riddle", "summit", "tundra", "umbra", "vortex", "walrus",
    "zenith", "blizzard", "copper", "dolphin", "eclipse", "furnace", "granite", "harpoon",
    "insect", "jasmine", "kayak", "labyrinth", "magnet", "nomad", "obelisk", "puzzle",
    "quantum", "raven", "scarlet", "tornado", "unicorn", "vagrant", "whisper", "xylophone",
    "yonder", "zeppelin", "alchemy", "bamboo", "cascade", "dungeon", "enigma", "firestorm",
    "gargoyle", "hammock", "igloo", "jigsaw", "kraken", "limestone", "mirage", "nucleus",
    "octagon", "phantom", "quicksand", "relic", "sapphire", "tempest", "utopia", "volcano",
    "wildfire", "xenon", "yearning", "zigzag", "aurora", "basilisk", "chimera", "dragonfly",
    "emerald", "fjord", "gazelle", "hydra", "inferno", "jubilee", "kaleidoscope", "lynx",
    "monsoon", "nectarine", "osprey", "porcupine", "quintet", "rattlesnake", "sphinx",
    "thistle", "undertow", "vineyard", "wisteria", "passport", "yucca", "zodiac",
    "avalanche", "bonsai", "centaur", "driftwood", "evergreen", "flamingo", "geyser",
    "hedgehog", "iceberg", "jackal", "kudzu", "lighthouse", "mantis", "nautilus",
    "obsidian", "penguin", "quasar", "rosemary", "stallion", "tapestry",
]

while True:
    picked = []
    indices = list(range(len(WORDS)))
    for _ in range(5):
        i = random.randint(0, len(indices) - 1)
        picked.append(WORDS[indices.pop(i)])
    prompt = "What do you think about " + " ".join(picked) + "?"
    type_string(kb, prompt)
    kb.send_keys([KeyCode.ENTER])
    time.sleep_ms(50)
    kb.send_keys([])
    time.sleep(random.randint(30, 60))

