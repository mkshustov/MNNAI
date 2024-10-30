# MNNAI

This repository contains an example of how to use the mnnai library.

## Prerequisites

- Python 3.x
- MNNAI library installed. You can install it using pip:

```bash
pip install mnnai
```

## Usage
**Image Generation**

```python
from mnnai import MNN
import base64
import os


client = MNN(
    key='MNN API KEY',
    id='MNN ID',
    # max_retries=2, 
    # timeout=60
)

response = client.Image_create(
    prompt="Draw a cute red panda",
    model='dall-e-3'
)

image_base64 = response['data'][0]['urls']

os.makedirs('images', exist_ok=True)

for i, image_base64 in enumerate(image_base64):
    image_data = base64.b64decode(image_base64)

    with open(f'images/image_{i}.png', 'wb') as f:
        f.write(image_data)

print("Images have been successfully downloaded!")
```

**Streaming Chat**
```python
import asyncio

stream = client.async_chat_create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hi"}],
    stream=True,
    temperature=0.5
)

async def generate():
    async for chunk in stream:
        if 'result' in chunk:
            print(chunk['result'], end='')
        else:
            print(f"\n{chunk}")

asyncio.run(generate())
```

**Non-Streaming Chat**
```python
chat_completion = client.chat_create(
    messages=[
        {
            "role": "user",
            "content": "Hi",
        }
    ],
    model="gpt-4o",
)
print(chat_completion)
```

### Models

Currently MNN supports:

```1c
**Text**:

*GPT 4o* : gpt-4o

*GPT 4o Mini* : gpt-4o-mini

*GPT 4 Turbo* : gpt-4-turbo

*GPT 3.5 Turbo* : gpt-3.5-turbo

*GPT 3.5 Turbo (16k)* : gpt-3.5-turbo-16k


*Llama 3.1 (70b)* : llama-3.1-70b


*Claude 3 (haiku)* : claude-3-haiku

**Image**:

*Stable diffusion (3)* : sd-3

*Flux (schnell)* : flux-schnell

*Dall-e (3)* : dall-e-3

**Are being tested**:

gemma-2b-it

Mixtral-8x7B-Instruct-v0.1
```



### Configuration
Replace the key and id parameters in the MNN client initialization with your own API key and user ID.
Adjust the prompt, model, and other parameters as needed for your specific use case.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Discord 
https://discord.gg/Ku2haNjFvj
