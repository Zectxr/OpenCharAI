# OpenCharAI

> An asynchronous Python API wrapper for [Character AI](https://character.ai/), powered by [curl-cffi](https://github.com/yifeikong/curl_cffi).  
> Forked from [PyCharacterAI](https://github.com/Xtr4F/PyCharacterAI) by XtraF.

> [!WARNING]
> This is an unofficial community project — not affiliated with Character AI. All API endpoints were discovered through reverse engineering. Use at your own risk.
>
> The library is actively maintained to keep up with website changes. Features not documented here may change or be removed without notice.

---

📚 [Documentation](https://github.com/Zectxr/OpenCharAI/blob/main/docs/welcome.md)

---

**What's new in OpenCharAI:**

- ✅ **Model preferences** — set your default model (`MODEL_TYPE_DEEP_SYNTH_LITE`, `MODEL_TYPE_SMART`, etc.)
- ✅ **Output styles** — pick a chat style (`creative`, `balanced`, `precise`, `default`)
- ✅ **Per-chat output style** — pass `output_style` to `create_chat()` for granular control
- ✅ **`MODEL_TYPE_DEEP_SYNTH_LITE`** — support for Character AI's latest model
- ✅ **`preferred_model_type` & `model_preference_version`** exposed on `Chat`
- ✅ **Bug fixes** — `generate_image()` and `upload_voice()` updated for API changes
- ✅ **curl-cffi** bumped to `>=0.15.0`

Questions or suggestions? [Open an issue](https://github.com/Zectxr/OpenCharAI/issues).

---

## Getting started

Install the package:

```bash
pip install OpenCharAI
```

Import and create a client:

```Python
from OpenCharAI import Client

client = Client()
```

Authenticate with your token:

```Python
await client.authenticate("TOKEN")
```

> To upload avatars you'll also need a `web_next_auth` token:
>
> ```Python
> await client.authenticate("TOKEN", web_next_auth="WEB_NEXT_AUTH")
> ```

Or use the convenience helper:

```Python
from OpenCharAI import get_client

client = await get_client(token="TOKEN", web_next_auth="WEB_NEXT_AUTH")
```

---

## Getting your tokens

> [!WARNING]
> Never share your tokens — anyone with them gains full access to your account.

This library uses two tokens. The main `token` is required for most methods. The `web_next_auth` token is only needed for `upload_avatar()`.

### Quick method (recommended)

Copy both tokens at once from the browser console:

1. Go to [Character AI](https://character.ai) and **log in**
2. Open developer tools (`F12` / `Ctrl+Shift+I` / `Cmd+J`)
3. Go to the **Console** tab
4. Paste and press Enter:

```javascript
copy({
  token: JSON.parse(localStorage.getItem('char_token')).accessToken,
  web_next_auth: document.cookie.match(/web-next-auth=([^;]+)/)?.[1] || ''
})
```

Your clipboard will contain both values.

### Alternative: Network tab

1. Open [Character AI](https://character.ai) in your browser
2. Open developer tools (`F12` / `Ctrl+Shift+I` / `Cmd+J`)
3. Go to the **Network** tab
4. Interact with the site (e.g. visit your profile)
5. Find a request header named `Authorization` and copy the value after `Token`

![token location](https://github.com/Zectxr/OpenCharAI/blob/main/assets/token.png)

### Getting `web_next_auth` token only

1. Open [Character AI](https://character.ai) in your browser
2. Open developer tools (`F12` / `Ctrl+Shift+I` / `Cmd+J`)
3. Go to the **Console** tab
4. Paste and press Enter:
```javascript
copy(document.cookie.match(/web-next-auth=([^;]+)/)?.[1] || '')
```

Or find it in **Storage → Cookies** → look for `web-next-auth`.

![web_next_auth location](https://github.com/Zectxr/OpenCharAI/blob/main/assets/web_next_auth.png)

---

## Examples

### Basic chat

```Python
import asyncio
from OpenCharAI import get_client
from OpenCharAI.exceptions import SessionClosedError

token = "TOKEN"
character_id = "ID"

async def main():
    client = await get_client(token=token)
    me = await client.account.fetch_me()
    print(f"Authenticated as @{me.username}")

    chat, greeting = await client.chat.create_chat(character_id)
    print(f"{greeting.author_name}: {greeting.get_primary_candidate().text}")

    try:
        while True:
            msg = input(f"[{me.name}]: ")
            answer = await client.chat.send_message(character_id, chat.chat_id, msg)
            print(f"[{answer.author_name}]: {answer.get_primary_candidate().text}")
    except SessionClosedError:
        print("Session closed. Bye!")
    finally:
        await client.close_session()

asyncio.run(main())
```

### Streaming

```Python
async def main():
    client = await get_client(token=token)
    me = await client.account.fetch_me()
    chat, greeting = await client.chat.create_chat(character_id)
    print(f"[{greeting.author_name}]: {greeting.get_primary_candidate().text}")

    try:
        while True:
            msg = input(f"[{me.name}]: ")
            stream = await client.chat.send_message(character_id, chat.chat_id, msg, streaming=True)
            printed = 0
            async for chunk in stream:
                if printed == 0:
                    print(f"[{chunk.author_name}]: ", end="")
                text = chunk.get_primary_candidate().text
                print(text[printed:], end="")
                printed = len(text)
            print("\n")
    except SessionClosedError:
        print("Session closed. Bye!")
    finally:
        await client.close_session()
```

### Model types & output styles

```Python
# Create a chat with a specific model:
chat, greeting = await client.chat.create_chat(
    character_id,
    model_type="MODEL_TYPE_DEEP_SYNTH_LITE"
)

# Or with a specific output style:
chat, greeting = await client.chat.create_chat(
    character_id,
    output_style="creative"  # creative | balanced | precise | default
)

# Inspect the chat's model:
print(chat.preferred_model_type)
print(chat.model_preference_version)

# Set global defaults:
await client.account.set_model_preference("MODEL_TYPE_DEEP_SYNTH_LITE")
await client.account.set_output_style("creative")

# Read current settings:
pref = await client.account.fetch_model_preference()
style = await client.account.fetch_output_style()
```

### Images

```Python
# Generate images from text:
images = await client.utils.generate_image("a cyberpunk city at night")

# Upload an avatar (requires web_next_auth):
avatar = await client.utils.upload_avatar("path/or/url/to/image.jpg")
```

### Voices

```Python
# Search voices:
voices = await client.utils.search_voices("friendly")

# Upload a voice clip:
voice = await client.utils.upload_voice("path/or/url/to/audio.mp3", "My Voice")

# Assign a voice to a character:
await client.account.set_voice("character_id", "voice_id")
await client.account.unset_voice("character_id")

# Generate speech from a chat message:
speech = await client.utils.generate_speech("chat_id", "turn_id", "candidate_id", "voice_id")
with open("voice.mp3", "wb") as f:
    f.write(speech)

# Or just get the URL:
url = await client.utils.generate_speech("chat_id", "turn_id", "candidate_id", "voice_id", return_url=True)
```

---

## Special thanks

- [PyCharacterAI](https://github.com/Xtr4F/PyCharacterAI) by XtraF — the original library this fork builds on.
- [node_characterai](https://github.com/realcoloride/node_characterai) by @realcoloride — backbone of the project in its early days.
- [CharacterAI](https://github.com/kramcat/CharacterAI) by @kramcat — inspiration for the original.
