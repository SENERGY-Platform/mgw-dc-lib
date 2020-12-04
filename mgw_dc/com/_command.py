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


__all__ = ("command", "gen_command_topic", "parse_command_topic")


from .. import _model as model
from .._util import validate_instance
import typing


class command:
    id = "command_id"
    data = "data"


def gen_command_topic(device_id: str, service_id: typing.Optional[str] = None) -> str:
    return model.Topics.comms_command.format(
        device_id=validate_instance(device_id, str),
        service_id=validate_instance(service_id, (str, type(None))) or "+"
    )


def parse_command_topic(topic: str) -> typing.Tuple[str, str]:
    topic = topic.split("/")
    return topic[1], topic[2]
