# User methods

---

### `fetch_user`

```python
async def fetch_user(username: str) -> Optional[PublicUser]
```

Fetches a user's public profile by username.

| Param | Type | Description |
|-------|------|-------------|
| `username` | `str` | Username of the user |

**Returns:** [`PublicUser`](../types/user.md#publicuser-class) or `None` if not found

---

### `fetch_user_voices`

```python
async def fetch_user_voices(username: str) -> List[Voice]
```

Fetches the public voices created by a user.

**Returns:** `List[Voice]`

---

### `follow_user`

```python
async def follow_user(username: str) -> bool
```

**Returns:** `bool`

---

### `unfollow_user`

```python
async def unfollow_user(username: str) -> bool
```

**Returns:** `bool`

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../methods.md)
  - [Account](account.md)
  - [Character](character.md)
  - [Chat](chat.md)
  - **User** ← you're here
  - [Utils](utils.md)
- [Types](../types.md)
