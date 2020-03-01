# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exemplo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exemplo.proto',
  package='nameko',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rexemplo.proto\x12\x06nameko\"3\n\x0e\x45xampleRequest\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\nmultiplier\x18\x02 \x01(\x05\".\n\x0c\x45xampleReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05seqno\x18\x02 \x01(\x05\x32\x91\x02\n\x07\x65xample\x12=\n\x0bunary_unary\x12\x16.nameko.ExampleRequest\x1a\x14.nameko.ExampleReply\"\x00\x12@\n\x0cunary_stream\x12\x16.nameko.ExampleRequest\x1a\x14.nameko.ExampleReply\"\x00\x30\x01\x12@\n\x0cstream_unary\x12\x16.nameko.ExampleRequest\x1a\x14.nameko.ExampleReply\"\x00(\x01\x12\x43\n\rstream_stream\x12\x16.nameko.ExampleRequest\x1a\x14.nameko.ExampleReply\"\x00(\x01\x30\x01\x62\x06proto3'
)




_EXAMPLEREQUEST = _descriptor.Descriptor(
  name='ExampleRequest',
  full_name='nameko.ExampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='nameko.ExampleRequest.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='nameko.ExampleRequest.multiplier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=25,
  serialized_end=76,
)


_EXAMPLEREPLY = _descriptor.Descriptor(
  name='ExampleReply',
  full_name='nameko.ExampleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='nameko.ExampleReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqno', full_name='nameko.ExampleReply.seqno', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=78,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['ExampleRequest'] = _EXAMPLEREQUEST
DESCRIPTOR.message_types_by_name['ExampleReply'] = _EXAMPLEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExampleRequest = _reflection.GeneratedProtocolMessageType('ExampleRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEREQUEST,
  '__module__' : 'exemplo_pb2'
  # @@protoc_insertion_point(class_scope:nameko.ExampleRequest)
  })
_sym_db.RegisterMessage(ExampleRequest)

ExampleReply = _reflection.GeneratedProtocolMessageType('ExampleReply', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEREPLY,
  '__module__' : 'exemplo_pb2'
  # @@protoc_insertion_point(class_scope:nameko.ExampleReply)
  })
_sym_db.RegisterMessage(ExampleReply)



_EXAMPLE = _descriptor.ServiceDescriptor(
  name='example',
  full_name='nameko.example',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=127,
  serialized_end=400,
  methods=[
  _descriptor.MethodDescriptor(
    name='unary_unary',
    full_name='nameko.example.unary_unary',
    index=0,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unary_stream',
    full_name='nameko.example.unary_stream',
    index=1,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stream_unary',
    full_name='nameko.example.stream_unary',
    index=2,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stream_stream',
    full_name='nameko.example.stream_stream',
    index=3,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXAMPLE)

DESCRIPTOR.services_by_name['example'] = _EXAMPLE

# @@protoc_insertion_point(module_scope)
