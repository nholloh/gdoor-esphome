#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorLastMessageBusSensor : public GDoorLastMessageBusSensor_P, public text_sensor::TextSensor, public Component {
 public:
  void setup() override;
};

}  // namespace gdoor_esphome
}  // namespace esphome