# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_pokemon_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_pokemon_info.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/data/battle/battle_pokemon_info.proto\x12\x16pogoprotos.data.battle\x1a\"pogoprotos/data/pokemon_data.proto\"w\n\x11\x42\x61ttlePokemonInfo\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x16\n\x0e\x63urrent_health\x18\x02 \x01(\x05\x12\x16\n\x0e\x63urrent_energy\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLEPOKEMONINFO = _descriptor.Descriptor(
  name='BattlePokemonInfo',
  full_name='pogoprotos.data.battle.BattlePokemonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='pogoprotos.data.battle.BattlePokemonInfo.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_health', full_name='pogoprotos.data.battle.BattlePokemonInfo.current_health', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_energy', full_name='pogoprotos.data.battle.BattlePokemonInfo.current_energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=112,
  serialized_end=231,
)

_BATTLEPOKEMONINFO.fields_by_name['pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
DESCRIPTOR.message_types_by_name['BattlePokemonInfo'] = _BATTLEPOKEMONINFO

BattlePokemonInfo = _reflection.GeneratedProtocolMessageType('BattlePokemonInfo', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPOKEMONINFO,
  __module__ = 'pogoprotos.data.battle.battle_pokemon_info_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattlePokemonInfo)
  ))
_sym_db.RegisterMessage(BattlePokemonInfo)


# @@protoc_insertion_point(module_scope)
