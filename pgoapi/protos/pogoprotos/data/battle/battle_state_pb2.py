# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_state.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/data/battle/battle_state.proto\x12\x16pogoprotos.data.battle*T\n\x0b\x42\x61ttleState\x12\x0f\n\x0bSTATE_UNSET\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07VICTORY\x10\x02\x12\x0c\n\x08\x44\x45\x46\x45\x41TED\x10\x03\x12\r\n\tTIMED_OUT\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BATTLESTATE = _descriptor.EnumDescriptor(
  name='BattleState',
  full_name='pogoprotos.data.battle.BattleState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VICTORY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEATED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=69,
  serialized_end=153,
)
_sym_db.RegisterEnumDescriptor(_BATTLESTATE)

BattleState = enum_type_wrapper.EnumTypeWrapper(_BATTLESTATE)
STATE_UNSET = 0
ACTIVE = 1
VICTORY = 2
DEFEATED = 3
TIMED_OUT = 4


DESCRIPTOR.enum_types_by_name['BattleState'] = _BATTLESTATE


# @@protoc_insertion_point(module_scope)
