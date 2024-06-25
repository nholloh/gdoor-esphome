import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import component
from esphome.const import CONF_ID
import conf_constants as cid

DOMAIN = "gdoor"
MULTI_CONF = False
CONF_GDOOR_ID = cid.CONF_GDOOR_ID

gdoor_esphome_ns = cg.esphome_ns.namespace('gdoor_esphome')
GDoor = gdoor_esphome_ns.class_('GDoor', cg.Component)
GDoorBusMessageButton_P = gdoor_esphome_ns.class_('GDoorBusMessageButton_P', cg.Parented.template(GDoor))
GDoorLastMessageBusSensor_P = gdoor_esphome_ns.class_('GDoorLastMessageBusSensor_P', cg.Parented.template(GDoor))
GDoorBusEvent_P = gdoor_esphome_ns.class_('GDoorBusEvent_P', cg.Parented.template(GDoor))

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(GDoor),
    cv.Optional(cid.CONF_ID_RX_PIN, default='GPIO22'): cv.gpio_input_pin_schema,
    cv.Optional(cid.CONF_ID_RX_SENSITIVITY, default=1.65): cv.positive_float.validators(cv.Range(min=1.3, max=1.65))
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cg.add(var.set_rx_pin(config[cid.CONF_ID_RX_PIN]))
    cg.add(var.set_rx_sensitivity(config[cid.CONF_ID_RX_SENSITIVITY]))