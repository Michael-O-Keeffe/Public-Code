# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: line.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='line.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nline.proto\"\x16\n\x05Lines\x12\r\n\x05lines\x18\x01 \x01(\t\" \n\x0c\x43heckReponse\x12\x10\n\x08received\x18\x01 \x01(\t24\n\x0eGetLineService\x12\"\n\x07GetLine\x12\x06.Lines\x1a\r.CheckReponse\"\x00\x62\x06proto3'
)




_LINES = _descriptor.Descriptor(
  name='Lines',
  full_name='Lines',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lines', full_name='Lines.lines', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=36,
)


_CHECKREPONSE = _descriptor.Descriptor(
  name='CheckReponse',
  full_name='CheckReponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='received', full_name='CheckReponse.received', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['Lines'] = _LINES
DESCRIPTOR.message_types_by_name['CheckReponse'] = _CHECKREPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lines = _reflection.GeneratedProtocolMessageType('Lines', (_message.Message,), {
  'DESCRIPTOR' : _LINES,
  '__module__' : 'line_pb2'
  # @@protoc_insertion_point(class_scope:Lines)
  })
_sym_db.RegisterMessage(Lines)

CheckReponse = _reflection.GeneratedProtocolMessageType('CheckReponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREPONSE,
  '__module__' : 'line_pb2'
  # @@protoc_insertion_point(class_scope:CheckReponse)
  })
_sym_db.RegisterMessage(CheckReponse)



_GETLINESERVICE = _descriptor.ServiceDescriptor(
  name='GetLineService',
  full_name='GetLineService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=72,
  serialized_end=124,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLine',
    full_name='GetLineService.GetLine',
    index=0,
    containing_service=None,
    input_type=_LINES,
    output_type=_CHECKREPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETLINESERVICE)

DESCRIPTOR.services_by_name['GetLineService'] = _GETLINESERVICE

# @@protoc_insertion_point(module_scope)
