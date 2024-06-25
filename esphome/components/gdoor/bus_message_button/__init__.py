import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.button as button
from esphome.const import CONF_ID

import conf_constants as cid
import config_validation as gdoor_cv
from .. import (
    GDoor,
    GDoorBusMessageButton_P,
    CONF_GDOOR_ID
)

DOMAIN = "gdoor"

gdoor_esphome_ns = cg.esphome_ns.namespace('gdoor_esphome')
GDoorBusMessageButton = gdoor_esphome_ns.class_('GDoorBusMessageButton', GDoorBusMessageButton_P, button.Button, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(GDoorBusMessageButton),
    cv.GenerateID(CONF_GDOOR_ID): cv.use_id(GDoor),
    cv.Required(cid.CONF_ID_BUTTON_BUSMESSAGE): gdoor_cv.hex_string
}).extend(button.BUTTON_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_GDOOR_ID])
    cg.add(var.set_button_busmessage(config[cid.CONF_ID_BUTTON_BUSMESSAGE]))
    await button.register_button(var, config)