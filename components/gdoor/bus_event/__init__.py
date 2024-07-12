import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.event as event
from esphome.const import CONF_ID

import conf_constants as cid
import config_validation as gdoor_cv
from .. import (
    Gdoor,
    GDoorBusEvent_P,
    CONF_GDOOR,
    gdoor_ns
)

GDoorBusEvent = gdoor_ns.class_('GDoorBusEvent', GDoorBusEvent_P, event.Event, cg.Component)

CONFIG_SCHEMA = event.EVENT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(GDoorBusEvent),
    cv.GenerateID(CONF_GDOOR): cv.use_id(Gdoor)
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_GDOOR])
    await event.register_event(var, config)
    