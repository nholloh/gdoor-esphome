#include "esphome/core/log.h"
#include "gdoor.h"
#include "lib/gdoor.h"
#include "gdoor_bus_event.h"

namespace esphome {
namespace gdoor_esphome {

static const char *TAG = "gdoor_esphome.gdoor";
static const String *PREFIX = "gdoor_";

void GDoorEvent::setup() {
    ESP_LOGI(TAG, "Setting up GDoorEvent");
    this->parent_->registerEvent([this](String action) {
        this->trigger(PREFIX + action);
    });
}

}  // namespace gdoor_esphome
}  // namespace esphome