# Chat methods

---

### `fetch_histories`

```python
async def fetch_histories(character_id: str, amount: int = 50) -> List[ChatHistory]
```

Fetches your chat v1 histories with a character.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `character_id` | `str` | — | ID of the character |
| `amount` | `int` | `50` | Number of histories to fetch |

**Returns:** `List[ChatHistory]`

---

### `fetch_chats`

```python
async def fetch_chats(character_id: str) -> List[Chat]
```

Fetches your chat v2 sessions with a character.

**Returns:** `List[Chat]`

---

### `fetch_chat`

```python
async def fetch_chat(chat_id: str) -> Chat
```

**Returns:** [`Chat`](../types/chat.md#chat-class)

---

### `fetch_recent_chats`

```python
async def fetch_recent_chats() -> List[Chat]
```

```python
chats = await client.chat.fetch_recent_chats()
for chat in chats:
    print(f"{chat.character_name} — {chat.chat_id}")
```

**Returns:** `List[Chat]`

---

### `fetch_messages`

```python
async def fetch_messages(
    chat_id: str,
    pinned_only: bool = False,
    next_token: Optional[str] = None,
) -> Tuple[List[Turn], Optional[str]]
```

Fetches messages in a chat. Returns a tuple of `(messages, next_token)`. If `next_token` is not `None`, more messages are available.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `chat_id` | `str` | — | ID of the chat |
| `pinned_only` | `bool` | `False` | Only fetch pinned messages |
| `next_token` | `Optional[str]` | `None` | Pagination token |

```python
messages, next_token = await client.chat.fetch_messages(chat_id)
for msg in messages:
    print(f"[{msg.author_name}]: {msg.get_primary_candidate().text}")

while next_token:
    messages, next_token = await client.chat.fetch_messages(chat_id, next_token=next_token)
    for msg in messages:
        print(f"[{msg.author_name}]: {msg.get_primary_candidate().text}")
```

**Returns:** `Tuple[List[Turn], Optional[str]]`

---

### `fetch_all_messages`

```python
async def fetch_all_messages(chat_id: str, pinned_only: bool = False) -> List[Turn]
```

Fetches **all** messages in a chat by automatically paginating.

**Returns:** `List[Turn]`

---

### `fetch_pinned_messages`

```python
async def fetch_pinned_messages(
    chat_id: str,
    next_token: Optional[str] = None,
) -> Tuple[List[Turn], Optional[str]]
```

**Returns:** `Tuple[List[Turn], Optional[str]]`

---

### `fetch_all_pinned_messages`

```python
async def fetch_all_pinned_messages(chat_id: str) -> List[Turn]
```

**Returns:** `List[Turn]`

---

### `fetch_following_messages`

```python
async def fetch_following_messages(
    chat_id: str,
    turn_id: str,
    pinned_only: bool = False,
) -> List[Turn]
```

Fetches all messages after a specific turn in a chat.

| Param | Type | Description |
|-------|------|-------------|
| `chat_id` | `str` | ID of the chat |
| `turn_id` | `str` | Reference turn ID |
| `pinned_only` | `bool` | Only fetch pinned messages |

**Returns:** `List[Turn]`

---

### `update_chat_name`

```python
async def update_chat_name(chat_id: str, name: str) -> bool
```

**Returns:** `bool`

---

### `archive_chat`

```python
async def archive_chat(chat_id: str) -> bool
```

**Returns:** `bool`

---

### `unarchive_chat`

```python
async def unarchive_chat(chat_id: str) -> bool
```

**Returns:** `bool`

---

### `copy_chat`

```python
async def copy_chat(chat_id: str, end_turn_id: str) -> Optional[str]
```

Copies all messages up to `end_turn_id` into a new chat. Returns the new chat's ID.

**Returns:** `Optional[str]`

---

### `create_chat`

```python
async def create_chat(
    character_id: str,
    greeting: bool = True,
    **kwargs,
) -> Tuple[Chat, Optional[Turn]]
```

Creates a new chat with a character.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `character_id` | `str` | — | ID of the character |
| `greeting` | `bool` | `True` | Whether to generate a greeting message |

**Keyword arguments:**

| Kwarg | Type | Description |
|-------|------|-------------|
| `model_type` | `str` | Model to use (e.g. `"MODEL_TYPE_DEEP_SYNTH_LITE"`) |
| `output_style` | `str` | Chat style (`"creative"`, `"balanced"`, `"precise"`, `"default"`) |

```python
# Basic usage
chat, greeting = await client.chat.create_chat(character_id)

# With model type and output style
chat, greeting = await client.chat.create_chat(
    character_id,
    model_type="MODEL_TYPE_DEEP_SYNTH_LITE",
    output_style="creative",
)

# Skip the greeting
chat, _ = await client.chat.create_chat(character_id, greeting=False)
```

**Returns:** `Tuple[Chat, Optional[Turn]]`

---

### `update_primary_candidate`

```python
async def update_primary_candidate(chat_id: str, turn_id: str, candidate_id: str) -> bool
```

Sets the primary candidate for a turn (swipes to a specific response).

**Returns:** `bool`

---

### `send_message`

```python
async def send_message(
    character_id: str,
    chat_id: str,
    text: str,
    streaming: bool = False,
) -> Union[Turn, AsyncGenerator[Turn, Any]]
```

Sends a message to the character. When `streaming=True`, returns an async generator that yields partial turn updates as they're generated.

```python
# Without streaming
answer = await client.chat.send_message(character_id, chat_id, "Hello!")
print(answer.get_primary_candidate().text)

# With streaming
stream = await client.chat.send_message(character_id, chat_id, "Hello!", streaming=True)
async for chunk in stream:
    print(chunk.get_primary_candidate().text)
```

**Returns:** [`Turn`](../types/message.md#turn-class) or `AsyncGenerator[Turn]`

---

### `another_response`

```python
async def another_response(
    character_id: str,
    chat_id: str,
    turn_id: str,
    streaming: bool = False,
) -> Union[Turn, AsyncGenerator[Turn, Any]]
```

Generates an alternative response for a specific turn (equivalent to swiping on the website).

**Returns:** [`Turn`](../types/message.md#turn-class) or `AsyncGenerator[Turn]`

---

### `edit_message`

```python
async def edit_message(chat_id: str, turn_id: str, candidate_id: str, text: str) -> Turn
```

Edits a candidate's text.

**Returns:** [`Turn`](../types/message.md#turn-class)

---

### `delete_messages`

```python
async def delete_messages(chat_id: str, turn_ids: List[str]) -> bool
```

Deletes multiple messages.

**Returns:** `bool`

---

### `delete_message`

```python
async def delete_message(chat_id: str, turn_id: str) -> bool
```

**Returns:** `bool`

---

### `pin_message`

```python
async def pin_message(chat_id: str, turn_id: str) -> bool
```

**Returns:** `bool`

---

### `unpin_message`

```python
async def unpin_message(chat_id: str, turn_id: str) -> bool
```

**Returns:** `bool`

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../methods.md)
  - [Account](account.md)
  - [Character](character.md)
  - **Chat** ← you're here
  - [User](user.md)
  - [Utils](utils.md)
- [Types](../types.md)
