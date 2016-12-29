# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/global_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import fort_settings_pb2 as pogoprotos_dot_settings_dot_fort__settings__pb2
from pogoprotos.settings import map_settings_pb2 as pogoprotos_dot_settings_dot_map__settings__pb2
from pogoprotos.settings import level_settings_pb2 as pogoprotos_dot_settings_dot_level__settings__pb2
from pogoprotos.settings import inventory_settings_pb2 as pogoprotos_dot_settings_dot_inventory__settings__pb2
from pogoprotos.settings import gps_settings_pb2 as pogoprotos_dot_settings_dot_gps__settings__pb2
from pogoprotos.settings import festival_settings_pb2 as pogoprotos_dot_settings_dot_festival__settings__pb2
from pogoprotos.settings import event_settings_pb2 as pogoprotos_dot_settings_dot_event__settings__pb2
from pogoprotos.settings import sfida_settings_pb2 as pogoprotos_dot_settings_dot_sfida__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/settings/global_settings.proto\x12\x13pogoprotos.settings\x1a\'pogoprotos/settings/fort_settings.proto\x1a&pogoprotos/settings/map_settings.proto\x1a(pogoprotos/settings/level_settings.proto\x1a,pogoprotos/settings/inventory_settings.proto\x1a&pogoprotos/settings/gps_settings.proto\x1a+pogoprotos/settings/festival_settings.proto\x1a(pogoprotos/settings/event_settings.proto\x1a(pogoprotos/settings/sfida_settings.proto\"\xaf\x04\n\x0eGlobalSettings\x12\x38\n\rfort_settings\x18\x02 \x01(\x0b\x32!.pogoprotos.settings.FortSettings\x12\x36\n\x0cmap_settings\x18\x03 \x01(\x0b\x32 .pogoprotos.settings.MapSettings\x12:\n\x0elevel_settings\x18\x04 \x01(\x0b\x32\".pogoprotos.settings.LevelSettings\x12\x42\n\x12inventory_settings\x18\x05 \x01(\x0b\x32&.pogoprotos.settings.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\t\x12\x36\n\x0cgps_settings\x18\x07 \x01(\x0b\x32 .pogoprotos.settings.GpsSettings\x12@\n\x11\x66\x65stival_settings\x18\x08 \x01(\x0b\x32%.pogoprotos.settings.FestivalSettings\x12:\n\x0e\x65vent_settings\x18\t \x01(\x0b\x32\".pogoprotos.settings.EventSettings\x12\x19\n\x11max_pokemon_types\x18\n \x01(\x05\x12:\n\x0esfida_settings\x18\x0b \x01(\x0b\x32\".pogoprotos.settings.SfidaSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_fort__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_map__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_level__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_inventory__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_gps__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_festival__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_event__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_sfida__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='pogoprotos.settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_settings', full_name='pogoprotos.settings.GlobalSettings.fort_settings', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_settings', full_name='pogoprotos.settings.GlobalSettings.map_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_settings', full_name='pogoprotos.settings.GlobalSettings.level_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_settings', full_name='pogoprotos.settings.GlobalSettings.inventory_settings', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='pogoprotos.settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_settings', full_name='pogoprotos.settings.GlobalSettings.gps_settings', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='festival_settings', full_name='pogoprotos.settings.GlobalSettings.festival_settings', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_settings', full_name='pogoprotos.settings.GlobalSettings.event_settings', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_pokemon_types', full_name='pogoprotos.settings.GlobalSettings.max_pokemon_types', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfida_settings', full_name='pogoprotos.settings.GlobalSettings.sfida_settings', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=405,
  serialized_end=964,
)

_GLOBALSETTINGS.fields_by_name['fort_settings'].message_type = pogoprotos_dot_settings_dot_fort__settings__pb2._FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map_settings'].message_type = pogoprotos_dot_settings_dot_map__settings__pb2._MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level_settings'].message_type = pogoprotos_dot_settings_dot_level__settings__pb2._LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory_settings'].message_type = pogoprotos_dot_settings_dot_inventory__settings__pb2._INVENTORYSETTINGS
_GLOBALSETTINGS.fields_by_name['gps_settings'].message_type = pogoprotos_dot_settings_dot_gps__settings__pb2._GPSSETTINGS
_GLOBALSETTINGS.fields_by_name['festival_settings'].message_type = pogoprotos_dot_settings_dot_festival__settings__pb2._FESTIVALSETTINGS
_GLOBALSETTINGS.fields_by_name['event_settings'].message_type = pogoprotos_dot_settings_dot_event__settings__pb2._EVENTSETTINGS
_GLOBALSETTINGS.fields_by_name['sfida_settings'].message_type = pogoprotos_dot_settings_dot_sfida__settings__pb2._SFIDASETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)
