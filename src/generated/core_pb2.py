# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncore.proto\"=\n\x07\x43onnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device\x12\x19\n\x08receiver\x18\x02 \x01(\x0e\x32\x07.Device\"%\n\nDisconnect\x12\x17\n\x06sender\x18\x01 \x01(\x0e\x32\x07.Device\"I\n\rUpdateSetting\x12\x1c\n\x06status\x18\x01 \x01(\x0e\x32\x0c.RoverStatus\x12\x1a\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x0b.ProtoColor\"6\n\nProtoColor\x12\x0b\n\x03red\x18\x01 \x01(\x02\x12\r\n\x05green\x18\x02 \x01(\x02\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x02*\xbd\x01\n\x06\x44\x65vice\x12\x14\n\x10\x44\x45VICE_UNDEFINED\x10\x00\x12\r\n\tDASHBOARD\x10\x01\x12\x0e\n\nSUBSYSTEMS\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\x0c\n\x08\x41UTONOMY\x10\x04\x12\x0c\n\x08\x46IRMWARE\x10\x05\x12\x07\n\x03\x41RM\x10\x06\x12\x0b\n\x07GRIPPER\x10\x07\x12\x0b\n\x07SCIENCE\x10\x08\x12\x0e\n\nELECTRICAL\x10\t\x12\t\n\x05\x44RIVE\x10\n\x12\x08\n\x04MARS\x10\x0b\x12\x0f\n\x0bMARS_SERVER\x10\x0c*T\n\x0bRoverStatus\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\n\n\x06MANUAL\x10\x02\x12\x0e\n\nAUTONOMOUS\x10\x03\x12\r\n\tPOWER_OFF\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICE._serialized_start=248
  _DEVICE._serialized_end=437
  _ROVERSTATUS._serialized_start=439
  _ROVERSTATUS._serialized_end=523
  _CONNECT._serialized_start=14
  _CONNECT._serialized_end=75
  _DISCONNECT._serialized_start=77
  _DISCONNECT._serialized_end=114
  _UPDATESETTING._serialized_start=116
  _UPDATESETTING._serialized_end=189
  _PROTOCOLOR._serialized_start=191
  _PROTOCOLOR._serialized_end=245
# @@protoc_insertion_point(module_scope)
