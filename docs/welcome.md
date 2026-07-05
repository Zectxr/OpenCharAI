# OpenCharAI

An asynchronous Python wrapper for the [Character AI](https://character.ai/) API.  
Built with [curl-cffi](https://github.com/yifeikong/curl_cffi).

---

## Navigation

- **Welcome** ← you're here
- [Getting started](getting_started.md)
- API Reference:
  - [Methods](api_reference/methods.md)
    - [Account](api_reference/methods/account.md)
    - [Character](api_reference/methods/character.md)
    - [Chat](api_reference/methods/chat.md)
    - [User](api_reference/methods/user.md)
    - [Utils](api_reference/methods/utils.md)
  - [Types](api_reference/types.md)
    - [Account / User](api_reference/types/user.md)
    - [Character](api_reference/types/character.md)
    - [Chat](api_reference/types/chat.md)
    - [Message](api_reference/types/message.md)
    - [Media](api_reference/types/media.md)

---

## Quick start

```bash
pip install OpenCharAI
```

```python
from OpenCharAI import get_client

client = await get_client(token="YOUR_TOKEN")
me = await client.account.fetch_me()
print(f"Logged in as @{me.username}")
```

See the [getting started guide](getting_started.md) for detailed setup instructions.
