# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: video.proto
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
    'video.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import version_pb2 as version__pb2
from . import vision_pb2 as vision__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bvideo.proto\x1a\rversion.proto\x1a\x0cvision.proto\"\xd8\x02\n\rCameraDetails\x12\x19\n\x04name\x18\x01 \x01(\x0e\x32\x0b.CameraName\x12\x18\n\x10resolution_width\x18\x02 \x01(\x05\x12\x19\n\x11resolution_height\x18\x03 \x01(\x05\x12\x0f\n\x07quality\x18\x04 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x05 \x01(\x05\x12\x1d\n\x06status\x18\x06 \x01(\x0e\x32\r.CameraStatus\x12\x11\n\tautofocus\x18\x07 \x01(\x08\x12\x0c\n\x04zoom\x18\x08 \x01(\x05\x12\x0b\n\x03pan\x18\t \x01(\x05\x12\x0c\n\x04tilt\x18\n \x01(\x05\x12\r\n\x05\x66ocus\x18\x0b \x01(\x05\x12\x14\n\x0c\x64iagonal_fov\x18\x0c \x01(\x02\x12\x16\n\x0ehorizontal_fov\x18\r \x01(\x02\x12\x14\n\x0cvertical_fov\x18\x0e \x01(\x02\x12\x14\n\x0cstream_width\x18\x0f \x01(\x05\x12\x15\n\rstream_height\x18\x10 \x01(\x05\"\x9f\x01\n\tVideoData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x0e.CameraDetails\x12\r\n\x05\x66rame\x18\x03 \x01(\x0c\x12\x19\n\x07version\x18\x04 \x01(\x0b\x32\x08.Version\x12\x11\n\timagePath\x18\x05 \x01(\t\x12(\n\x0f\x64\x65tectedObjects\x18\x06 \x03(\x0b\x32\x0f.DetectedObject\"l\n\x0cVideoCommand\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x0e.CameraDetails\x12\x19\n\x07version\x18\x03 \x01(\x0b\x32\x08.Version\x12\x14\n\x0ctakeSnapshot\x18\x04 \x01(\x08*\xc9\x01\n\x0c\x43\x61meraStatus\x12\x1b\n\x17\x43\x41MERA_STATUS_UNDEFINED\x10\x00\x12\x17\n\x13\x43\x41MERA_DISCONNECTED\x10\x01\x12\x12\n\x0e\x43\x41MERA_ENABLED\x10\x02\x12\x13\n\x0f\x43\x41MERA_DISABLED\x10\x03\x12\x19\n\x15\x43\x41MERA_NOT_RESPONDING\x10\x04\x12\x12\n\x0e\x43\x41MERA_LOADING\x10\x05\x12\x13\n\x0f\x46RAME_TOO_LARGE\x10\x06\x12\x16\n\x12\x43\x41MERA_HAS_NO_NAME\x10\x07*\xaf\x01\n\nCameraName\x12\x19\n\x15\x43\x41MERA_NAME_UNDEFINED\x10\x00\x12\x0f\n\x0bROVER_FRONT\x10\x01\x12\x0e\n\nROVER_REAR\x10\x02\x12\x12\n\x0e\x41UTONOMY_DEPTH\x10\x03\x12\x0e\n\nSUBSYSTEM1\x10\x04\x12\x0e\n\nSUBSYSTEM2\x10\x05\x12\x0e\n\nSUBSYSTEM3\x10\x06\x12\x0f\n\x0b\x42OTTOM_LEFT\x10\x07\x12\x10\n\x0c\x42OTTOM_RIGHT\x10\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CAMERASTATUS']._serialized_start=664
  _globals['_CAMERASTATUS']._serialized_end=865
  _globals['_CAMERANAME']._serialized_start=868
  _globals['_CAMERANAME']._serialized_end=1043
  _globals['_CAMERADETAILS']._serialized_start=45
  _globals['_CAMERADETAILS']._serialized_end=389
  _globals['_VIDEODATA']._serialized_start=392
  _globals['_VIDEODATA']._serialized_end=551
  _globals['_VIDEOCOMMAND']._serialized_start=553
  _globals['_VIDEOCOMMAND']._serialized_end=661
# @@protoc_insertion_point(module_scope)
