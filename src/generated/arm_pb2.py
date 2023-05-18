# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tarm.proto\".\n\x0b\x43oordinates\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\x9d\x01\n\tMotorData\x12\x11\n\tis_moving\x18\x01 \x01(\x08\x12\x1f\n\x17is_limit_switch_pressed\x18\x02 \x01(\x08\x12\"\n\tdirection\x18\x03 \x01(\x0e\x32\x0f.MotorDirection\x12\x14\n\x0c\x63urrent_step\x18\x04 \x01(\x05\x12\x13\n\x0btarget_step\x18\x05 \x01(\x05\x12\r\n\x05\x61ngle\x18\x06 \x01(\x02\"8\n\x0cMotorCommand\x12\x12\n\nmove_steps\x18\x01 \x01(\x05\x12\x14\n\x0cmove_radians\x18\x02 \x01(\x02\"\xa9\x01\n\x07\x41rmData\x12%\n\x0f\x63urrentPosition\x18\x01 \x01(\x0b\x32\x0c.Coordinates\x12$\n\x0etargetPosition\x18\x02 \x01(\x0b\x32\x0c.Coordinates\x12\x18\n\x04\x62\x61se\x18\x03 \x01(\x0b\x32\n.MotorData\x12\x1c\n\x08shoulder\x18\x04 \x01(\x0b\x32\n.MotorData\x12\x19\n\x05\x65lbow\x18\x05 \x01(\x0b\x32\n.MotorData\"\xe7\x01\n\nArmCommand\x12\x0c\n\x04stop\x18\x01 \x01(\x08\x12\x11\n\tcalibrate\x18\x02 \x01(\x08\x12\x1d\n\x06swivel\x18\x03 \x01(\x0b\x32\r.MotorCommand\x12\x1f\n\x08shoulder\x18\x04 \x01(\x0b\x32\r.MotorCommand\x12\x1c\n\x05\x65lbow\x18\x05 \x01(\x0b\x32\r.MotorCommand\x12#\n\x0cgripper_lift\x18\x06 \x01(\x0b\x32\r.MotorCommand\x12\x0c\n\x04ik_x\x18\x07 \x01(\x02\x12\x0c\n\x04ik_y\x18\x08 \x01(\x02\x12\x0c\n\x04ik_z\x18\t \x01(\x02\x12\x0b\n\x03jab\x18\n \x01(\x08\"^\n\x0bGripperData\x12\x18\n\x04lift\x18\x01 \x01(\x0b\x32\n.MotorData\x12\x1a\n\x06rotate\x18\x02 \x01(\x0b\x32\n.MotorData\x12\x19\n\x05pinch\x18\x03 \x01(\x0b\x32\n.MotorData\"\xb6\x01\n\x0eGripperCommand\x12\x0c\n\x04stop\x18\x01 \x01(\x08\x12\x11\n\tcalibrate\x18\x02 \x01(\x08\x12\x1b\n\x04lift\x18\x03 \x01(\x0b\x32\r.MotorCommand\x12\x1d\n\x06rotate\x18\x04 \x01(\x0b\x32\r.MotorCommand\x12\x1c\n\x05pinch\x18\x05 \x01(\x0b\x32\r.MotorCommand\x12\x0c\n\x04open\x18\x06 \x01(\x08\x12\r\n\x05\x63lose\x18\x07 \x01(\x08\x12\x0c\n\x04spin\x18\x08 \x01(\x08*\xa6\x01\n\x0eMotorDirection\x12\x1d\n\x19MOTOR_DIRECTION_UNDEFINED\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04\x44OWN\x10\x02\x12\x08\n\x04LEFT\x10\x03\x12\t\n\x05RIGHT\x10\x04\x12\r\n\tCLOCKWISE\x10\x05\x12\x15\n\x11\x43OUNTER_CLOCKWISE\x10\x06\x12\x0b\n\x07OPENING\x10\x07\x12\x0b\n\x07\x43LOSING\x10\x08\x12\x0e\n\nNOT_MOVING\x10\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOTORDIRECTION._serialized_start=967
  _MOTORDIRECTION._serialized_end=1133
  _COORDINATES._serialized_start=13
  _COORDINATES._serialized_end=59
  _MOTORDATA._serialized_start=62
  _MOTORDATA._serialized_end=219
  _MOTORCOMMAND._serialized_start=221
  _MOTORCOMMAND._serialized_end=277
  _ARMDATA._serialized_start=280
  _ARMDATA._serialized_end=449
  _ARMCOMMAND._serialized_start=452
  _ARMCOMMAND._serialized_end=683
  _GRIPPERDATA._serialized_start=685
  _GRIPPERDATA._serialized_end=779
  _GRIPPERCOMMAND._serialized_start=782
  _GRIPPERCOMMAND._serialized_end=964
# @@protoc_insertion_point(module_scope)
