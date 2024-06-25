#include "esphome/core/log.h"
#include "gdoor_bus_message_button.h"

namespace esphome {
namespace gdoor_esphome {

static const char *TAG = "gdoor_esphome.gdoor";

void GDoorBusMessageButton::setup() {
    ESP_LOGI(TAG, "Setting up GDoorBusMessageButton");
}

void GDoorBusMessageButton::dump_config() { 
    ESP_LOGCONFIG(TAG, "GDoor base");
}

void GDoorBusMessageButton::press() {
    ESP_LOGI(TAG, "Button ", *this->button_name_, " pressed");
    ESP_LOGD(TAG, "Sending bus message ", *this->button_busmessage_);
    this->parent_->send(this->button_busmessage_);
}

}  // namespace gdoor_esphome
}  // namespace esphome