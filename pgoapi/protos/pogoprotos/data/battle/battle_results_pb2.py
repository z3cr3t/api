# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_results.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.gym import gym_state_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__state__pb2
from pogoprotos.data.battle import battle_participant_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_results.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n+pogoprotos/data/battle/battle_results.proto\x12\x16pogoprotos.data.battle\x1a#pogoprotos/data/gym/gym_state.proto\x1a/pogoprotos/data/battle/battle_participant.proto\"\xde\x01\n\rBattleResults\x12\x30\n\tgym_state\x18\x01 \x01(\x0b\x32\x1d.pogoprotos.data.gym.GymState\x12<\n\tattackers\x18\x02 \x03(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12!\n\x19player_experience_awarded\x18\x03 \x03(\x05\x12 \n\x18next_defender_pokemon_id\x18\x04 \x01(\x03\x12\x18\n\x10gym_points_delta\x18\x05 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_gym_dot_gym__state__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLERESULTS = _descriptor.Descriptor(
  name='BattleResults',
  full_name='pogoprotos.data.battle.BattleResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_state', full_name='pogoprotos.data.battle.BattleResults.gym_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackers', full_name='pogoprotos.data.battle.BattleResults.attackers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_experience_awarded', full_name='pogoprotos.data.battle.BattleResults.player_experience_awarded', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_defender_pokemon_id', full_name='pogoprotos.data.battle.BattleResults.next_defender_pokemon_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_points_delta', full_name='pogoprotos.data.battle.BattleResults.gym_points_delta', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=158,
  serialized_end=380,
)

_BATTLERESULTS.fields_by_name['gym_state'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__state__pb2._GYMSTATE
_BATTLERESULTS.fields_by_name['attackers'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
DESCRIPTOR.message_types_by_name['BattleResults'] = _BATTLERESULTS

BattleResults = _reflection.GeneratedProtocolMessageType('BattleResults', (_message.Message,), dict(
  DESCRIPTOR = _BATTLERESULTS,
  __module__ = 'pogoprotos.data.battle.battle_results_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattleResults)
  ))
_sym_db.RegisterMessage(BattleResults)


# @@protoc_insertion_point(module_scope)
