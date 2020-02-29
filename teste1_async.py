from time import time
import os
import json

from nameko.standalone.rpc import ClusterRpcProxy


config = {
    'AMQP_URI':'amqp://guest:@127.0.0.1:5672/'
}

label = os.environ.get("LABEL", "")

res = []
timers = {}

with ClusterRpcProxy(config) as cluster_rpc: 
    for i in range(20): 
        key = f"{label}{i}"
        print(f"send {key}")

        start = time()
        response = cluster_rpc.service_a.dispatching_method.call_async({"k": key}) 
        res.append(response)
        end = time()-start

        print(f"TIME:  {end}") 

        timers[key] = {
            "send": end,
            "start": start
        }

    for r in res:
        result = r.result()
        print(f"return {result}")

        timers[result["result"]["k"]]["response"] = time()-timers[result["result"]["k"]]["start"]

print(json.dumps(timers, indent=2))


"""
export LABEL=A; python teste1_async.py >> result.txt &
export LABEL=B; python teste1_async.py >> result.txt &
export LABEL=C; python teste1_async.py >> result.txt &
export LABEL=D; python teste1_async.py >> result.txt &
export LABEL=E; python teste1_async.py >> result.txt &
export LABEL=F; python teste1_async.py >> result.txt &
export LABEL=G; python teste1_async.py >> result.txt &
export LABEL=H; python teste1_async.py >> result.txt &
export LABEL=I; python teste1_async.py >> result.txt &
export LABEL=J; python teste1_async.py >> result.txt &
export LABEL=K; python teste1_async.py >> result.txt &
export LABEL=L; python teste1_async.py >> result.txt &
export LABEL=M; python teste1_async.py >> result.txt &
export LABEL=N; python teste1_async.py >> result.txt &
export LABEL=O; python teste1_async.py >> result.txt &
export LABEL=P; python teste1_async.py >> result.txt &
export LABEL=Q; python teste1_async.py >> result.txt &
export LABEL=R; python teste1_async.py >> result.txt &
export LABEL=S; python teste1_async.py >> result.txt &
export LABEL=T; python teste1_async.py >> result.txt &
export LABEL=U; python teste1_async.py >> result.txt &
export LABEL=V; python teste1_async.py >> result.txt &
export LABEL=X; python teste1_async.py >> result.txt &
export LABEL=Y; python teste1_async.py >> result.txt &
export LABEL=Z; python teste1_async.py >> result.txt
"""