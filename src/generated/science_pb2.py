# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: science.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rscience.proto\"\x93\x03\n\x0eScienceCommand\x12\x15\n\rdirt_carousel\x18\x01 \x01(\x02\x12\x13\n\x0b\x64irt_linear\x18\x02 \x01(\x02\x12\x16\n\x0escience_linear\x18\x03 \x01(\x02\x12\x15\n\rvacuum_linear\x18\x04 \x01(\x02\x12\x1a\n\x06vacuum\x18\x05 \x01(\x0e\x32\n.PumpState\x12&\n\x0b\x64irtRelease\x18\x07 \x01(\x0e\x32\x11.DirtReleaseState\x12\x19\n\x05pump1\x18\x08 \x01(\x0e\x32\n.PumpState\x12\x19\n\x05pump2\x18\t \x01(\x0e\x32\n.PumpState\x12\x19\n\x05pump3\x18\n \x01(\x0e\x32\n.PumpState\x12\x19\n\x05pump4\x18\x0b \x01(\x0e\x32\n.PumpState\x12\x11\n\tcalibrate\x18\x0c \x01(\x08\x12\x0c\n\x04stop\x18\r \x01(\x08\x12\x11\n\tnext_tube\x18\x0e \x01(\x08\x12\x14\n\x0cnext_section\x18\x0f \x01(\x08\x12\x0e\n\x06sample\x18\x10 \x01(\x05\x12\x1c\n\x05state\x18\x11 \x01(\x0e\x32\r.ScienceState\"\x8c\x01\n\x0bScienceData\x12\x0b\n\x03\x63o2\x18\x01 \x01(\x02\x12\x10\n\x08humidity\x18\x02 \x01(\x02\x12\x0f\n\x07methane\x18\x03 \x01(\x02\x12\n\n\x02pH\x18\x04 \x01(\x02\x12\x13\n\x0btemperature\x18\x05 \x01(\x02\x12\x0e\n\x06sample\x18\x06 \x01(\x05\x12\x1c\n\x05state\x18\x07 \x01(\x0e\x32\r.ScienceState*@\n\tPumpState\x12\x18\n\x14PUMP_STATE_UNDEFINED\x10\x00\x12\x0b\n\x07PUMP_ON\x10\x01\x12\x0c\n\x08PUMP_OFF\x10\x02*S\n\x10\x44irtReleaseState\x12 \n\x1c\x44IRT_RELEASE_STATE_UNDEFINED\x10\x00\x12\r\n\tOPEN_DIRT\x10\x01\x12\x0e\n\nCLOSE_DIRT\x10\x02*R\n\x0cScienceState\x12\x1b\n\x17SCIENCE_STATE_UNDEFINED\x10\x00\x12\x10\n\x0c\x43OLLECT_DATA\x10\x01\x12\x13\n\x0fSTOP_COLLECTING\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'science_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUMPSTATE._serialized_start=566
  _PUMPSTATE._serialized_end=630
  _DIRTRELEASESTATE._serialized_start=632
  _DIRTRELEASESTATE._serialized_end=715
  _SCIENCESTATE._serialized_start=717
  _SCIENCESTATE._serialized_end=799
  _SCIENCECOMMAND._serialized_start=18
  _SCIENCECOMMAND._serialized_end=421
  _SCIENCEDATA._serialized_start=424
  _SCIENCEDATA._serialized_end=564
# @@protoc_insertion_point(module_scope)
