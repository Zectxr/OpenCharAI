# Chat types

---

### `Chat` class

Represents a chat v2 session.

| Field | Type | Description |
|-------|------|-------------|
| `chat_id` | `str` | Chat ID |
| `character_id` | `str` | Character ID |
| `creator_id` | `str` | Chat creator's account ID |
| `create_time` | `Optional[datetime]` | Creation timestamp |
| `state` | `str` | Chat state (e.g. `"STATE_ACTIVE"`) |
| `chat_type` | `str` | Chat type (e.g. `"TYPE_ONE_ON_ONE"`) |
| `visibility` | `str` | `"public"`, `"unlisted"`, or `"private"` |
| `preview_turns` | `List[Turn]` | Preview of recent messages |
| `chat_name` | `Optional[str]` | Custom chat name |
| `preferred_model_type` | `Optional[str]` | Model used for this chat (e.g. `"MODEL_TYPE_DEEP_SYNTH_LITE"`) |
| `model_preference_version` | `Optional[str]` | Version of the model preference |
| `character_name` | `Optional[str]` | Character name (only in `fetch_recent_chats()`) |
| `character_avatar` | `Optional[Avatar]` | Character avatar (only in `fetch_recent_chats()`) |

---

### `ChatHistory` class

Represents a chat v1 history session.

> ⚠️ This is the legacy format. Use `Chat` (v2) for all new development.

| Field | Type | Description |
|-------|------|-------------|
| `chat_id` | `str` | History ID |
| `create_time` | `Optional[datetime]` | Creation timestamp |
| `last_interaction` | `Optional[datetime]` | Last interaction timestamp |
| `preview_messages` | `List[HistoryMessage]` | Preview of recent messages |

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../../methods.md)
- [Types](../types.md)
  - [User](user.md)
  - [Character](character.md)
  - **Chat** ← you're here
  - [Message](message.md)
  - [Media](media.md)
