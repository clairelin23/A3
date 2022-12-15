from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FANTASY: GenreType
FICTION: GenreType
ROMANCE: GenreType
available: Status
taken: Status

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: GenreType
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateReply(_message.Message):
    __slots__ = ["message", "title"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    message: str
    title: str
    def __init__(self, message: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: GenreType
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class GetReply(_message.Message):
    __slots__ = ["message", "title"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    message: str
    title: str
    def __init__(self, message: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["aBook", "inventoryNumber", "status"]
    ABOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    aBook: Book
    inventoryNumber: str
    status: Status
    def __init__(self, inventoryNumber: _Optional[str] = ..., aBook: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
