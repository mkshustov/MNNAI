from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='mnnlibr',
  version='1.0.0',
  author='mkshustov',
  author_email='mkshustov@mail.ru',
  description='Module for using AI',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='http://127.0.0.1:8080/',
  packages=find_packages(),
  install_requires=['requests>=2.25.1', 'aiohttp'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='ai MNN chatgpt',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)