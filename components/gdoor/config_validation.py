import esphome.config_validation as cv

def hex_string(value):
    value = cv.string(value)
    if value.startswith('0x'):
        value = value[2:]
    _ = bytes.fromhex(value)
    return value.toUpper()