# Message types

---

### `Turn` class

Represents a single message in a chat v2 session.

| Field | Type | Description |
|-------|------|-------------|
| `chat_id` | `str` | Chat ID |
| `turn_id` | `str` | Turn (message) ID |
| `create_time` | `Optional[datetime]` | Creation timestamp |
| `last_update_time` | `Optional[datetime]` | Last update timestamp |
| `state` | `str` | Turn state |
| `author_id` | `str` | Author's account ID |
| `author_name` | `str` | Author's display name |
| `author_is_human` | `bool` | Whether the author is human |
| `candidates` | `Dict[str, TurnCandidate]` | All candidates (keyed by candidate ID) |
| `primary_candidate_id` | `Optional[str]` | Currently selected candidate ID |

**Methods:**

#### `get_candidates()`

```python
def get_candidates() -> List[TurnCandidate]
```

Returns all candidates as a list.

#### `get_primary_candidate()`

```python
def get_primary_candidate() -> Optional[TurnCandidate]
```

Returns the currently selected candidate, or `None`.

---

### `TurnCandidate` class

Represents one version of a message's content (swipes create new candidates).

| Field | Type | Description |
|-------|------|-------------|
| `candidate_id` | `str` | Candidate ID |
| `text` | `str` | Message text content |
| `is_final` | `bool` | Whether generation is complete |
| `is_filtered` | `bool` | Whether the content was filtered |
| `create_time` | `Optional[datetime]` | Creation timestamp |

---

### `HistoryMessage` class

Represents a message in a chat v1 history session.

> ⚠️ Legacy format. Use `Turn` for new development.

| Field | Type | Description |
|-------|------|-------------|
| `uuid` | `str` | Message UUID |
| `id` | `str` | Message ID |
| `text` | `str` | Message text |
| `src` | `Dict` | Source data |
| `tgt` | `Dict` | Target data |
| `is_alternative` | `bool` | Whether this is an alternative |
| `image_relative_path` | `str` | Image path if applicable |

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../../methods.md)
- [Types](../types.md)
  - [User](user.md)
  - [Character](character.md)
  - [Chat](chat.md)
  - **Message** ← you're here
  - [Media](media.md)
