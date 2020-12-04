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


__all__ = ("gen_response_topic", "gen_response_msg")


from .. import _model as model
from .._util import validate_instance
from ._command import command
import typing


def gen_response_topic(device_id: str, service_id: str) -> str:
    return model.Topics.comms_response.format(
        device_id=validate_instance(device_id, str),
        service_id=validate_instance(service_id, str)
    )


def gen_response_msg(command_id: str, data: str) -> typing.Dict:
    return {
        command.id: validate_instance(command_id, str),
        command.data: validate_instance(data, str)
    }
