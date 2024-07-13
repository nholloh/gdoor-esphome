#pragma once

#include "esphome/core/component.h"
#include "esphome/components/button/button.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorBusMessageButton : public button::Button, public Component {
 public:
  void setup() override;
  void press() override;
  void dump_config() override;
  void set_parent(GDoor *parent) { this->parent_ = parent; }
  void set_button_busmessage(String *button_busmessage) { this->button_busmessage_ = button_busmessage; }
 protected:
  String *button_busmessage_;
  GDoor *parent_;
};

}  // namespace gdoor_esphome
}  // namespace esphome