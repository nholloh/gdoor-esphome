#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace gdoor_esphome {

class GDoor : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  void send(String str);
  void registerLastReceived(void (*callback)(String));
  void registerEvent(void (*callback)(String));
  void set_rx_pin(int rx_pin) { this->rx_pin_ = rx_pin; }
  void set_rx_sensitivity(float_t rx_pin_threshold) { this->rx_pin_threshold_ = rx_pin_threshold; }
 protected:
  void (*onStateUpdateLastReceived)(String);
  void (*onStateUpdateEvent)(String);
  float_t rx_pin_threshold_;
  int rx_pin_;
};

}  // namespace gdoor_esphome
}  // namespace esphome