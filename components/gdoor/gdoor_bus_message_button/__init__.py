import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.button as button
from esphome.const import CONF_ID

import conf_constants as cid
import config_validation as gdoor_cv
from .. import (
    Gdoor,
    CONF_GDOOR,
    gdoor_ns
)

GDoorBusMessageButton = gdoor_ns.class_('GDoorBusMessageButton', button.Button, cg.Component)

CONFIG_SCHEMA = button.BUTTON_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(GDoorBusMessageButton),
    cv.GenerateID(CONF_GDOOR): cv.use_id(Gdoor),
    cv.Required(cid.CONF_ID_BUTTON_BUSMESSAGE): gdoor_cv.hex_string
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[cid.CONF_ID_BUTTON_BUSMESSAGE])
    await cg.register_component(var, config)
    await button.register_button(var, config)
    parent = await cg.get_variable(config[CONF_GDOOR])
    cg.add(var.set_parent(parent))
    cg.add(var.set_button_busmessage(config[cid.CONF_ID_BUTTON_BUSMESSAGE]))