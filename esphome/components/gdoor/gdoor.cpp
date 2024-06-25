#include "esphome/core/log.h"
#include "gdoor.h"
#include "lib/gdoor.h"

namespace esphome {
namespace gdoor_esphome {

static const char *TAG = "gdoor_esphome.gdoor";

void GDoor::setup() {
    ESP_LOGI(TAG, "Setting up GDoorSensor");
    
    GDOOR::setRxThreshold(PIN_RX_THRESH, this->rx_pin_threshold_);

    GDOOR::setup(PIN_TX, PIN_TX_EN, this->rx_pin_);

    // Publish initial idle state.
    publish_state(gdoor_data_idle.action);
}

void GDoor::dump_config() { 
    ESP_LOGCONFIG(TAG, "GDoor base");
}

void GDoor::loop() {
    GDOOR::loop();

    GDOOR_DATA* rx_data = GDOOR::read();
    if(rx_data != NULL) {
        ESP_LOGI(TAG, "Received data from bus");
        GDOOR_DATA_PROTOCOL busmessage = GDOOR_DATA_PROTOCOL(rx_data);
        ESP_LOGD(TAG, "Data: ", busmessage);

        // Set sensor state.
        this->onStateUpdateEvent(busmessage.action);
        this->onStateUpdateLastReceived(busmessage.action);
    }
}

void GDoor::send(String str) {
    GDOOR::send(str);
}

void GDoor::registerLastReceived(void (*callback)(String)) {
    this->onStateUpdateLastReceived = callback;
}

void GDoor::registerEvent(void (*callback)(String)) {
    this->onStateUpdateEvent = callback;
}

}  // namespace gdoor_esphome
}  // namespace esphome