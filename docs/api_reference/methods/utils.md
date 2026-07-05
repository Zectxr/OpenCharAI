# Utils methods

---

### `ping`

```python
async def ping() -> bool
```

Checks API connectivity.

**Returns:** `bool`

---

### `fetch_voice`

```python
async def fetch_voice(voice_id: str) -> Voice
```

**Returns:** [`Voice`](../types/media.md#voice-class)

---

### `search_voices`

```python
async def search_voices(voice_name: str) -> List[Voice]
```

```python
voices = await client.utils.search_voices("soft")
for v in voices:
    print(f"{v.name} — {v.voice_id}")
```

**Returns:** `List[Voice]`

---

### `generate_image`

```python
async def generate_image(prompt: str, **kwargs) -> List[str]
```

Generates images from a text prompt. Returns a list of image URLs.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `prompt` | `str` | — | Image description |
| `num_candidates` (kwarg) | `int` | `4` | Number of images to generate |

```python
images = await client.utils.generate_image("a sunset over mountains", num_candidates=4)
for url in images:
    print(url)
```

**Returns:** `List[str]`

---

### `upload_avatar`

```python
async def upload_avatar(image: str, check_image: bool = True) -> Avatar
```

Uploads an image to use as an avatar.

> **Note:** Requires the `web_next_auth` token to be set during authentication.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `image` | `str` | — | File path or URL |
| `check_image` | `bool` | `True` | Verify the uploaded image is accessible |

```python
avatar = await client.utils.upload_avatar("path/to/image.jpg")
print(avatar.get_url())
```

**Returns:** [`Avatar`](../types/media.md#avatar-class)

---

### `upload_voice`

```python
async def upload_voice(
    voice: Union[str, bytes],
    name: str,
    description: str = "",
    visibility: str = "private",
) -> Voice
```

Uploads audio as a character voice.

| Param | Type | Constraints |
|-------|------|-------------|
| `voice` | `str` or `bytes` | File path, URL, or raw bytes |
| `name` | `str` | 3–20 characters |
| `description` | `str` | ≤120 characters |
| `visibility` | `str` | `"public"` or `"private"` |

```python
voice = await client.utils.upload_voice("path/to/audio.mp3", "My Voice")
print(f"Uploaded: {voice.voice_id}")
```

**Returns:** [`Voice`](../types/media.md#voice-class)

---

### `edit_voice`

```python
async def edit_voice(
    voice: Union[str, Voice],
    name: Optional[str] = None,
    description: Optional[str] = None,
    visibility: str = "private",
) -> Voice
```

| Param | Type | Description |
|-------|------|-------------|
| `voice` | `str` or `Voice` | Voice ID or Voice object |
| `name` | `Optional[str]` | New name (3–20 chars) |
| `description` | `Optional[str]` | New description (≤120 chars) |
| `visibility` | `str` | `"public"` or `"private"` |

**Returns:** [`Voice`](../types/media.md#voice-class)

---

### `delete_voice`

```python
async def delete_voice(voice_id: str) -> bool
```

**Returns:** `bool`

---

### `generate_speech`

```python
async def generate_speech(
    chat_id: str,
    turn_id: str,
    candidate_id: str,
    voice_id: str,
    **kwargs,
) -> Union[bytes, str]
```

Generates speech audio from a character's message.

| Param | Type | Description |
|-------|------|-------------|
| `chat_id` | `str` | ID of the chat |
| `turn_id` | `str` | ID of the turn (message) |
| `candidate_id` | `str` | ID of the candidate |
| `voice_id` | `str` | ID of the voice |

**Kwargs:**

| Kwarg | Type | Default | Description |
|-------|------|---------|-------------|
| `return_url` | `bool` | `False` | Return the audio URL instead of raw bytes |

```python
# Get raw audio bytes
audio = await client.utils.generate_speech(chat_id, turn_id, candidate_id, voice_id)
with open("output.mp3", "wb") as f:
    f.write(audio)

# Get the URL instead
url = await client.utils.generate_speech(chat_id, turn_id, candidate_id, voice_id, return_url=True)
```

**Returns:** `bytes` or `str`

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../methods.md)
  - [Account](account.md)
  - [Character](character.md)
  - [Chat](chat.md)
  - [User](user.md)
  - **Utils** ← you're here
- [Types](../types.md)
