# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/download_settings_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/download_settings_action.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/settings/download_settings_action.proto\x12\x13pogoprotos.settings\"&\n\x16\x44ownloadSettingsAction\x12\x0c\n\x04hash\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADSETTINGSACTION = _descriptor.Descriptor(
  name='DownloadSettingsAction',
  full_name='pogoprotos.settings.DownloadSettingsAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='pogoprotos.settings.DownloadSettingsAction.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['DownloadSettingsAction'] = _DOWNLOADSETTINGSACTION

DownloadSettingsAction = _reflection.GeneratedProtocolMessageType('DownloadSettingsAction', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSACTION,
  __module__ = 'pogoprotos.settings.download_settings_action_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.DownloadSettingsAction)
  ))
_sym_db.RegisterMessage(DownloadSettingsAction)


# @@protoc_insertion_point(module_scope)
