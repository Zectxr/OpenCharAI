# Character types

---

### `CharacterShort` class

Short representation of a character (used in search results and listings).

| Field | Type | Description |
|-------|------|-------------|
| `character_id` | `str` | Unique character ID |
| `title` | `str` | Character title |
| `name` | `str` | Character name |
| `visibility` | `str` | `"public"`, `"unlisted"`, or `"private"` |
| `greeting` | `str` | Initial greeting message |
| `description` | `str` | Character description |
| `definition` | `str` | Character definition |
| `upvotes` | `Optional[int]` | Number of upvotes |
| `author_username` | `Optional[str]` | Creator's username |
| `num_interactions` | `Optional[int]` | Total interaction count |
| `avatar` | `Optional[Avatar]` | Character avatar |

---

### `Character` class

Full representation of a character (returned by `fetch_character_info` and `create_character`).

Includes all `CharacterShort` fields, plus:

| Field | Type | Description |
|-------|------|-------------|
| `copyable` | `bool` | Whether the definition is visible to others |
| `identifier` | `str` | Character identifier |
| `img_gen_enabled` | `bool` | Whether image generation is enabled |
| `base_img_prompt` | `str` | Base prompt for image generation |
| `img_prompt_regex` | `str` | Regex for image prompts |
| `strip_img_prompt_from_msg` | `bool` | Whether to strip prompt from messages |
| `starter_prompts` | `Dict` | Suggested conversation starters |
| `comments_enabled` | `bool` | Whether comments are enabled |
| `internal_id` | `str` | Internal system ID |
| `voice_id` | `str` | Assigned voice ID |
| `default_voice_id` | `str` | Default voice ID |
| `songs` | `List` | Associated songs |

---

## Navigation

- [Welcome](../../welcome.md)
- [Getting started](../../getting_started.md)
- [Methods](../../methods.md)
- [Types](../types.md)
  - [User](user.md)
  - **Character** ← you're here
  - [Chat](chat.md)
  - [Message](message.md)
  - [Media](media.md)
