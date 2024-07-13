import re
import esphome.codegen as cg
import esphome.config_validation as cv
import esphome.components.button as button

from esphome import pins
from esphome.const import (
  CONF_ID,
  CONF_RX_PIN,
  CONF_SENSITIVITY,
)  

MULTI_CONF = True
AUTO_LOAD = ["button", "text_sensor", "event"]

gdoor_ns = cg.esphome_ns.namespace('gdoor_esphome')
Gdoor = gdoor_ns.class_("GDoor", cg.Component)
GDoorBusMessageButton = gdoor_ns.class_('GDoorBusMessageButton', button.Button, cg.Component)

CONF_GDOOR = "gdoor"

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(Gdoor),
        cv.Optional(CONF_RX_PIN, default='GPIO22'): pins.gpio_input_pin_schema,
        cv.Optional(CONF_SENSITIVITY, default=1.65): cv.float_range(min=1.3, max=1.65),
    }
)

data_validation_list = []

def data(value):
  value = cv.string_strict(value).lower()
  if re.match("^([0-9a-f]{2})+$", value):
    if value in data_validation_list:
      raise cv.Invalid('data field must be a unique frame value')
    else:
      data_validation_list.append(value)
      return value
  else:
    raise cv.Invalid('data must be a hex byte representation, see https://gdoor-org.github.io/documentation/protocol.html for details')

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_rx_pin(config[CONF_RX_PIN]))
    cg.add(var.set_rx_sensitivity(config[CONF_SENSITIVITY]))
