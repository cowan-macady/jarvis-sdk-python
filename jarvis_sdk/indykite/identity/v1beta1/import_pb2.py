# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/identity/v1beta1/import.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jarvis_sdk.indykite.identity.v1beta1 import attributes_pb2 as indykite_dot_identity_dot_v1beta1_dot_attributes__pb2
from jarvis_sdk.indykite.identity.v1beta1 import model_pb2 as indykite_dot_identity_dot_v1beta1_dot_model__pb2
from jarvis_sdk.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&indykite/identity/v1beta1/import.proto\x12\x19indykite.identity.v1beta1\x1a*indykite/identity/v1beta1/attributes.proto\x1a%indykite/identity/v1beta1/model.proto\x1a\x17validate/validate.proto\"\xf0\x07\n\x19ImportDigitalTwinsRequest\x12\\\n\x08\x65ntities\x18\x01 \x03(\x0b\x32,.indykite.identity.v1beta1.ImportDigitalTwinB\x12\xfa\x42\x0f\x92\x01\x0c\x08\x01\x10\xe8\x07\"\x05\x8a\x01\x02\x10\x01R\x08\x65ntities\x12;\n\x06\x62\x63rypt\x18\x02 \x01(\x0b\x32!.indykite.identity.v1beta1.BcryptH\x00R\x06\x62\x63rypt\x12T\n\x0fstandard_scrypt\x18\x03 \x01(\x0b\x32).indykite.identity.v1beta1.StandardScryptH\x00R\x0estandardScrypt\x12;\n\x06scrypt\x18\x04 \x01(\x0b\x32!.indykite.identity.v1beta1.ScryptH\x00R\x06scrypt\x12?\n\x08hmac_md5\x18\x05 \x01(\x0b\x32\".indykite.identity.v1beta1.HMACMD5H\x00R\x07hmacMd5\x12\x42\n\thmac_sha1\x18\x06 \x01(\x0b\x32#.indykite.identity.v1beta1.HMACSHA1H\x00R\x08hmacSha1\x12H\n\x0bhmac_sha512\x18\x07 \x01(\x0b\x32%.indykite.identity.v1beta1.HMACSHA512H\x00R\nhmacSha512\x12H\n\x0bhmac_sha256\x18\x08 \x01(\x0b\x32%.indykite.identity.v1beta1.HMACSHA256H\x00R\nhmacSha256\x12\x32\n\x03md5\x18\t \x01(\x0b\x32\x1e.indykite.identity.v1beta1.MD5H\x00R\x03md5\x12N\n\rpbkdf2_sha256\x18\n \x01(\x0b\x32\'.indykite.identity.v1beta1.PBKDF2SHA256H\x00R\x0cpbkdf2Sha256\x12\x45\n\npbkdf_sha1\x18\x0b \x01(\x0b\x32$.indykite.identity.v1beta1.PBKDFSHA1H\x00R\tpbkdfSha1\x12\x35\n\x04sha1\x18\x0c \x01(\x0b\x32\x1f.indykite.identity.v1beta1.SHA1H\x00R\x04sha1\x12;\n\x06sha256\x18\r \x01(\x0b\x32!.indykite.identity.v1beta1.SHA256H\x00R\x06sha256\x12;\n\x06sha512\x18\x0e \x01(\x0b\x32!.indykite.identity.v1beta1.SHA512H\x00R\x06sha512B\x10\n\x0ehash_algorithm\"\xb0\x01\n\x18ImportDigitalTwinSuccess\x12I\n\x0c\x64igital_twin\x18\x01 \x01(\x0b\x32&.indykite.identity.v1beta1.DigitalTwinR\x0b\x64igitalTwin\x12I\n\x07results\x18\x02 \x03(\x0b\x32/.indykite.identity.v1beta1.BatchOperationResultR\x07results\"2\n\x16ImportDigitalTwinError\x12\x18\n\x07message\x18\x01 \x03(\tR\x07message\"\xda\x01\n\x17ImportDigitalTwinResult\x12\x14\n\x05index\x18\x01 \x01(\x04R\x05index\x12O\n\x07success\x18\x02 \x01(\x0b\x32\x33.indykite.identity.v1beta1.ImportDigitalTwinSuccessH\x00R\x07success\x12I\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x31.indykite.identity.v1beta1.ImportDigitalTwinErrorH\x00R\x05\x65rrorB\r\n\x06result\x12\x03\xf8\x42\x01\"j\n\x1aImportDigitalTwinsResponse\x12L\n\x07results\x18\x01 \x03(\x0b\x32\x32.indykite.identity.v1beta1.ImportDigitalTwinResultR\x07results\"\xf2\x04\n\x11ImportDigitalTwin\x12\x19\n\x02id\x18\x01 \x01(\x0c\x42\t\xfa\x42\x06z\x04h\x10p\x01R\x02id\x12$\n\ttenant_id\x18\x02 \x01(\x0c\x42\x07\xfa\x42\x04z\x02h\x10R\x08tenantId\x12L\n\x04kind\x18\x03 \x01(\x0e\x32*.indykite.identity.v1beta1.DigitalTwinKindB\x0c\xfa\x42\t\x82\x01\x06\x10\x01\x18\x01\x18\x03R\x04kind\x12O\n\x05state\x18\x04 \x01(\x0e\x32+.indykite.identity.v1beta1.DigitalTwinStateB\x0c\xfa\x42\t\x82\x01\x06\x10\x01\x18\x01\x18\x02R\x05state\x12\x36\n\x04tags\x18\x05 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x10 \x18\x01\"\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04tags\x12I\n\x08password\x18\x06 \x01(\x0b\x32-.indykite.identity.v1beta1.PasswordCredentialR\x08password\x12h\n\x12provider_user_info\x18\x07 \x03(\x0b\x32\'.indykite.identity.v1beta1.UserProviderB\x11\xfa\x42\x0e\x92\x01\x0b\x08\x00\x10\n\"\x05\x8a\x01\x02\x10\x01R\x10providerUserInfo\x12K\n\nproperties\x18\x08 \x01(\x0b\x32+.indykite.identity.v1beta1.ImportPropertiesR\nproperties\x12\x43\n\x08metadata\x18\t \x01(\x0b\x32\'.indykite.identity.v1beta1.UserMetadataR\x08metadata\"\x99\x01\n\x10ImportProperties\x12\x62\n\noperations\x18\x02 \x03(\x0b\x32\x31.indykite.identity.v1beta1.PropertyBatchOperationB\x0f\xfa\x42\x0c\x92\x01\t\x08\x01\"\x05\x8a\x01\x02\x10\x01R\noperations\x12!\n\x0c\x66orce_delete\x18\x04 \x01(\x08R\x0b\x66orceDelete\"\xa6\x01\n\x0cUserMetadata\x12-\n\x12\x63reation_timestamp\x18\x01 \x01(\x03R\x11\x63reationTimestamp\x12\x31\n\x15last_log_in_timestamp\x18\x02 \x01(\x03R\x12lastLogInTimestamp\x12\x34\n\x16last_refresh_timestamp\x18\x03 \x01(\x03R\x14lastRefreshTimestamp\"\x97\x01\n\x0cUserProvider\x12\x10\n\x03uid\x18\x01 \x01(\tR\x03uid\x12\x1f\n\x0bprovider_id\x18\x02 \x01(\tR\nproviderId\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\x12!\n\x0c\x64isplay_name\x18\x04 \x01(\tR\x0b\x64isplayName\x12\x1b\n\tphoto_url\x18\x05 \x01(\tR\x08photoUrl\"9\n\x05\x45mail\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12\x1a\n\x08verified\x18\x02 \x01(\x08R\x08verified\"^\n\x06Mobile\x12\x38\n\x06mobile\x18\x01 \x01(\tB \xfa\x42\x1dr\x1b\x32\x16^+.*[0-9A-Za-z]{7,16}$\xd0\x01\x01R\x06mobile\x12\x1a\n\x08verified\x18\x02 \x01(\x08R\x08verified\"\x93\x02\n\x12PasswordCredential\x12\x38\n\x05\x65mail\x18\x01 \x01(\x0b\x32 .indykite.identity.v1beta1.EmailH\x00R\x05\x65mail\x12;\n\x06mobile\x18\x02 \x01(\x0b\x32!.indykite.identity.v1beta1.MobileH\x00R\x06mobile\x12\x1c\n\x08username\x18\x03 \x01(\tH\x00R\x08username\x12\x16\n\x05value\x18\x04 \x01(\tH\x01R\x05value\x12=\n\x04hash\x18\x05 \x01(\x0b\x32\'.indykite.identity.v1beta1.PasswordHashH\x01R\x04hashB\x05\n\x03uidB\n\n\x08password\"G\n\x0cPasswordHash\x12#\n\rpassword_hash\x18\x04 \x01(\x0cR\x0cpasswordHash\x12\x12\n\x04salt\x18\x05 \x01(\x0cR\x04salt\"\x08\n\x06\x42\x63rypt\"\xa8\x01\n\x0eStandardScrypt\x12\x1d\n\nblock_size\x18\x01 \x01(\x03R\tblockSize\x12,\n\x12\x64\x65rived_key_length\x18\x02 \x01(\x03R\x10\x64\x65rivedKeyLength\x12\x1f\n\x0bmemory_cost\x18\x03 \x01(\x03R\nmemoryCost\x12(\n\x0fparallelization\x18\x04 \x01(\x03R\x0fparallelization\"z\n\x06Scrypt\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12%\n\x0esalt_separator\x18\x02 \x01(\x0cR\rsaltSeparator\x12\x16\n\x06rounds\x18\x03 \x01(\x03R\x06rounds\x12\x1f\n\x0bmemory_cost\x18\x04 \x01(\x03R\nmemoryCost\"\x1b\n\x07HMACMD5\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\"\x1c\n\x08HMACSHA1\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\"\x1e\n\nHMACSHA512\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\"\x1e\n\nHMACSHA256\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\"\x1d\n\x03MD5\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06rounds\"&\n\x0cPBKDF2SHA256\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06rounds\"#\n\tPBKDFSHA1\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06rounds\"\x1e\n\x04SHA1\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06rounds\" \n\x06SHA256\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06rounds\" \n\x06SHA512\x12\x16\n\x06rounds\x18\x01 \x01(\x03R\x06roundsB\xb2\x01\n\x1d\x63om.indykite.identity.v1beta1B\x0bImportProtoP\x01\xa2\x02\x03IIX\xaa\x02\x19Indykite.Identity.V1beta1\xca\x02\x19Indykite\\Identity\\V1beta1\xe2\x02%Indykite\\Identity\\V1beta1\\GPBMetadata\xea\x02\x1bIndykite::Identity::V1beta1b\x06proto3')



_IMPORTDIGITALTWINSREQUEST = DESCRIPTOR.message_types_by_name['ImportDigitalTwinsRequest']
_IMPORTDIGITALTWINSUCCESS = DESCRIPTOR.message_types_by_name['ImportDigitalTwinSuccess']
_IMPORTDIGITALTWINERROR = DESCRIPTOR.message_types_by_name['ImportDigitalTwinError']
_IMPORTDIGITALTWINRESULT = DESCRIPTOR.message_types_by_name['ImportDigitalTwinResult']
_IMPORTDIGITALTWINSRESPONSE = DESCRIPTOR.message_types_by_name['ImportDigitalTwinsResponse']
_IMPORTDIGITALTWIN = DESCRIPTOR.message_types_by_name['ImportDigitalTwin']
_IMPORTPROPERTIES = DESCRIPTOR.message_types_by_name['ImportProperties']
_USERMETADATA = DESCRIPTOR.message_types_by_name['UserMetadata']
_USERPROVIDER = DESCRIPTOR.message_types_by_name['UserProvider']
_EMAIL = DESCRIPTOR.message_types_by_name['Email']
_MOBILE = DESCRIPTOR.message_types_by_name['Mobile']
_PASSWORDCREDENTIAL = DESCRIPTOR.message_types_by_name['PasswordCredential']
_PASSWORDHASH = DESCRIPTOR.message_types_by_name['PasswordHash']
_BCRYPT = DESCRIPTOR.message_types_by_name['Bcrypt']
_STANDARDSCRYPT = DESCRIPTOR.message_types_by_name['StandardScrypt']
_SCRYPT = DESCRIPTOR.message_types_by_name['Scrypt']
_HMACMD5 = DESCRIPTOR.message_types_by_name['HMACMD5']
_HMACSHA1 = DESCRIPTOR.message_types_by_name['HMACSHA1']
_HMACSHA512 = DESCRIPTOR.message_types_by_name['HMACSHA512']
_HMACSHA256 = DESCRIPTOR.message_types_by_name['HMACSHA256']
_MD5 = DESCRIPTOR.message_types_by_name['MD5']
_PBKDF2SHA256 = DESCRIPTOR.message_types_by_name['PBKDF2SHA256']
_PBKDFSHA1 = DESCRIPTOR.message_types_by_name['PBKDFSHA1']
_SHA1 = DESCRIPTOR.message_types_by_name['SHA1']
_SHA256 = DESCRIPTOR.message_types_by_name['SHA256']
_SHA512 = DESCRIPTOR.message_types_by_name['SHA512']
ImportDigitalTwinsRequest = _reflection.GeneratedProtocolMessageType('ImportDigitalTwinsRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWINSREQUEST,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwinsRequest)
  })
_sym_db.RegisterMessage(ImportDigitalTwinsRequest)

ImportDigitalTwinSuccess = _reflection.GeneratedProtocolMessageType('ImportDigitalTwinSuccess', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWINSUCCESS,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwinSuccess)
  })
_sym_db.RegisterMessage(ImportDigitalTwinSuccess)

ImportDigitalTwinError = _reflection.GeneratedProtocolMessageType('ImportDigitalTwinError', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWINERROR,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwinError)
  })
_sym_db.RegisterMessage(ImportDigitalTwinError)

ImportDigitalTwinResult = _reflection.GeneratedProtocolMessageType('ImportDigitalTwinResult', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWINRESULT,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwinResult)
  })
_sym_db.RegisterMessage(ImportDigitalTwinResult)

ImportDigitalTwinsResponse = _reflection.GeneratedProtocolMessageType('ImportDigitalTwinsResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWINSRESPONSE,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwinsResponse)
  })
_sym_db.RegisterMessage(ImportDigitalTwinsResponse)

ImportDigitalTwin = _reflection.GeneratedProtocolMessageType('ImportDigitalTwin', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDIGITALTWIN,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportDigitalTwin)
  })
_sym_db.RegisterMessage(ImportDigitalTwin)

ImportProperties = _reflection.GeneratedProtocolMessageType('ImportProperties', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPROPERTIES,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.ImportProperties)
  })
_sym_db.RegisterMessage(ImportProperties)

UserMetadata = _reflection.GeneratedProtocolMessageType('UserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _USERMETADATA,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.UserMetadata)
  })
_sym_db.RegisterMessage(UserMetadata)

UserProvider = _reflection.GeneratedProtocolMessageType('UserProvider', (_message.Message,), {
  'DESCRIPTOR' : _USERPROVIDER,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.UserProvider)
  })
_sym_db.RegisterMessage(UserProvider)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), {
  'DESCRIPTOR' : _EMAIL,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Email)
  })
_sym_db.RegisterMessage(Email)

Mobile = _reflection.GeneratedProtocolMessageType('Mobile', (_message.Message,), {
  'DESCRIPTOR' : _MOBILE,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Mobile)
  })
_sym_db.RegisterMessage(Mobile)

PasswordCredential = _reflection.GeneratedProtocolMessageType('PasswordCredential', (_message.Message,), {
  'DESCRIPTOR' : _PASSWORDCREDENTIAL,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.PasswordCredential)
  })
_sym_db.RegisterMessage(PasswordCredential)

PasswordHash = _reflection.GeneratedProtocolMessageType('PasswordHash', (_message.Message,), {
  'DESCRIPTOR' : _PASSWORDHASH,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.PasswordHash)
  })
_sym_db.RegisterMessage(PasswordHash)

Bcrypt = _reflection.GeneratedProtocolMessageType('Bcrypt', (_message.Message,), {
  'DESCRIPTOR' : _BCRYPT,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Bcrypt)
  })
_sym_db.RegisterMessage(Bcrypt)

StandardScrypt = _reflection.GeneratedProtocolMessageType('StandardScrypt', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDSCRYPT,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.StandardScrypt)
  })
_sym_db.RegisterMessage(StandardScrypt)

Scrypt = _reflection.GeneratedProtocolMessageType('Scrypt', (_message.Message,), {
  'DESCRIPTOR' : _SCRYPT,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Scrypt)
  })
_sym_db.RegisterMessage(Scrypt)

HMACMD5 = _reflection.GeneratedProtocolMessageType('HMACMD5', (_message.Message,), {
  'DESCRIPTOR' : _HMACMD5,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.HMACMD5)
  })
_sym_db.RegisterMessage(HMACMD5)

HMACSHA1 = _reflection.GeneratedProtocolMessageType('HMACSHA1', (_message.Message,), {
  'DESCRIPTOR' : _HMACSHA1,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.HMACSHA1)
  })
_sym_db.RegisterMessage(HMACSHA1)

HMACSHA512 = _reflection.GeneratedProtocolMessageType('HMACSHA512', (_message.Message,), {
  'DESCRIPTOR' : _HMACSHA512,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.HMACSHA512)
  })
_sym_db.RegisterMessage(HMACSHA512)

HMACSHA256 = _reflection.GeneratedProtocolMessageType('HMACSHA256', (_message.Message,), {
  'DESCRIPTOR' : _HMACSHA256,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.HMACSHA256)
  })
_sym_db.RegisterMessage(HMACSHA256)

MD5 = _reflection.GeneratedProtocolMessageType('MD5', (_message.Message,), {
  'DESCRIPTOR' : _MD5,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.MD5)
  })
_sym_db.RegisterMessage(MD5)

PBKDF2SHA256 = _reflection.GeneratedProtocolMessageType('PBKDF2SHA256', (_message.Message,), {
  'DESCRIPTOR' : _PBKDF2SHA256,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.PBKDF2SHA256)
  })
_sym_db.RegisterMessage(PBKDF2SHA256)

PBKDFSHA1 = _reflection.GeneratedProtocolMessageType('PBKDFSHA1', (_message.Message,), {
  'DESCRIPTOR' : _PBKDFSHA1,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.PBKDFSHA1)
  })
_sym_db.RegisterMessage(PBKDFSHA1)

SHA1 = _reflection.GeneratedProtocolMessageType('SHA1', (_message.Message,), {
  'DESCRIPTOR' : _SHA1,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.SHA1)
  })
_sym_db.RegisterMessage(SHA1)

SHA256 = _reflection.GeneratedProtocolMessageType('SHA256', (_message.Message,), {
  'DESCRIPTOR' : _SHA256,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.SHA256)
  })
_sym_db.RegisterMessage(SHA256)

SHA512 = _reflection.GeneratedProtocolMessageType('SHA512', (_message.Message,), {
  'DESCRIPTOR' : _SHA512,
  '__module__' : 'indykite.identity.v1beta1.import_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.SHA512)
  })
_sym_db.RegisterMessage(SHA512)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.indykite.identity.v1beta1B\013ImportProtoP\001\242\002\003IIX\252\002\031Indykite.Identity.V1beta1\312\002\031Indykite\\Identity\\V1beta1\342\002%Indykite\\Identity\\V1beta1\\GPBMetadata\352\002\033Indykite::Identity::V1beta1'
  _IMPORTDIGITALTWINSREQUEST.fields_by_name['entities']._options = None
  _IMPORTDIGITALTWINSREQUEST.fields_by_name['entities']._serialized_options = b'\372B\017\222\001\014\010\001\020\350\007\"\005\212\001\002\020\001'
  _IMPORTDIGITALTWINRESULT.oneofs_by_name['result']._options = None
  _IMPORTDIGITALTWINRESULT.oneofs_by_name['result']._serialized_options = b'\370B\001'
  _IMPORTDIGITALTWIN.fields_by_name['id']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['id']._serialized_options = b'\372B\006z\004h\020p\001'
  _IMPORTDIGITALTWIN.fields_by_name['tenant_id']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['tenant_id']._serialized_options = b'\372B\004z\002h\020'
  _IMPORTDIGITALTWIN.fields_by_name['kind']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['kind']._serialized_options = b'\372B\t\202\001\006\020\001\030\001\030\003'
  _IMPORTDIGITALTWIN.fields_by_name['state']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['state']._serialized_options = b'\372B\t\202\001\006\020\001\030\001\030\002'
  _IMPORTDIGITALTWIN.fields_by_name['tags']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['tags']._serialized_options = b'\372B\037\222\001\034\020 \030\001\"\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _IMPORTDIGITALTWIN.fields_by_name['provider_user_info']._options = None
  _IMPORTDIGITALTWIN.fields_by_name['provider_user_info']._serialized_options = b'\372B\016\222\001\013\010\000\020\n\"\005\212\001\002\020\001'
  _IMPORTPROPERTIES.fields_by_name['operations']._options = None
  _IMPORTPROPERTIES.fields_by_name['operations']._serialized_options = b'\372B\014\222\001\t\010\001\"\005\212\001\002\020\001'
  _MOBILE.fields_by_name['mobile']._options = None
  _MOBILE.fields_by_name['mobile']._serialized_options = b'\372B\035r\0332\026^+.*[0-9A-Za-z]{7,16}$\320\001\001'
  _IMPORTDIGITALTWINSREQUEST._serialized_start=178
  _IMPORTDIGITALTWINSREQUEST._serialized_end=1186
  _IMPORTDIGITALTWINSUCCESS._serialized_start=1189
  _IMPORTDIGITALTWINSUCCESS._serialized_end=1365
  _IMPORTDIGITALTWINERROR._serialized_start=1367
  _IMPORTDIGITALTWINERROR._serialized_end=1417
  _IMPORTDIGITALTWINRESULT._serialized_start=1420
  _IMPORTDIGITALTWINRESULT._serialized_end=1638
  _IMPORTDIGITALTWINSRESPONSE._serialized_start=1640
  _IMPORTDIGITALTWINSRESPONSE._serialized_end=1746
  _IMPORTDIGITALTWIN._serialized_start=1749
  _IMPORTDIGITALTWIN._serialized_end=2375
  _IMPORTPROPERTIES._serialized_start=2378
  _IMPORTPROPERTIES._serialized_end=2531
  _USERMETADATA._serialized_start=2534
  _USERMETADATA._serialized_end=2700
  _USERPROVIDER._serialized_start=2703
  _USERPROVIDER._serialized_end=2854
  _EMAIL._serialized_start=2856
  _EMAIL._serialized_end=2913
  _MOBILE._serialized_start=2915
  _MOBILE._serialized_end=3009
  _PASSWORDCREDENTIAL._serialized_start=3012
  _PASSWORDCREDENTIAL._serialized_end=3287
  _PASSWORDHASH._serialized_start=3289
  _PASSWORDHASH._serialized_end=3360
  _BCRYPT._serialized_start=3362
  _BCRYPT._serialized_end=3370
  _STANDARDSCRYPT._serialized_start=3373
  _STANDARDSCRYPT._serialized_end=3541
  _SCRYPT._serialized_start=3543
  _SCRYPT._serialized_end=3665
  _HMACMD5._serialized_start=3667
  _HMACMD5._serialized_end=3694
  _HMACSHA1._serialized_start=3696
  _HMACSHA1._serialized_end=3724
  _HMACSHA512._serialized_start=3726
  _HMACSHA512._serialized_end=3756
  _HMACSHA256._serialized_start=3758
  _HMACSHA256._serialized_end=3788
  _MD5._serialized_start=3790
  _MD5._serialized_end=3819
  _PBKDF2SHA256._serialized_start=3821
  _PBKDF2SHA256._serialized_end=3859
  _PBKDFSHA1._serialized_start=3861
  _PBKDFSHA1._serialized_end=3896
  _SHA1._serialized_start=3898
  _SHA1._serialized_end=3928
  _SHA256._serialized_start=3930
  _SHA256._serialized_end=3962
  _SHA512._serialized_start=3964
  _SHA512._serialized_end=3996
# @@protoc_insertion_point(module_scope)
