# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kylinbot_core/Sonar.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Sonar(genpy.Message):
  _md5sum = "32e3008d8c0744f5206e9f75d97600c9"
  _type = "kylinbot_core/Sonar"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 frame_id
uint16 fixed
uint16 moble
uint16 left
uint16 right
"""
  __slots__ = ['frame_id','fixed','moble','left','right']
  _slot_types = ['uint32','uint16','uint16','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       frame_id,fixed,moble,left,right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Sonar, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.frame_id is None:
        self.frame_id = 0
      if self.fixed is None:
        self.fixed = 0
      if self.moble is None:
        self.moble = 0
      if self.left is None:
        self.left = 0
      if self.right is None:
        self.right = 0
    else:
      self.frame_id = 0
      self.fixed = 0
      self.moble = 0
      self.left = 0
      self.right = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_I4H().pack(_x.frame_id, _x.fixed, _x.moble, _x.left, _x.right))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.frame_id, _x.fixed, _x.moble, _x.left, _x.right,) = _get_struct_I4H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_I4H().pack(_x.frame_id, _x.fixed, _x.moble, _x.left, _x.right))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.frame_id, _x.fixed, _x.moble, _x.left, _x.right,) = _get_struct_I4H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_I4H = None
def _get_struct_I4H():
    global _struct_I4H
    if _struct_I4H is None:
        _struct_I4H = struct.Struct("<I4H")
    return _struct_I4H
