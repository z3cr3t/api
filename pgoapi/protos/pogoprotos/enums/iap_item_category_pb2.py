# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/iap_item_category.proto

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
  name='pogoprotos/enums/iap_item_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/enums/iap_item_category.proto\x12\x10pogoprotos.enums*\xad\x01\n\x13HoloIapItemCategory\x12\x15\n\x11IAP_CATEGORY_NONE\x10\x00\x12\x17\n\x13IAP_CATEGORY_BUNDLE\x10\x01\x12\x16\n\x12IAP_CATEGORY_ITEMS\x10\x02\x12\x19\n\x15IAP_CATEGORY_UPGRADES\x10\x03\x12\x1a\n\x16IAP_CATEGORY_POKECOINS\x10\x04\x12\x17\n\x13IAP_CATEGORY_AVATAR\x10\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_HOLOIAPITEMCATEGORY = _descriptor.EnumDescriptor(
  name='HoloIapItemCategory',
  full_name='pogoprotos.enums.HoloIapItemCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_BUNDLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_ITEMS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_UPGRADES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_POKECOINS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IAP_CATEGORY_AVATAR', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=63,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_HOLOIAPITEMCATEGORY)

HoloIapItemCategory = enum_type_wrapper.EnumTypeWrapper(_HOLOIAPITEMCATEGORY)
IAP_CATEGORY_NONE = 0
IAP_CATEGORY_BUNDLE = 1
IAP_CATEGORY_ITEMS = 2
IAP_CATEGORY_UPGRADES = 3
IAP_CATEGORY_POKECOINS = 4
IAP_CATEGORY_AVATAR = 5


DESCRIPTOR.enum_types_by_name['HoloIapItemCategory'] = _HOLOIAPITEMCATEGORY


# @@protoc_insertion_point(module_scope)
