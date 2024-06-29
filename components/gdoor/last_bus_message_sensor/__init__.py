import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.text_sensor as text_sensor
from esphome.const import CONF_ID

import conf_constants as cid
from .. import (
    GDoor,
    GDoorLastMessageBusSensor_P,
    CONF_GDOOR_ID
)

DOMAIN = "gdoor"

gdoor_esphome_ns = cg.esphome_ns.namespace('gdoor_esphome')
GDoorLastMessageBusSensor = gdoor_esphome_ns.class_('GDoorLastMessageBusSensor', GDoorLastMessageBusSensor_P, text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(GDoorLastMessageBusSensor),
    cv.GenerateID(CONF_GDOOR_ID): cv.use_id(GDoor),
}).extend(text_sensor.text_sensor_schema)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cg.register_parented(var, config[CONF_GDOOR_ID])
    await text_sensor.register_text_sensor(var, config)