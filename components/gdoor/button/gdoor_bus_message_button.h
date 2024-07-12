#pragma once

#include "esphome/core/component.h"
#include "esphome/components/button/button.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorBusMessageButton : public GDoorBusMessageButton_P, public button::Button, public Component {
 public:
  void setup() override;
  void press() override;
  void dump_config() override;
 protected:
  String *button_busmessage_;
};

}  // namespace gdoor_esphome
}  // namespace esphome