from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Ok: _ClassVar[Status]
    Err: _ClassVar[Status]
Ok: Status
Err: Status

class AnalyzeRequest(_message.Message):
    __slots__ = ("name", "code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class AnalyzeResponse(_message.Message):
    __slots__ = ("status", "report", "ir")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    IR_FIELD_NUMBER: _ClassVar[int]
    status: Status
    report: str
    ir: str
    def __init__(self, status: _Optional[_Union[Status, str]] = ..., report: _Optional[str] = ..., ir: _Optional[str] = ...) -> None: ...
