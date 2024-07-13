#include "esphome/core/log.h"
#include "gdoor_last_message_bus_sensor.h"

namespace esphome {
namespace gdoor_esphome {

static const char *TAG = "gdoor_esphome.gdoor";
static const GDOOR_DATA_PROTOCOL gdoor_data_idle(NULL, true);

void GDoorLastMessageBusSensor::setup() {
    ESP_LOGI(TAG, "Setting up GDoorLastMessageBusSensor");
    this->parent_->registerLastReceived([this](String action) {
        this->publish_state(PREFIX + action);
    });
}

void GDoorLastMessageBusSensor::dump_config() { 
    ESP_LOGCONFIG(TAG, "GDoor base");
}

}  // namespace gdoor_esphome
}  // namespace esphome