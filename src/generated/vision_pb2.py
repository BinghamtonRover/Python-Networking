# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vision.proto
# Protobuf Python Version: 6.30.0-rc1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '-rc1',
    'vision.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cvision.proto\x1a\x0egeometry.proto\"1\n\tPnpResult\x12\x15\n\x04pose\x18\x01 \x01(\x0b\x32\x07.Pose3d\x12\r\n\x05\x65rror\x18\x02 \x01(\x01\"\xdd\x01\n\x0e\x44\x65tectedObject\x12\'\n\nobjectType\x18\x01 \x01(\x0e\x32\x13.DetectedObjectType\x12\x12\n\narucoTagId\x18\x02 \x01(\x05\x12\x11\n\txPosition\x18\x04 \x01(\x02\x12\x14\n\x0crelativeSize\x18\x05 \x01(\x02\x12\x0b\n\x03yaw\x18\x06 \x01(\x02\x12\r\n\x05pitch\x18\x07 \x01(\x02\x12!\n\rbestPnpResult\x18\x08 \x01(\x0b\x32\n.PnpResult\x12&\n\x12\x61lternatePnpResult\x18\t \x01(\x0b\x32\n.PnpResult*U\n\x12\x44\x65tectedObjectType\x12\x1c\n\x18\x44\x45TECTION_TYPE_UNDEFINED\x10\x00\x12\t\n\x05\x41RUCO\x10\x01\x12\n\n\x06HAMMER\x10\x02\x12\n\n\x06\x42OTTLE\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vision_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DETECTEDOBJECTTYPE']._serialized_start=307
  _globals['_DETECTEDOBJECTTYPE']._serialized_end=392
  _globals['_PNPRESULT']._serialized_start=32
  _globals['_PNPRESULT']._serialized_end=81
  _globals['_DETECTEDOBJECT']._serialized_start=84
  _globals['_DETECTEDOBJECT']._serialized_end=305
# @@protoc_insertion_point(module_scope)
