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


__all__ = ("Method", "Message")


class Method:
    set = "set"
    delete = "delete"


class Message:
    method = "method"
    device_id = "device_id"
    data = "data"
    class Data:
        name = "name"
        state = "state"
        device_type = "device_type"
        attributes = "attributes"


class Topics:
    dm = "device-manager/device/{dc_id}"
    dm_lw = "device-manager/device/{dc_id}/lw"
    dm_refresh = "device-manager/refresh"
    comms_event = "event/{device_id}/{service_id}"
    comms_command = "command/{device_id}/{service_id}"
    comms_response = "response/{device_id}/{service_id}"
    comms_err_client = "error/client"
    comms_err_device = "error/device/{device_id}"
    comms_err_command = "error/command/{correlation_id}"


class DeviceAttribute:
    key = "key"
    value = "value"
