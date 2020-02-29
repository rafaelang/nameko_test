from time import time
import os

from nameko.standalone.rpc import ClusterRpcProxy


config = {
    'AMQP_URI':'amqp://guest:@127.0.0.1:5672/'
}

label = os.environ.get("LABEL", "")


with ClusterRpcProxy(config) as cluster_rpc: 
    for i in range(100): 
        key = f"{label}{i}"
        print(f"send {key}")

        start = time() 
        
        cluster_rpc.service_a.dispatching_method({"ok": key}) 

        print(f"TIME:  {time()-start}") 


"""
export LABEL=A; python teste1.py &
export LABEL=B; python teste1.py &
export LABEL=C; python teste1.py &
export LABEL=D; python teste1.py &
export LABEL=E; python teste1.py &
export LABEL=F; python teste1.py &
export LABEL=G; python teste1.py &
export LABEL=H; python teste1.py &
export LABEL=I; python teste1.py &
export LABEL=J; python teste1.py &
export LABEL=K; python teste1.py &
export LABEL=L; python teste1.py &
export LABEL=M; python teste1.py &
export LABEL=N; python teste1.py &
export LABEL=O; python teste1.py &
export LABEL=P; python teste1.py &
export LABEL=Q; python teste1.py &
export LABEL=R; python teste1.py &
export LABEL=S; python teste1.py &
export LABEL=T; python teste1.py &
export LABEL=U; python teste1.py &
export LABEL=V; python teste1.py &
export LABEL=X; python teste1.py &
export LABEL=Y; python teste1.py &
export LABEL=Z; python teste1.py
"""