# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncore.proto\"=\n\x07\x43onnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device\x12\x19\n\x08receiver\x18\x02 \x01(\x0e\x32\x07.Device\"%\n\nDisconnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device*\x92\x01\n\x06\x44\x65vice\x12\x14\n\x10\x44\x45VICE_UNDEFINED\x10\x00\x12\r\n\tDASHBOARD\x10\x01\x12\x0e\n\nSUBSYSTEMS\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\x0c\n\x08\x41UTONOMY\x10\x04\x12\x0c\n\x08\x46IRMWARE\x10\x05\x12\x07\n\x03\x41RM\x10\x06\x12\x0b\n\x07GRIPPER\x10\x07\x12\x0b\n\x07SCIENCE\x10\x08\x12\t\n\x05\x44RIVE\x10\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DEVICE']._serialized_start=117
  _globals['_DEVICE']._serialized_end=263
  _globals['_CONNECT']._serialized_start=14
  _globals['_CONNECT']._serialized_end=75
  _globals['_DISCONNECT']._serialized_start=77
  _globals['_DISCONNECT']._serialized_end=114
# @@protoc_insertion_point(module_scope)
