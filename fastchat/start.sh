#!/bin/bash

python -m fastchat.serve.controller --host 0.0.0.0 &
sleep 10
python -m fastchat.serve.model_worker --host 0.0.0.0 --model-name 'vicuna-7b-v1.1' --model-path /model/ --device cpu &
sleep 10
python -m fastchat.serve.api --host 0.0.0.0 --port 8000 &

wait -n
exit $?
