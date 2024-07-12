import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.text_sensor as text_sensor
from esphome.const import CONF_ID

import conf_constants as cid
from .. import (
    Gdoor,
    GDoorLastMessageBusSensor_P,
    CONF_GDOOR,
    gdoor_ns
)

GDoorLastMessageBusSensor = gdoor_ns.class_('GDoorLastMessageBusSensor', GDoorLastMessageBusSensor_P, text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(GDoorLastMessageBusSensor),
    cv.GenerateID(CONF_GDOOR): cv.use_id(Gdoor),
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_GDOOR])
    await text_sensor.register_text_sensor(var, config)