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


__all__ = ("gen_device_topic", "gen_last_will_topic", "gen_refresh_topic", "gen_set_device_msg", "gen_delete_device_msg")


from .. import _model as model
from .._util import validate_instance
from ._device import Device
import typing


def gen_device_topic(dc_id: str) -> str:
    return model.Topics.dm.format(dc_id=validate_instance(dc_id, str))


def gen_last_will_topic(dc_id: str) -> str:
    return model.Topics.dm_lw.format(dc_id=validate_instance(dc_id, str))


def gen_refresh_topic() -> str:
    return model.Topics.dm_refresh


def gen_set_device_msg(device: Device) -> typing.Dict:
    validate_instance(device, Device)
    return {
        model.Message.method: model.Method.set,
        model.Message.device_id: device.id,
        model.Message.data: {
            model.Message.Data.name: device.name,
            model.Message.Data.state: device.state,
            model.Message.Data.device_type: device.type
        }
    }


def gen_delete_device_msg(device: Device) -> typing.Dict:
    validate_instance(device, Device)
    return {
        model.Message.method: model.Method.delete,
        model.Message.device_id: device.id,
        model.Message.data: None
    }
