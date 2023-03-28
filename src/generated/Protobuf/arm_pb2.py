# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protobuf/arm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12Protobuf/arm.proto\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"D\n\x0bMotorStatus\x12\x11\n\tis_moving\x18\x01 \x01(\x08\x12\r\n\x05\x61ngle\x18\x02 \x01(\x02\x12\x13\n\x0btemperature\x18\x03 \x01(\x02\"\xa9\x01\n\x07\x41rmData\x12\"\n\x0f\x63urrentPosition\x18\x01 \x01(\x0b\x32\t.Position\x12!\n\x0etargetPosition\x18\x02 \x01(\x0b\x32\t.Position\x12\x1a\n\x04\x62\x61se\x18\x03 \x01(\x0b\x32\x0c.MotorStatus\x12\x1e\n\x08shoulder\x18\x04 \x01(\x0b\x32\x0c.MotorStatus\x12\x1b\n\x05\x65lbow\x18\x05 \x01(\x0b\x32\x0c.MotorStatus\"m\n\nArmCommand\x12\x0c\n\x04stop\x18\x01 \x01(\x08\x12\x11\n\tcalibrate\x18\x02 \x01(\x08\x12\x13\n\x0bmove_swivel\x18\x03 \x01(\x02\x12\x15\n\rmove_shoulder\x18\x04 \x01(\x02\x12\x12\n\nmove_elbow\x18\x05 \x01(\x02\"d\n\x0bGripperData\x12\x1c\n\x06rotate\x18\x01 \x01(\x0b\x32\x0c.MotorStatus\x12\x1a\n\x04lift\x18\x02 \x01(\x0b\x32\x0c.MotorStatus\x12\x1b\n\x05pinch\x18\x03 \x01(\x0b\x32\x0c.MotorStatus\"o\n\x0eGripperCommand\x12\x0c\n\x04stop\x18\x01 \x01(\x08\x12\x11\n\tcalibrate\x18\x02 \x01(\x08\x12\x13\n\x0bmove_rotate\x18\x03 \x01(\x02\x12\x11\n\tmove_lift\x18\x04 \x01(\x02\x12\x14\n\x0cmove_gripper\x18\x05 \x01(\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Protobuf.arm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSITION._serialized_start=22
  _POSITION._serialized_end=65
  _MOTORSTATUS._serialized_start=67
  _MOTORSTATUS._serialized_end=135
  _ARMDATA._serialized_start=138
  _ARMDATA._serialized_end=307
  _ARMCOMMAND._serialized_start=309
  _ARMCOMMAND._serialized_end=418
  _GRIPPERDATA._serialized_start=420
  _GRIPPERDATA._serialized_end=520
  _GRIPPERCOMMAND._serialized_start=522
  _GRIPPERCOMMAND._serialized_end=633
# @@protoc_insertion_point(module_scope)
