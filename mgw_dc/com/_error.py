"""
   Copyright 2022 InfAI (CC SES)

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


__all__ = ("gen_client_error_topic", "gen_device_error_topic", "gen_command_error_topic")


from .. import _model as model
from .._util import validate_instance


def gen_client_error_topic() -> str:
    return model.Topics.comms_err_client


def gen_device_error_topic(device_id: str) -> str:
    return model.Topics.comms_err_device.format(
        device_id=validate_instance(device_id, str)
    )


def gen_command_error_topic(correlation_id: str) -> str:
    return model.Topics.comms_err_device.format(
        device_id=validate_instance(correlation_id, str)
    )
