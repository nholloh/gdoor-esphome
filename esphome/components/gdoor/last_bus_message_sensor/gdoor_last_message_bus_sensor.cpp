#include "esphome/core/log.h"
#include "gdoor_last_message_bus_sensor.h"

namespace esphome {
namespace gdoor_esphome {

static const char *TAG = "gdoor_esphome.gdoor";
static const GDOOR_DATA_PROTOCOL gdoor_data_idle(NULL, true);

void GDoorLastMessageBusSensor::setup() {
    ESP_LOGI(TAG, "Setting up GDoorLastMessageBusSensor");
}

void GDoorLastMessageBusSensor::dump_config() { 
    ESP_LOGCONFIG(TAG, "GDoor base");
}

void GDoorLastMessageBusSensor::press() {
    ESP_LOGI(TAG, "Button ", *this->name_, " pressed");
    ESP_LOGD(TAG, "Sending bus message ", *this->button_busmessage_);
    this->parent_->send(this->button_busmessage_);
}

}  // namespace gdoor_esphome
}  // namespace esphome