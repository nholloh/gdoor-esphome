import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.event as event
from esphome.const import CONF_ID

import conf_constants as cid
import config_validation as gdoor_cv
from .. import (
    GDoor,
    GDoorBusEvent_P,
    CONF_GDOOR_ID
)

DOMAIN = "gdoor"

gdoor_esphome_ns = cg.esphome_ns.namespace('gdoor_esphome')
GDoorBusEvent = gdoor_esphome_ns.class_('GDoorBusEvent', GDoorBusEvent_P, event.Event, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(GDoorBusEvent),
    cv.GenerateID(CONF_GDOOR_ID): cv.use_id(GDoor)
}).extend(event.EVENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_GDOOR_ID])
    await event.register_event(var, config)