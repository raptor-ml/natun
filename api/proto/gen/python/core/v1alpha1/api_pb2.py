# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/v1alpha1/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from core.v1alpha1 import types_pb2 as core_dot_v1alpha1_dot_types__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63ore/v1alpha1/api.proto\x12\rcore.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63ore/v1alpha1/types.proto\x1a\x17validate/validate.proto\"\x8e\x03\n\nGetRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\xef\x01\n\x08selector\x18\x02 \x01(\tB\xd2\x01\xfa\x42\xce\x01r\xcb\x01\x32\xc8\x01(?si)^((?P<namespace>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})\\.)?(?P<name>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})(\\+(?P<aggrFn>([a-z]+_*[a-z]+)))?(@-(?P<version>([0-9]+)))?(\\[(?P<encoding>([a-z]+_*[a-z]+))])?$R\x08selector\x12\x37\n\x04keys\x18\x03 \x03(\x0b\x32#.core.v1alpha1.GetRequest.KeysEntryR\x04keys\x1a\x37\n\tKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xaf\x01\n\x0bGetResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.core.v1alpha1.FeatureValueR\x05value\x12O\n\x12\x66\x65\x61ture_descriptor\x18\x03 \x01(\x0b\x32 .core.v1alpha1.FeatureDescriptorR\x11\x66\x65\x61tureDescriptor\"\xcc\x02\n\nSetRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12H\n\x08selector\x18\x02 \x01(\tB,\xfa\x42)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$R\x08selector\x12\x37\n\x04keys\x18\x03 \x03(\x0b\x32#.core.v1alpha1.SetRequest.KeysEntryR\x04keys\x12*\n\x05value\x18\x04 \x01(\x0b\x32\x14.core.v1alpha1.ValueR\x05value\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a\x37\n\tKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"e\n\x0bSetResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\xc9\x02\n\rAppendRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12>\n\x03\x66qn\x18\x02 \x01(\tB,\xfa\x42)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$R\x03\x66qn\x12:\n\x04keys\x18\x03 \x03(\x0b\x32&.core.v1alpha1.AppendRequest.KeysEntryR\x04keys\x12+\n\x05value\x18\x04 \x01(\x0b\x32\x15.core.v1alpha1.ScalarR\x05value\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a\x37\n\tKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"h\n\x0e\x41ppendResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\xc5\x02\n\x0bIncrRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12>\n\x03\x66qn\x18\x02 \x01(\tB,\xfa\x42)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$R\x03\x66qn\x12\x38\n\x04keys\x18\x03 \x03(\x0b\x32$.core.v1alpha1.IncrRequest.KeysEntryR\x04keys\x12+\n\x05value\x18\x04 \x01(\x0b\x32\x15.core.v1alpha1.ScalarR\x05value\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a\x37\n\tKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"f\n\x0cIncrResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\xd2\x02\n\rUpdateRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12H\n\x08selector\x18\x02 \x01(\tB,\xfa\x42)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$R\x08selector\x12:\n\x04keys\x18\x03 \x03(\x0b\x32&.core.v1alpha1.UpdateRequest.KeysEntryR\x04keys\x12*\n\x05value\x18\x04 \x01(\x0b\x32\x14.core.v1alpha1.ValueR\x05value\x12\x38\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a\x37\n\tKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"h\n\x0eUpdateResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\xaa\x02\n\x18\x46\x65\x61tureDescriptorRequest\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12\xef\x01\n\x08selector\x18\x02 \x01(\tB\xd2\x01\xfa\x42\xce\x01r\xcb\x01\x32\xc8\x01(?si)^((?P<namespace>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})\\.)?(?P<name>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})(\\+(?P<aggrFn>([a-z]+_*[a-z]+)))?(@-(?P<version>([0-9]+)))?(\\[(?P<encoding>([a-z]+_*[a-z]+))])?$R\x08selector\"\x8a\x01\n\x19\x46\x65\x61tureDescriptorResponse\x12\x1c\n\x04uuid\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01R\x04uuid\x12O\n\x12\x66\x65\x61ture_descriptor\x18\x02 \x01(\x0b\x32 .core.v1alpha1.FeatureDescriptorR\x11\x66\x65\x61tureDescriptor2\xcb\x04\n\rEngineService\x12\x83\x01\n\x11\x46\x65\x61tureDescriptor\x12\'.core.v1alpha1.FeatureDescriptorRequest\x1a(.core.v1alpha1.FeatureDescriptorResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x42\x13\n\x04HEAD\x12\x0b/{selector}\x12Q\n\x03Get\x12\x19.core.v1alpha1.GetRequest\x1a\x1a.core.v1alpha1.GetResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/{selector}\x12Q\n\x03Set\x12\x19.core.v1alpha1.SetRequest\x1a\x1a.core.v1alpha1.SetResponse\"\x13\x82\xd3\xe4\x93\x02\r\x1a\x0b/{selector}\x12\\\n\x06\x41ppend\x12\x1c.core.v1alpha1.AppendRequest\x1a\x1d.core.v1alpha1.AppendResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/{fqn}/append\x12T\n\x04Incr\x12\x1a.core.v1alpha1.IncrRequest\x1a\x1b.core.v1alpha1.IncrResponse\"\x13\x82\xd3\xe4\x93\x02\r\"\x0b/{fqn}/incr\x12Z\n\x06Update\x12\x1c.core.v1alpha1.UpdateRequest\x1a\x1d.core.v1alpha1.UpdateResponse\"\x13\x82\xd3\xe4\x93\x02\r\"\x0b/{selector}B\xbb\x01\n\x11\x63om.core.v1alpha1B\x08\x41piProtoP\x01ZGgithub.com/raptor-ml/raptor/api/proto/gen/go/core/v1alpha1;corev1alpha1\xa2\x02\x03\x43XX\xaa\x02\rCore.V1alpha1\xca\x02\rCore\\V1alpha1\xe2\x02\x19\x43ore\\V1alpha1\\GPBMetadata\xea\x02\x0e\x43ore::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.v1alpha1.api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.core.v1alpha1B\010ApiProtoP\001ZGgithub.com/raptor-ml/raptor/api/proto/gen/go/core/v1alpha1;corev1alpha1\242\002\003CXX\252\002\rCore.V1alpha1\312\002\rCore\\V1alpha1\342\002\031Core\\V1alpha1\\GPBMetadata\352\002\016Core::V1alpha1'
  _GETREQUEST_KEYSENTRY._options = None
  _GETREQUEST_KEYSENTRY._serialized_options = b'8\001'
  _GETREQUEST.fields_by_name['uuid']._options = None
  _GETREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _GETREQUEST.fields_by_name['selector']._options = None
  _GETREQUEST.fields_by_name['selector']._serialized_options = b'\372B\316\001r\313\0012\310\001(?si)^((?P<namespace>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})\\.)?(?P<name>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})(\\+(?P<aggrFn>([a-z]+_*[a-z]+)))?(@-(?P<version>([0-9]+)))?(\\[(?P<encoding>([a-z]+_*[a-z]+))])?$'
  _GETRESPONSE.fields_by_name['uuid']._options = None
  _GETRESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _SETREQUEST_KEYSENTRY._options = None
  _SETREQUEST_KEYSENTRY._serialized_options = b'8\001'
  _SETREQUEST.fields_by_name['uuid']._options = None
  _SETREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _SETREQUEST.fields_by_name['selector']._options = None
  _SETREQUEST.fields_by_name['selector']._serialized_options = b'\372B)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$'
  _SETRESPONSE.fields_by_name['uuid']._options = None
  _SETRESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _APPENDREQUEST_KEYSENTRY._options = None
  _APPENDREQUEST_KEYSENTRY._serialized_options = b'8\001'
  _APPENDREQUEST.fields_by_name['uuid']._options = None
  _APPENDREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _APPENDREQUEST.fields_by_name['fqn']._options = None
  _APPENDREQUEST.fields_by_name['fqn']._serialized_options = b'\372B)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$'
  _APPENDRESPONSE.fields_by_name['uuid']._options = None
  _APPENDRESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _INCRREQUEST_KEYSENTRY._options = None
  _INCRREQUEST_KEYSENTRY._serialized_options = b'8\001'
  _INCRREQUEST.fields_by_name['uuid']._options = None
  _INCRREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _INCRREQUEST.fields_by_name['fqn']._options = None
  _INCRREQUEST.fields_by_name['fqn']._serialized_options = b'\372B)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$'
  _INCRRESPONSE.fields_by_name['uuid']._options = None
  _INCRRESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _UPDATEREQUEST_KEYSENTRY._options = None
  _UPDATEREQUEST_KEYSENTRY._serialized_options = b'8\001'
  _UPDATEREQUEST.fields_by_name['uuid']._options = None
  _UPDATEREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _UPDATEREQUEST.fields_by_name['selector']._options = None
  _UPDATEREQUEST.fields_by_name['selector']._serialized_options = b'\372B)r\'2%(i?)^([a0-z9\\-\\.]*)(\\[([a0-z9])*\\])?$'
  _UPDATERESPONSE.fields_by_name['uuid']._options = None
  _UPDATERESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _FEATUREDESCRIPTORREQUEST.fields_by_name['uuid']._options = None
  _FEATUREDESCRIPTORREQUEST.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _FEATUREDESCRIPTORREQUEST.fields_by_name['selector']._options = None
  _FEATUREDESCRIPTORREQUEST.fields_by_name['selector']._serialized_options = b'\372B\316\001r\313\0012\310\001(?si)^((?P<namespace>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})\\.)?(?P<name>([a0-z9]+[a0-z9_]*[a0-z9]+){1,256})(\\+(?P<aggrFn>([a-z]+_*[a-z]+)))?(@-(?P<version>([0-9]+)))?(\\[(?P<encoding>([a-z]+_*[a-z]+))])?$'
  _FEATUREDESCRIPTORRESPONSE.fields_by_name['uuid']._options = None
  _FEATUREDESCRIPTORRESPONSE.fields_by_name['uuid']._serialized_options = b'\372B\005r\003\260\001\001'
  _ENGINESERVICE.methods_by_name['FeatureDescriptor']._options = None
  _ENGINESERVICE.methods_by_name['FeatureDescriptor']._serialized_options = b'\202\323\344\223\002\025B\023\n\004HEAD\022\013/{selector}'
  _ENGINESERVICE.methods_by_name['Get']._options = None
  _ENGINESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\r\022\013/{selector}'
  _ENGINESERVICE.methods_by_name['Set']._options = None
  _ENGINESERVICE.methods_by_name['Set']._serialized_options = b'\202\323\344\223\002\r\032\013/{selector}'
  _ENGINESERVICE.methods_by_name['Append']._options = None
  _ENGINESERVICE.methods_by_name['Append']._serialized_options = b'\202\323\344\223\002\017\"\r/{fqn}/append'
  _ENGINESERVICE.methods_by_name['Incr']._options = None
  _ENGINESERVICE.methods_by_name['Incr']._serialized_options = b'\202\323\344\223\002\r\"\013/{fqn}/incr'
  _ENGINESERVICE.methods_by_name['Update']._options = None
  _ENGINESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\r\"\013/{selector}'
  _globals['_GETREQUEST']._serialized_start=158
  _globals['_GETREQUEST']._serialized_end=556
  _globals['_GETREQUEST_KEYSENTRY']._serialized_start=501
  _globals['_GETREQUEST_KEYSENTRY']._serialized_end=556
  _globals['_GETRESPONSE']._serialized_start=559
  _globals['_GETRESPONSE']._serialized_end=734
  _globals['_SETREQUEST']._serialized_start=737
  _globals['_SETREQUEST']._serialized_end=1069
  _globals['_SETREQUEST_KEYSENTRY']._serialized_start=501
  _globals['_SETREQUEST_KEYSENTRY']._serialized_end=556
  _globals['_SETRESPONSE']._serialized_start=1071
  _globals['_SETRESPONSE']._serialized_end=1172
  _globals['_APPENDREQUEST']._serialized_start=1175
  _globals['_APPENDREQUEST']._serialized_end=1504
  _globals['_APPENDREQUEST_KEYSENTRY']._serialized_start=501
  _globals['_APPENDREQUEST_KEYSENTRY']._serialized_end=556
  _globals['_APPENDRESPONSE']._serialized_start=1506
  _globals['_APPENDRESPONSE']._serialized_end=1610
  _globals['_INCRREQUEST']._serialized_start=1613
  _globals['_INCRREQUEST']._serialized_end=1938
  _globals['_INCRREQUEST_KEYSENTRY']._serialized_start=501
  _globals['_INCRREQUEST_KEYSENTRY']._serialized_end=556
  _globals['_INCRRESPONSE']._serialized_start=1940
  _globals['_INCRRESPONSE']._serialized_end=2042
  _globals['_UPDATEREQUEST']._serialized_start=2045
  _globals['_UPDATEREQUEST']._serialized_end=2383
  _globals['_UPDATEREQUEST_KEYSENTRY']._serialized_start=501
  _globals['_UPDATEREQUEST_KEYSENTRY']._serialized_end=556
  _globals['_UPDATERESPONSE']._serialized_start=2385
  _globals['_UPDATERESPONSE']._serialized_end=2489
  _globals['_FEATUREDESCRIPTORREQUEST']._serialized_start=2492
  _globals['_FEATUREDESCRIPTORREQUEST']._serialized_end=2790
  _globals['_FEATUREDESCRIPTORRESPONSE']._serialized_start=2793
  _globals['_FEATUREDESCRIPTORRESPONSE']._serialized_end=2931
  _globals['_ENGINESERVICE']._serialized_start=2934
  _globals['_ENGINESERVICE']._serialized_end=3521
# @@protoc_insertion_point(module_scope)
