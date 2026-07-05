# Character methods

---

### `fetch_characters_by_category`

```python
async def fetch_characters_by_category() -> Dict[str, List[CharacterShort]]
```

Returns characters grouped by category.

```python
chars = await client.character.fetch_characters_by_category()
for category, characters in chars.items():
    print(f"{category}: {len(characters)} characters")
```

**Returns:** `Dict[str, List[CharacterShort]]`

---

### `fetch_recommended_characters`

```python
async def fetch_recommended_characters() -> List[CharacterShort]
```

**Returns:** `List[CharacterShort]`

---

### `fetch_featured_characters`

```python
async def fetch_featured_characters() -> List[CharacterShort]
```

**Returns:** `List[CharacterShort]`

---

### `fetch_similar_characters`

```python
async def fetch_similar_characters(character_id: str) -> List[CharacterShort]
```

| Param | Type | Description |
|-------|------|-------------|
| `character_id` | `str` | ID of the character |

**Returns:** `List[CharacterShort]`

---

### `fetch_character_info`

```python
async def fetch_character_info(character_id: str) -> Character
```

Fetches full information about a character, including definition, image settings, and voice configuration.

| Param | Type | Description |
|-------|------|-------------|
| `character_id` | `str` | ID of the character |

**Returns:** [`Character`](../types/character.md#character-class)

---

### `search_characters`

```python
async def search_characters(character_name: str) -> List[CharacterShort]
```

Searches for characters by name.

```python
results = await client.character.search_characters("assistant")
for c in results:
    print(f"{c.name} — {c.character_id}")
```

**Returns:** `List[CharacterShort]`

---

### `search_creators`

```python
async def search_creators(creator_name: str) -> List[str]
```

Searches for creators by name. Returns a list of matching usernames.

**Returns:** `List[str]`

---

### `character_vote`

```python
async def character_vote(character_id: str, vote: Optional[bool]) -> bool
```

| Param | Type | Description |
|-------|------|-------------|
| `character_id` | `str` | ID of the character |
| `vote` | `Optional[bool]` | `True` = like, `False` = dislike, `None` = remove vote |

**Returns:** `bool`

---

### `create_character`

```python
async def create_character(
    name: str,
    greeting: str,
    title: str = "",
    description: str = "",
    definition: str = "",
    copyable: bool = False,
    visibility: str = "private",
    avatar_rel_path: str = "",
    default_voice_id: str = "",
) -> Character
```

| Param | Type | Constraints |
|-------|------|-------------|
| `name` | `str` | 3–20 characters |
| `greeting` | `str` | 3–4096 characters |
| `title` | `str` | 3–50 characters |
| `description` | `str` | ≤500 characters |
| `definition` | `str` | ≤32000 characters |
| `copyable` | `bool` | Whether definition is visible to others |
| `visibility` | `str` | `"public"`, `"unlisted"`, or `"private"` |
| `avatar_rel_path` | `str` | Filename on CAI server |
| `default_voice_id` | `str` | Default voice for the character |

**Returns:** [`Character`](../types/character.md#character-class)

---

### `edit_character`

```python
async def edit_character(
    character_id: str,
    name: str,
    greeting: str,
    title: str = "",
    description: str = "",
    definition: str = "",
    copyable: bool = False,
    visibility: str = "private",
    avatar_rel_path: str = "",
    default_voice_id: str = "",
) -> Character
```

Same parameters as `create_character`, plus `character_id` to specify which character to edit.

**Returns:** [`Character`](../types/character.md#character-class)

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../methods.md)
  - [Account](account.md)
  - **Character** ← you're here
  - [Chat](chat.md)
  - [User](user.md)
  - [Utils](utils.md)
- [Types](../types.md)
