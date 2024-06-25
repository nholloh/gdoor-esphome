#pragma once

#include "esphome/core/component.h"

namespace esphome {
namespace gdoor_esphome {

class GDoorBusMessageButton_P : public Parented<GDoor> {};

class GDoorLastMessageBusSensor_P : public Parented<GDoor> {};

class GDoorBusEvent_P : public Parented<GDoor> {};

class GDoor : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  void send(String str);
  void registerLastReceived(void (*callback)(String));
  void registerEvent(void (*callback)(String));
 protected:
  void (*onStateUpdateLastReceived)(String);
  void (*onStateUpdateEvent)(String);
};

}  // namespace gdoor_esphome
}  // namespace esphome