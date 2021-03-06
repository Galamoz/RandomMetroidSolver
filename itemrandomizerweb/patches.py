patches = {
    "Removes_Gravity_Suit_heat_protection": {
        0x06e37d: [0x01],
        0x0869dd: [0x01]},
    "Mother_Brain_Cutscene_Edits": {
        0x148824: [0x01,0x00],
        0x148848: [0x01,0x00],
        0x148867: [0x01,0x00],
        0x14887f: [0x01,0x00],
        0x148bdb: [0x04,0x00],
        0x14897d: [0x10,0x00],
        0x1489af: [0x10,0x00],
        0x1489e1: [0x10,0x00],
        0x148a09: [0x10,0x00],
        0x148a31: [0x10,0x00],
        0x148a63: [0x10,0x00],
        0x148a95: [0x10,0x00],
        0x148b33: [0x10,0x00],
        0x148dc6: [0xb0],
        0x148b8d: [0x12,0x00],
        0x148d74: [0x00,0x00],
        0x148d86: [0x00,0x00],
        0x148daf: [0x00,0x01],
        0x148e51: [0x01,0x00],
        0x14b93a: [0x00,0x01],
        0x148eef: [0x0a,0x00],
        0x148f0f: [0x60,0x00],
        0x14af4e: [0x0a,0x00],
        0x14af0d: [0x0a,0x00],
        0x14b00d: [0x00,0x00],
        0x14b132: [0x40,0x00],
        0x14b16d: [0x00,0x00],
        0x14b19f: [0x20,0x00],
        0x14b1b2: [0x30,0x00],
        0x14b20c: [0x03,0x00]},
    "Suit_acquisition_animation_skip":{
        0x020717: [0xea,0xea,0xea,0xea]},
    "Fix_heat_damage_speed_echoes_bug":{
        0x08b629: [0x01]},
    "Disable_GT_Code":{
        0x15491c: [0x80]},
    "Disable_Space_Time_select_in_menu":{
        0x013175: [0x01]},
    "Fix_Morph_Ball_Hidden_Chozo_PLMs":{
        0x0268ce: [0x04],
        0x026e02: [0x04]},
    "Fix_Screw_Attack_selection_in_menu":{
        0x0134c5: [0x0c]},
    "No_Music":{
        0x278413: [0x6f]},
    "Phantoon_Eye_Door":{
        0x7CCAF: [0x91,0xC2]},
    "Tourian_Refill": {
        0x1922C: [0x47, 0xF6]},
    "Escape_Rando_Enable_Enemies":{
        0x10F000: [0x0, 0x0]},
    "Escape_Rando_Disable_Enemies":{
        0x10F000: [0x1]},
    "Escape_Rando_Tourian_Doors":{
        0x7C836: [0x0C],
        0x7C828: [0x0C]},
    "Save_G4": {
        # load point entry
        0x4527: [0xED, 0xA5, 0x16, 0x92, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0xA8, 0x00, 0x60, 0x00],
        # map icon X/Y
        0x1486f: [0x78, 0x00, 0x48, 0x00]
    },
    "Save_Gauntlet": {
        # load point entry
        0x4519: [0xBD, 0x99, 0x1A, 0x8B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x88, 0x00, 0x50, 0x00],
        # music in room state header
        0x799ce: [0x09],
        # map icon X/Y
        0x1486b: [0x58, 0x00, 0x18, 0x00]
    },
    "Save_Watering_Hole": {
        # load point entry
        0x4979: [0x3B, 0xD1, 0x98, 0xA4, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x88, 0x00, 0xD0, 0xFF],
        # music in room state header
        0x7d14c: [0x1b, 0x06],
        # map icon X/Y
        0x14a0f: [0x68, 0x00, 0x28, 0x00]
    },
    "Save_Etecoons": {
        # load point entry
        0x4631: [0x51, 0xA0, 0x3A, 0x8F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x98, 0x00, 0xD0, 0xFF],
        # music in room state header
        0x7a062: [0x0f, 0x05],
        # map icon X/Y
        0x148d9: [0x28, 0x00, 0x58, 0x00]
    }
}

additional_PLMs = {
    "WS_Map_Grey_Door": {
        'room': 0Xcc6f,
        'plm_bytes_list': [
            [0x48, 0xc8, 0x1, 0x6, 0x61, 0x90]
        ]
    },
    "WS_Save_Blinking_Door": { # works together with ws_save.ips
        'room': 0xcaf6,
        'state': 0xcb08,
        'plm_bytes_list': [
            [0x42, 0xC8, 0x4E, 0x36, 0x62, 0x0C]
        ]
    },
    "Morph_Zebes_Awake": {
        'room': 0x9e9f,
        'state': 0x9ecb,
        'plm_bytes_list': [
            [0xff, 0xff, 0x45, 0x29, 0x1A, 0x00]
        ],
        'locations': [("Morphing Ball", 0)]
    },
    "Save_G4": {
        "room": 0xa5ed,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x3D, 0x0C, 0x07, 0x00]
        ]
    },
    "Save_Gauntlet": {
        "room": 0x99bd,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x0C, 0x0A, 0x06, 0x00]
        ]
    },
    "Save_Watering_Hole": {
        "room": 0xd13b,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x14, 0x0A, 0x07, 0x00]
        ]
    },
    "Save_Etecoons": {
        "room": 0xa051,
        'plm_bytes_list': [
            [0x6F, 0xB7, 0x04, 0x0B, 0x07, 0x00]
        ]
    },
}
