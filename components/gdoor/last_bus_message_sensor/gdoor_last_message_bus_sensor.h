#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorLastMessageBusSensor : public text_sensor::TextSensor, public Component {
 public:
  void setup() override;
  void set_parent(GDoor *parent) { this->parent_ = parent; }
 protected:
  GDoor *parent_;
};

}  // namespace gdoor_esphome
}  // namespace esphome