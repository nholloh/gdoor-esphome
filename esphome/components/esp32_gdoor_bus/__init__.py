import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID

MULTI_CONF = False

AUTO_LOAD = ['text_sensor']

gdoor_esphome_ns = cg.esphome_ns.namespace('gdoor_esphome')
GDoorSensor = gdoor_esphome_ns.class_('GDoorSensor', text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(GDoorSensor)
}).extend(cv.COMPONENT_SCHEMA).extend(cv.only_with_arduino())

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield text_sensor.register_text_sensor(var, config)
    yield cg.register_component(var, config)

PLATFORM_SCHEMA = CONFIG_SCHEMA

text_sensor.register_platform('gdoor-sensor', PLATFORM_SCHEMA, to_code)
