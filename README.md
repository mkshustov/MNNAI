# MNNLibr

This repository contains an example of how to use the MNNLib library to interact with the MNN API for image generation and text chat functionalities.

## Prerequisites

- Python 3.x
- MNNLib library installed. You can install it using pip:

```bash
pip install mnnlibr
```

## Usage
Image Generation
The following code demonstrates how to generate an image based on a prompt using the MNN API.

```python
from mnnlibr import MNN

client = MNN(
    key='MNN API KEY',
    id='MNN ID',
    # max_retries=2, 
    # timeout=60
)

response = client.Image_create(
    prompt="Draw a cute red panda",
    model='sdxl'
)

image_url = response['data'][0]['url']
print(image_url)
```

## Text Chat
The following code demonstrates how to create a chat session with the MNN API, both with streaming and without streaming.

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

### Configuration
Replace the key and id parameters in the MNN client initialization with your own API key and user ID.
Adjust the prompt, model, and other parameters as needed for your specific use case.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Discord 
https://discord.gg/Ku2haNjFvj
