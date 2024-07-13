import re
import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.button as button
from esphome import pins
from esphome.const import (
  CONF_ID
)  

MULTI_CONF = True
AUTO_LOAD = ["button", "text_sensor", "event"]

gdoor_ns = cg.esphome_ns.namespace('gdoor_esphome')
Gdoor = gdoor_ns.class_("GDoor", cg.Component)

CONF_GDOOR = "gdoor"
CONF_RX_PIN = "rx_pin"
CONF_SENSITIVITY = "sensitivity"

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(Gdoor),
        cv.Optional(CONF_RX_PIN): pins.gpio_input_pin_schema,
        cv.Optional(CONF_SENSITIVITY, default=1.65): cv.float_range(min=1.3, max=1.65),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_rx_pin(config[CONF_RX_PIN]))
    cg.add(var.set_rx_sensitivity(config[CONF_SENSITIVITY]))
