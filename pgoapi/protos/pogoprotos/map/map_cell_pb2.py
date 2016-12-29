# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/map_cell.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map import spawn_point_pb2 as pogoprotos_dot_map_dot_spawn__point__pb2
from pogoprotos.map.fort import fort_data_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__data__pb2
from pogoprotos.map.fort import fort_summary_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__summary__pb2
from pogoprotos.map.pokemon import nearby_pokemon_pb2 as pogoprotos_dot_map_dot_pokemon_dot_nearby__pokemon__pb2
from pogoprotos.map.pokemon import wild_pokemon_pb2 as pogoprotos_dot_map_dot_pokemon_dot_wild__pokemon__pb2
from pogoprotos.map.pokemon import map_pokemon_pb2 as pogoprotos_dot_map_dot_pokemon_dot_map__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/map_cell.proto',
  package='pogoprotos.map',
  syntax='proto3',
  serialized_pb=_b('\n\x1dpogoprotos/map/map_cell.proto\x12\x0epogoprotos.map\x1a pogoprotos/map/spawn_point.proto\x1a#pogoprotos/map/fort/fort_data.proto\x1a&pogoprotos/map/fort/fort_summary.proto\x1a+pogoprotos/map/pokemon/nearby_pokemon.proto\x1a)pogoprotos/map/pokemon/wild_pokemon.proto\x1a(pogoprotos/map/pokemon/map_pokemon.proto\"\x81\x04\n\x07MapCell\x12\x12\n\ns2_cell_id\x18\x01 \x01(\x04\x12\x1c\n\x14\x63urrent_timestamp_ms\x18\x02 \x01(\x03\x12,\n\x05\x66orts\x18\x03 \x03(\x0b\x32\x1d.pogoprotos.map.fort.FortData\x12\x30\n\x0cspawn_points\x18\x04 \x03(\x0b\x32\x1a.pogoprotos.map.SpawnPoint\x12\x17\n\x0f\x64\x65leted_objects\x18\x06 \x03(\t\x12\x19\n\x11is_truncated_list\x18\x07 \x01(\x08\x12\x38\n\x0e\x66ort_summaries\x18\x08 \x03(\x0b\x32 .pogoprotos.map.fort.FortSummary\x12:\n\x16\x64\x65\x63imated_spawn_points\x18\t \x03(\x0b\x32\x1a.pogoprotos.map.SpawnPoint\x12:\n\rwild_pokemons\x18\x05 \x03(\x0b\x32#.pogoprotos.map.pokemon.WildPokemon\x12>\n\x12\x63\x61tchable_pokemons\x18\n \x03(\x0b\x32\".pogoprotos.map.pokemon.MapPokemon\x12>\n\x0fnearby_pokemons\x18\x0b \x03(\x0b\x32%.pogoprotos.map.pokemon.NearbyPokemonb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_spawn__point__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_fort_dot_fort__data__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_fort_dot_fort__summary__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_pokemon_dot_nearby__pokemon__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_pokemon_dot_wild__pokemon__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_pokemon_dot_map__pokemon__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAPCELL = _descriptor.Descriptor(
  name='MapCell',
  full_name='pogoprotos.map.MapCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s2_cell_id', full_name='pogoprotos.map.MapCell.s2_cell_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_timestamp_ms', full_name='pogoprotos.map.MapCell.current_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forts', full_name='pogoprotos.map.MapCell.forts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_points', full_name='pogoprotos.map.MapCell.spawn_points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_objects', full_name='pogoprotos.map.MapCell.deleted_objects', index=4,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_truncated_list', full_name='pogoprotos.map.MapCell.is_truncated_list', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_summaries', full_name='pogoprotos.map.MapCell.fort_summaries', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decimated_spawn_points', full_name='pogoprotos.map.MapCell.decimated_spawn_points', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wild_pokemons', full_name='pogoprotos.map.MapCell.wild_pokemons', index=8,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catchable_pokemons', full_name='pogoprotos.map.MapCell.catchable_pokemons', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nearby_pokemons', full_name='pogoprotos.map.MapCell.nearby_pokemons', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=291,
  serialized_end=804,
)

_MAPCELL.fields_by_name['forts'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__data__pb2._FORTDATA
_MAPCELL.fields_by_name['spawn_points'].message_type = pogoprotos_dot_map_dot_spawn__point__pb2._SPAWNPOINT
_MAPCELL.fields_by_name['fort_summaries'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__summary__pb2._FORTSUMMARY
_MAPCELL.fields_by_name['decimated_spawn_points'].message_type = pogoprotos_dot_map_dot_spawn__point__pb2._SPAWNPOINT
_MAPCELL.fields_by_name['wild_pokemons'].message_type = pogoprotos_dot_map_dot_pokemon_dot_wild__pokemon__pb2._WILDPOKEMON
_MAPCELL.fields_by_name['catchable_pokemons'].message_type = pogoprotos_dot_map_dot_pokemon_dot_map__pokemon__pb2._MAPPOKEMON
_MAPCELL.fields_by_name['nearby_pokemons'].message_type = pogoprotos_dot_map_dot_pokemon_dot_nearby__pokemon__pb2._NEARBYPOKEMON
DESCRIPTOR.message_types_by_name['MapCell'] = _MAPCELL

MapCell = _reflection.GeneratedProtocolMessageType('MapCell', (_message.Message,), dict(
  DESCRIPTOR = _MAPCELL,
  __module__ = 'pogoprotos.map.map_cell_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.MapCell)
  ))
_sym_db.RegisterMessage(MapCell)


# @@protoc_insertion_point(module_scope)
