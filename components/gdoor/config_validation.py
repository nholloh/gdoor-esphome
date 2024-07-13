import esphome.config_validation as cv

def hex_string(value):
    value = cv.string_strict(value)
    if value.startswith('0x'):
        value = value[2:]
    
    try: _ = bytes.fromhex(value)
    except ValueError: raise cv.Invalid("Invalid hex string!")

    return value.toUpper()