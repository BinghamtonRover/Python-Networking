# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gps.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tgps.proto\"G\n\x0eGpsCoordinates\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x02\".\n\x0bOrientation\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"P\n\rRoverPosition\x12\x1c\n\x03gps\x18\x01 \x01(\x0b\x32\x0f.GpsCoordinates\x12!\n\x0borientation\x18\x02 \x01(\x0b\x32\x0c.Orientationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gps_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GPSCOORDINATES']._serialized_start=13
  _globals['_GPSCOORDINATES']._serialized_end=84
  _globals['_ORIENTATION']._serialized_start=86
  _globals['_ORIENTATION']._serialized_end=132
  _globals['_ROVERPOSITION']._serialized_start=134
  _globals['_ROVERPOSITION']._serialized_end=214
# @@protoc_insertion_point(module_scope)
