#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class EDAMErrorCode(object):
  UNKNOWN = 1
  BAD_DATA_FORMAT = 2
  PERMISSION_DENIED = 3
  INTERNAL_ERROR = 4
  DATA_REQUIRED = 5
  LIMIT_REACHED = 6
  QUOTA_REACHED = 7
  INVALID_AUTH = 8
  AUTH_EXPIRED = 9
  DATA_CONFLICT = 10
  ENML_VALIDATION = 11
  SHARD_UNAVAILABLE = 12
  @classmethod
  def tostring(cls, val):
    for k,v in vars(cls).iteritems():
      if v == val:
        return k

  @classmethod
  def fromstring(cls, str):
    return getattr(cls, str.upper(), None)

class EDAMUserException(Exception):

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'parameter', None, None, ), # 2
  )

  def __init__(self, d=None):
    self.errorCode = None
    self.parameter = None
    if isinstance(d, dict):
      if 'errorCode' in d:
        self.errorCode = d['errorCode']
      if 'parameter' in d:
        self.parameter = d['parameter']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.parameter = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMUserException')
    if self.errorCode != None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.parameter != None:
      oprot.writeFieldBegin('parameter', TType.STRING, 2)
      oprot.writeString(self.parameter)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self):
    return str(self.__dict__)

  def __repr__(self):
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EDAMSystemException(Exception):

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
  )

  def __init__(self, d=None):
    self.errorCode = None
    self.message = None
    if isinstance(d, dict):
      if 'errorCode' in d:
        self.errorCode = d['errorCode']
      if 'message' in d:
        self.message = d['message']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMSystemException')
    if self.errorCode != None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self):
    return str(self.__dict__)

  def __repr__(self):
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EDAMNotFoundException(Exception):

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'identifier', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
  )

  def __init__(self, d=None):
    self.identifier = None
    self.key = None
    if isinstance(d, dict):
      if 'identifier' in d:
        self.identifier = d['identifier']
      if 'key' in d:
        self.key = d['key']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.identifier = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMNotFoundException')
    if self.identifier != None:
      oprot.writeFieldBegin('identifier', TType.STRING, 1)
      oprot.writeString(self.identifier)
      oprot.writeFieldEnd()
    if self.key != None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self):
    return str(self.__dict__)

  def __repr__(self):
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

