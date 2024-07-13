#pragma once

#include "esphome/core/component.h"
#include "esphome/components/event/event.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorBusMessageButton : public event::Event, public Component {
 public:
  void setup() override;
  void set_parent(GDoor *parent) { this->parent_ = parent; }
 protected:
  GDoor *parent_;
};

}  // namespace gdoor_esphome
}  // namespace esphome