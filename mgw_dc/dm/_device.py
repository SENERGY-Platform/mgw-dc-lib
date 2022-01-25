"""
   Copyright 2020 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

__all__ = ("Device", "device_state", "gen_attribute")

import typing

from .._util import validate_instance
from .._model import DeviceAttribute


class device_state:
    online = "online"
    offline = "offline"


def gen_attribute(key, value):
    validate_instance(key, str)
    validate_instance(value, (str, int, float))
    return {DeviceAttribute.key: key, DeviceAttribute.value: value}


class Device:
    def __init__(self, id: str, name: str, type: str, state: typing.Optional[str] = None, attributes: typing.Optional[typing.List[typing.Dict[str, typing.Union[str, int, float]]]] = None):
        self.__id = validate_instance(id, str)
        self.__type = validate_instance(type, str)
        self.attributes = attributes
        self.name = name
        self.state = state

    @property
    def id(self) -> str:
        return self.__id

    @property
    def type(self) -> str:
        return self.__type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, arg: str) -> None:
        self.__name = validate_instance(arg, str)

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, arg: str) -> None:
        if validate_instance(arg, (str, type(None))) in device_state.__dict__.values():
            self.__state = arg
        else:
            err = "undefined state '{}'".format(arg)
            raise ValueError(err)

    @property
    def attributes(self) -> typing.Optional[typing.List[typing.Dict[str, typing.Union[str, int, float]]]]:
        if self.__attributes:
            return [obj.copy() for obj in self.__attributes]
        else:
            return self.__attributes

    @attributes.setter
    def attributes(self, arg: typing.List[typing.Dict[str, typing.Union[str, int, float]]]):
        validate_instance(arg, (list, tuple, type(None)))
        if arg:
            attributes = list()
            for item in arg:
                attributes.append(gen_attribute(**item))
            self.__attributes = attributes
        else:
            self.__attributes = arg

    def __str__(self, **kwargs):
        properties = [
            ('id', repr(self.id)),
            ('name', repr(self.name)),
            ('state', repr(self.state)),
            ('type', repr(self.type)),
            ('attributes', repr(self.__attributes))
        ]
        if kwargs:
            for arg, value in kwargs.items():
                properties.append((arg, value))
        return "{}({})".format(
            self.__class__.__name__, ", ".join(["=".join([key, str(value)]) for key, value in properties])
        )
