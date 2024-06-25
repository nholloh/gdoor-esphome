#pragma once

#include "esphome/core/component.h"
#include "esphome/components/event/event.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorBusMessageButton : public GDoorBusEvent_P, public event::Event, public Component {
 public:
  void setup() override;
};

}  // namespace gdoor_esphome
}  // namespace esphome