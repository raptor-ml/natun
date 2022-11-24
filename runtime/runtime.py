#  Copyright (c) 2022 RaptorML authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import asyncio
import os
import sys
import warnings

import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

from svc import RuntimeServicer


async def main():
    runtime_name = "default" if os.environ.get('RUNTIME_NAME') is None else os.environ.get('RUNTIME_NAME')
    core_grpc_url = "/tmp/raptor/core.sock" if os.environ.get("CORE_GRPC_URL") is None else os.environ.get(
        "CORE_GRPC_URL")
    engine_channel = grpc.insecure_channel(core_grpc_url)

    svc = RuntimeServicer(engine_channel=engine_channel)
    server = grpc.aio.server()
    svc.attach_to_server(server)
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    reflection.enable_server_reflection((
        svc.full_name(),
        reflection.SERVICE_NAME,
        health.SERVICE_NAME
    ), server)

    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    uds_path = f"/tmp/raptor/runtime/{runtime_name}@{python_version}.sock"
    if not os.path.exists("/tmp/raptor/runtime"):
        os.makedirs("/tmp/raptor/runtime")
    if os.path.exists(uds_path):
        warnings.warn(f"Removing existing UDS path: {uds_path}")
        os.remove(uds_path)

    server.add_insecure_port(f"unix://{uds_path}")
    uds_link = "/tmp/this-runtime.sock"
    if os.path.islink(uds_link):
        os.remove(uds_link)
    os.symlink(uds_path, uds_link)
    print(f"Starting server on {uds_path} or {uds_link}")
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(main())
