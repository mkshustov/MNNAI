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
            "content": "What's the weather like in New York?",
        }
    ],
    model="gpt-4o-mini",
    web_search=True # Internet search
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

Base64 response:
```python
import base64
import os

response = client.images.create(
    prompt="Draw a cute red panda",
    model='dall-e-3'
)

image_base64 = response.data

os.makedirs('images', exist_ok=True)

for i, image_base64 in enumerate(image_base64):
    image_data = base64.b64decode(image_base64.b64_json)

    with open(f'images/image_{i}.png', 'wb') as f:
        f.write(image_data)

print("Images have been successfully downloaded!")
```

Url:
```python
response = client.images.create(
    prompt="Draw a cute red panda",
    model='dall-e-3',
    n=4,
    enhance=True,
    response_format='url'
)
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

Base64 response:
```python
import asyncio
import base64
import os

async def main():
    response = await client.images.async_create(
        prompt="Draw a cute red panda",
        model='dall-e-3',
        n=4,
        enhance=True
    )

    image_base64 = response.data

    os.makedirs('images', exist_ok=True)

    for i, image_base64 in enumerate(image_base64):
        image_data = base64.b64decode(image_base64.b64_json)

        with open(f'images/image_{i}.png', 'wb') as f:
            f.write(image_data)

    print("Images have been successfully downloaded!")


asyncio.run(main())
```

Url:
```python
import asyncio

async def main():
    response = await client.images.async_create(
        prompt="Draw a cute red panda",
        model='dall-e-3',
        n=4,
        enhance=True,
        response_format='url'
    )

    for url in response.data:
        print(url.url)

asyncio.run(main())
```

**Vision**

With an image URL:

```python
prompt = "What is in this image?"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Red_Panda_%2825193861686%29.jpg/1600px-Red_Panda_%2825193861686%29.jpg"

response = client.chat.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": img_url
                    }
                },
            ]
        }
    ],
)
```

With the image as a base64 encoded string:

```python
import base64

image_path = "image.png"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)
prompt = "What is in this image?"

response = client.chat.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                },
            ]
        }
    ],
)
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