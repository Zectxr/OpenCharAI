# Account methods

---

### `fetch_me`

```python
async def fetch_me() -> Account
```

Fetches your account information.

```python
account = await client.account.fetch_me()
print(f"@{account.username} — {account.name}")
```

**Returns:** [`Account`](../types/user.md#account-class)

---

### `fetch_my_settings`

```python
async def fetch_my_settings() -> Dict
```

Fetches your account settings, including persona overrides, voice overrides, model preferences, and output style settings.

```python
settings = await client.account.fetch_my_settings()
default_persona = settings.get("default_persona_id")
voice_overrides = settings.get("voiceOverrides", {})
```

**Returns:** `Dict`

---

### `fetch_my_followers`

```python
async def fetch_my_followers() -> List
```

**Returns:** `List[str]`

---

### `fetch_my_following`

```python
async def fetch_my_following() -> List
```

**Returns:** `List[str]`

---

### `fetch_my_persona`

```python
async def fetch_my_persona(persona_id: str) -> Persona
```

| Param | Type | Description |
|-------|------|-------------|
| `persona_id` | `str` | ID of your persona |

**Returns:** [`Persona`](../types/user.md#persona-class)

---

### `fetch_my_personas`

```python
async def fetch_my_personas() -> List[Persona]
```

```python
personas = await client.account.fetch_my_personas()
for p in personas:
    print(f"{p.name} — {p.persona_id}")
```

**Returns:** `List[Persona]`

---

### `fetch_my_characters`

```python
async def fetch_my_characters() -> List[CharacterShort]
```

**Returns:** `List[CharacterShort]`

---

### `fetch_my_upvoted_characters`

```python
async def fetch_my_upvoted_characters() -> List[CharacterShort]
```

**Returns:** `List[CharacterShort]`

---

### `fetch_my_voices`

```python
async def fetch_my_voices() -> List[Voice]
```

**Returns:** `List[Voice]`

---

### `edit_account`

```python
async def edit_account(name: str, username: str, bio: str = "", avatar_rel_path: str = "") -> bool
```

| Param | Type | Constraints |
|-------|------|-------------|
| `name` | `str` | 2–50 characters |
| `username` | `str` | 2–20 characters |
| `bio` | `str` | ≤500 characters |
| `avatar_rel_path` | `str` | Filename on CAI server |

**Returns:** `bool`

---

### `create_persona`

```python
async def create_persona(name: str, definition: str = "", avatar_rel_path: str = "") -> Persona
```

| Param | Type | Constraints |
|-------|------|-------------|
| `name` | `str` | 3–20 characters |
| `definition` | `str` | ≤750 characters |
| `avatar_rel_path` | `str` | Filename on CAI server |

**Returns:** [`Persona`](../types/user.md#persona-class)

---

### `edit_persona`

```python
async def edit_persona(persona_id: str, name: str = "", definition: str = "", avatar_rel_path: str = "") -> Persona
```

**Returns:** [`Persona`](../types/user.md#persona-class)

---

### `delete_persona`

```python
async def delete_persona(persona_id: str) -> bool
```

**Returns:** `bool`

---

### `set_default_persona`

```python
async def set_default_persona(persona_id: Optional[str]) -> bool
```

Sets a persona as the default for all characters without a specific override. Pass `None` to unset.

**Returns:** `bool`

---

### `unset_default_persona`

```python
async def unset_default_persona() -> bool
```

---

### `set_persona`

```python
async def set_persona(character_id: str, persona_id: Optional[str]) -> bool
```

Sets a persona override for a specific character. Pass `None` to clear.

**Returns:** `bool`

---

### `unset_persona`

```python
async def unset_persona(character_id: str) -> bool
```

---

### `set_voice`

```python
async def set_voice(character_id: str, voice_id: Optional[str]) -> bool
```

Sets a voice override for a character. Pass `None` to clear.

**Returns:** `bool`

---

### `unset_voice`

```python
async def unset_voice(character_id: str) -> bool
```

---

### `fetch_model_preference`

```python
async def fetch_model_preference() -> Dict
```

Returns your current model preference settings, e.g. `{"defaultModelType": "MODEL_TYPE_DEEP_SYNTH_LITE"}`.

**Returns:** `Dict`

---

### `set_model_preference`

```python
async def set_model_preference(model_type: str) -> bool
```

Sets your default model type. Common values:

| Model type | Description |
|------------|-------------|
| `MODEL_TYPE_DEEP_SYNTH_LITE` | Latest default model (PipSqueak 2) |
| `MODEL_TYPE_SMART` | Smart/thoughtful responses |
| `MODEL_TYPE_BALANCED` | Balanced responses |
| `MODEL_TYPE_FAST` | Fast responses |
| `MODEL_TYPE_FAMILY_FRIENDLY` | Family-friendly mode |

**Returns:** `bool`

---

### `fetch_output_style`

```python
async def fetch_output_style() -> Optional[Dict]
```

Returns your current output style settings, e.g. `{"style": "creative"}`. Returns `None` if not set.

**Returns:** `Optional[Dict]`

---

### `set_output_style`

```python
async def set_output_style(style: str) -> bool
```

Sets your output style. Available styles:

| Style | Description |
|-------|-------------|
| `creative` | More creative and varied responses |
| `balanced` | Balanced between creative and precise |
| `precise` | More focused and direct responses |
| `default` | Default style |

**Returns:** `bool`

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../methods.md)
  - **Account** ← you're here
  - [Character](character.md)
  - [Chat](chat.md)
  - [User](user.md)
  - [Utils](utils.md)
- [Types](../types.md)
