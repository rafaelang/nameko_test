# teste nameko

## broker

```
docker run -d -p 5672:5672 rabbitmq:3
```

## install

- virtualenv python3

```
pip install -r requirements.txt
```

## run 

```
nameko run services --config config.yml
```

## teste

```
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
```

## pior resultado

```json
"X2": {
    "send": 0.20346665382385254,
    "start": 1582989378.051139,
    "response": 12.234633684158325
  },
```