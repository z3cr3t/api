# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/daily_quest.proto

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
  name='pogoprotos/data/quests/daily_quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/data/quests/daily_quest.proto\x12\x16pogoprotos.data.quests\"I\n\nDailyQuest\x12\x1d\n\x15\x63urrent_period_bucket\x18\x01 \x01(\x05\x12\x1c\n\x14\x63urrent_streak_count\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DAILYQUEST = _descriptor.Descriptor(
  name='DailyQuest',
  full_name='pogoprotos.data.quests.DailyQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_period_bucket', full_name='pogoprotos.data.quests.DailyQuest.current_period_bucket', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_streak_count', full_name='pogoprotos.data.quests.DailyQuest.current_streak_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=68,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['DailyQuest'] = _DAILYQUEST

DailyQuest = _reflection.GeneratedProtocolMessageType('DailyQuest', (_message.Message,), dict(
  DESCRIPTOR = _DAILYQUEST,
  __module__ = 'pogoprotos.data.quests.daily_quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.DailyQuest)
  ))
_sym_db.RegisterMessage(DailyQuest)


# @@protoc_insertion_point(module_scope)
