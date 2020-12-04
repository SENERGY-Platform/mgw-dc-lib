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


__all__ = ("Device", "device_state")


from .._util import validate_instance
import typing


class device_state:
    online = "online"
    offline = "offline"


class Device:
    def __init__(self, id: str, name: str, type: str, state: typing.Optional[str] = None):
        self.__id = validate_instance(id, str)
        self.__type = validate_instance(type, str)
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

    def __str__(self, **kwargs):
        attributes = [
            ('id', repr(self.id)),
            ('name', repr(self.name)),
            ('state', repr(self.state)),
            ('type', repr(self.type))
        ]
        if kwargs:
            for arg, value in kwargs.items():
                attributes.append((arg, value))
        return "{}({})".format(self.__class__.__name__, ", ".join(["=".join([key, str(value)]) for key, value in attributes]))
