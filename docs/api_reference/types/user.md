# User types

---

### `Account` class

Represents your own account.

| Field | Type | Description |
|-------|------|-------------|
| `username` | `str` | Account username |
| `name` | `str` | Display name |
| `bio` | `str` | Biography text |
| `avatar` | `Optional[Avatar]` | Account avatar |
| `account_id` | `str` | Unique account ID |
| `first_name` | `Optional[str]` | First name |
| `avatar_type` | `str` | `"DEFAULT"` or `"UPLOADED"` |
| `is_human` | `bool` | Whether the account belongs to a human |
| `email` | `Optional[str]` | Email address |

---

### `PublicUser` class

Represents another user's public profile.

| Field | Type | Description |
|-------|------|-------------|
| `username` | `str` | Username |
| `name` | `str` | Display name |
| `bio` | `str` | Biography text |
| `avatar` | `Optional[Avatar]` | Avatar |
| `num_following` | `int` | Number of users they follow |
| `num_followers` | `int` | Number of followers |
| `characters` | `List[CharacterShort]` | Their public characters |
| `subscription_type` | `str` | Subscription tier |

---

### `Persona` class

Represents a persona (user角色).

| Field | Type | Description |
|-------|------|-------------|
| `persona_id` | `str` | Persona ID |
| `name` | `str` | Persona name |
| `definition` | `str` | Persona definition text |
| `avatar` | `Optional[Avatar]` | Persona avatar |
| `author_username` | `Optional[str]` | Creator's username |

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../../methods.md)
- [Types](../types.md)
  - **User** ← you're here
  - [Character](character.md)
  - [Chat](chat.md)
  - [Message](message.md)
  - [Media](media.md)
