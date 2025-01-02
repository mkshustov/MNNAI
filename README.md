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
    key='MNN API KEY',
    id='MNN ID',
    # max_retries=2, 
    # timeout=60
)

chat_completion = client.chat_create(
    messages=[
        {
            "role": "user",
            "content": "Hi",
        }
    ],
    model="gpt-4o-mini",
)
print(chat_completion)
```


**Image Generation**

```python
import base64
import os

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


### Models

```python 
print(client.GetModels())
```

### Configuration
Replace the key and id parameters in the MNN client initialization with your own API key and user ID.
Adjust the prompt, model, and other parameters as needed for your specific use case.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Discord 
https://discord.gg/Ku2haNjFvj
