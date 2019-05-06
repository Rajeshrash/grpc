# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\"\x18\n\x07Welcome\x12\r\n\x05hello\x18\x01 \x01(\t29\n\x0fWelcome_Message\x12&\n\x0eWelcomeMessage\x12\x08.Welcome\x1a\x08.Welcome\"\x00\x32.\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x32\x31\n\rCalculatorNew\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x62\x06proto3')
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=20,
  serialized_end=43,
)


_WELCOME = _descriptor.Descriptor(
  name='Welcome',
  full_name='Welcome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='Welcome.hello', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=45,
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['Welcome'] = _WELCOME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), dict(
  DESCRIPTOR = _NUMBER,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  ))
_sym_db.RegisterMessage(Number)

Welcome = _reflection.GeneratedProtocolMessageType('Welcome', (_message.Message,), dict(
  DESCRIPTOR = _WELCOME,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Welcome)
  ))
_sym_db.RegisterMessage(Welcome)



_WELCOME_MESSAGE = _descriptor.ServiceDescriptor(
  name='Welcome_Message',
  full_name='Welcome_Message',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=71,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='WelcomeMessage',
    full_name='Welcome_Message.WelcomeMessage',
    index=0,
    containing_service=None,
    input_type=_WELCOME,
    output_type=_WELCOME,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WELCOME_MESSAGE)

DESCRIPTOR.services_by_name['Welcome_Message'] = _WELCOME_MESSAGE


_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=130,
  serialized_end=176,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR


_CALCULATORNEW = _descriptor.ServiceDescriptor(
  name='CalculatorNew',
  full_name='CalculatorNew',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=178,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='CalculatorNew.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATORNEW)

DESCRIPTOR.services_by_name['CalculatorNew'] = _CALCULATORNEW

# @@protoc_insertion_point(module_scope)