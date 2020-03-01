from time import time
import os
import json

from exemplo_pb2 import ExampleRequest
from exemplo_pb2_grpc import exampleStub

from nameko_grpc.client import Client


label = os.environ.get("LABEL", "")
res = []
timers = {}

with Client("//127.0.0.1", exampleStub) as client:
    for i in range(20): 
        key = f"{label}{i}"
        print(f"send {key}")

        start = time()
        res.append(client.unary_unary.future(ExampleRequest(value=key)))
        end = time()-start

        print(f"TIME:  {end}") 

        timers[key] = {
            "send": end,
            "start": start
        }

    for r in res:
        result = r.result().message
        print(f"return {result}")

        timers[result]["response"] = time()-timers[result]["start"]

print(json.dumps(timers, indent=2))

"""
export LABEL=A; python client.py >> result.txt &
export LABEL=B; python client.py >> result.txt &
export LABEL=C; python client.py >> result.txt &
export LABEL=D; python client.py >> result.txt &
export LABEL=E; python client.py >> result.txt &
export LABEL=F; python client.py >> result.txt &
export LABEL=G; python client.py >> result.txt &
export LABEL=H; python client.py >> result.txt &
export LABEL=I; python client.py >> result.txt &
export LABEL=J; python client.py >> result.txt &
export LABEL=K; python client.py >> result.txt &
export LABEL=L; python client.py >> result.txt &
export LABEL=M; python client.py >> result.txt &
export LABEL=N; python client.py >> result.txt &
export LABEL=O; python client.py >> result.txt &
export LABEL=P; python client.py >> result.txt &
export LABEL=Q; python client.py >> result.txt &
export LABEL=R; python client.py >> result.txt &
export LABEL=S; python client.py >> result.txt &
export LABEL=T; python client.py >> result.txt &
export LABEL=U; python client.py >> result.txt &
export LABEL=V; python client.py >> result.txt &
export LABEL=X; python client.py >> result.txt &
export LABEL=Y; python client.py >> result.txt &
export LABEL=Z; python client.py >> result.txt
"""
