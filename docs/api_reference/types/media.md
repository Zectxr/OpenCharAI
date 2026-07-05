# Media types

---

### `Avatar` class

Represents an avatar image.

**Methods:**

#### `get_file_name()`

```python
def get_file_name() -> str
```

Returns the avatar file name (also known as `avatar_rel_path`).

#### `get_url()`

```python
def get_url(size: int = 400, animated: bool = False) -> str
```

Returns a URL to the avatar image.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `size` | `int` | `400` | Image size. Must be `80`, `200`, or `400`. |
| `animated` | `bool` | `False` | Enable animation |

---

### `Voice` class

Represents a character voice.

| Field | Type | Description |
|-------|------|-------------|
| `voice_id` | `str` | Voice ID |
| `name` | `str` | Voice name |
| `description` | `str` | Voice description |
| `gender` | `str` | Voice gender |
| `visibility` | `str` | `"public"`, `"unlisted"`, or `"private"` |
| `preview_audio_url` | `Optional[str]` | Preview audio URL |
| `preview_text` | `str` | Preview text for the voice |
| `creator_id` | `Optional[str]` | Creator's account ID |
| `creator_username` | `Optional[str]` | Creator's username |
| `internal_status` | `str` | Internal processing status |
| `last_update_time` | `Optional[datetime]` | Last update timestamp |

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../../methods.md)
- [Types](../types.md)
  - [User](user.md)
  - [Character](character.md)
  - [Chat](chat.md)
  - [Message](message.md)
  - **Media** ← you're here
