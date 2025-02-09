# MNNAI

This repository contains an example of how to use the mnnai library.

## Prerequisites

- Python 3.x
- MNNAI library installed. You can install it using pip:

```bash
pip install mnnai
```

## Usage

**Non-Streaming Chat**

```python
from mnnai import MNN

client = MNN(
    key='MNN API KEY' # This is the default and can be omitted
)

chat_completion = client.chat.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o-mini"
)
print(chat_completion.choices[0].message.content)
```

**Streaming Chat**

```python
stream = client.chat.create(
    messages=[
        {
            "role": "user",
            "content": "Will the neural networks capture the world?",
        }
    ],
    model="gpt-4o-mini",
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

**Image Generation**

```python
import base64
import os

response = client.images.create(
    prompt="Draw a cute red panda",
    model='dall-e-3'
)

image_base64 = response.data[0].url

os.makedirs('images', exist_ok=True)

for i, image_base64 in enumerate(image_base64):
    image_data = base64.b64decode(image_base64)

    with open(f'images/image_{i}.png', 'wb') as f:
        f.write(image_data)

print("Images have been successfully downloaded!")
```

## Async usage

**Non-Streaming Chat**

```python
import asyncio

async def main():
    chat_completion = await client.chat.async_create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-4o-mini",
    )
    print(chat_completion.choices[0].message.content)


asyncio.run(main())
```

**Streaming Chat**

```python
import asyncio

async def main():
    stream = await client.chat.async_create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
```

**Image Generation**

```python
import asyncio
import base64
import os

async def main():
    response = await client.images.async_create(
        prompt="Draw a cute red panda",
        model='dall-e-3'
    )

    image_base64 = response.data[0].url

    os.makedirs('images', exist_ok=True)

    for i, image_base64 in enumerate(image_base64):
        image_data = base64.b64decode(image_base64)

        with open(f'images/image_{i}.png', 'wb') as f:
            f.write(image_data)

    print("Images have been successfully downloaded!")


asyncio.run(main())
```

## Auxiliary functions 

**Get models**

```python
print(client.GetModels())
```

**Configuring the client**

```python
from mnnai import MNN

client = MNN(
    key='MNN API KEY',
    max_retries=2, # Number of retries in case of failure
    timeout=60, # Maximum amount of time the request will be processed
    debug=True # Whether the application needs to be debugged
)
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Discord 
https://discord.gg/Ku2haNjFvj

