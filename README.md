# MagicPyden

[![Github Issues](https://img.shields.io/github/issues/ChristianPerez34/magicpyden?logo=github&style=for-the-badge)](https://github.com/ChristianPerez34/magicpyden/issues)
[![Codacy Badge](https://img.shields.io/codacy/grade/12257657689e48369b7e91b215dcb14a?logo=codacy&style=for-the-badge)](https://www.codacy.com/gh/ChristianPerez34/magicpyden/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ChristianPerez34/magicpyden&amp;utm_campaign=Badge_Grade)
[![Github Top Language](https://img.shields.io/github/languages/top/Stonks-Luma-Liberty/Crepitus?logo=python&style=for-the-badge)](https://www.python.org)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg?style=for-the-badge)](https://github.com/wemake-services/wemake-python-styleguide)

Asynchronous API wrapper for the MagicEden API

## Installation

PyPi

```bash
  pip install magicpyden
```

Poetry

```bash
  poetry add magicpyden
```

From source

```bash
  git clone https://github.com/ChristianPerez34/magicpyden.git
  cd magicpyden
  python setup.py install
```

## Usage/Examples

[Official Documentation](https://api.magiceden.dev)

```python
from magicpyden import MagicEdenApi

# Assuming inside async function/method
async with MagicEdenApi() as api:
    collection_stats = await api.get_collection_stats(collection_name="degods")
```
