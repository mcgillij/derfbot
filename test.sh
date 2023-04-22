#!/bin/bash

curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model":"vicuna-7b-v1.1",
      "messages": [{"role":"user", "content": "Can you tell me a Kobold joke?"}]
    }'
