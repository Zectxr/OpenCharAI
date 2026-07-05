# Methods

All methods are grouped into five categories. Call them through the client:

```python
client.account.method_name()
client.character.method_name()
client.chat.method_name()
client.user.method_name()
client.utils.method_name()
```

---

## Account

| Method | Returns |
|--------|---------|
| `fetch_me()` | [`Account`](../types/user.md#account-class) |
| `fetch_my_settings()` | `Dict` |
| `fetch_my_followers()` | `List[str]` |
| `fetch_my_following()` | `List[str]` |
| `fetch_my_persona(persona_id)` | [`Persona`](../types/user.md#persona-class) |
| `fetch_my_personas()` | `List[Persona]` |
| `fetch_my_characters()` | `List[CharacterShort]` |
| `fetch_my_upvoted_characters()` | `List[CharacterShort]` |
| `fetch_my_voices()` | `List[Voice]` |
| `edit_account(name, username, bio, avatar_rel_path)` | `bool` |
| `create_persona(name, definition, avatar_rel_path)` | [`Persona`](../types/user.md#persona-class) |
| `edit_persona(persona_id, name, definition, avatar_rel_path)` | [`Persona`](../types/user.md#persona-class) |
| `delete_persona(persona_id)` | `bool` |
| `set_default_persona(persona_id)` | `bool` |
| `unset_default_persona()` | `bool` |
| `set_persona(character_id, persona_id)` | `bool` |
| `unset_persona(character_id)` | `bool` |
| `set_voice(character_id, voice_id)` | `bool` |
| `unset_voice(character_id)` | `bool` |
| `fetch_model_preference()` | `Dict` |
| `set_model_preference(model_type)` | `bool` |
| `fetch_output_style()` | `Optional[Dict]` |
| `set_output_style(style)` | `bool` |

[Full documentation →](methods/account.md)

---

## Character

| Method | Returns |
|--------|---------|
| `fetch_characters_by_category()` | `Dict[str, List[CharacterShort]]` |
| `fetch_recommended_characters()` | `List[CharacterShort]` |
| `fetch_featured_characters()` | `List[CharacterShort]` |
| `fetch_similar_characters(character_id)` | `List[CharacterShort]` |
| `fetch_character_info(character_id)` | [`Character`](../types/character.md#character-class) |
| `search_characters(character_name)` | `List[CharacterShort]` |
| `search_creators(creator_name)` | `List[str]` |
| `character_vote(character_id, vote)` | `bool` |
| `create_character(name, greeting, ...)` | [`Character`](../types/character.md#character-class) |
| `edit_character(character_id, name, greeting, ...)` | [`Character`](../types/character.md#character-class) |

[Full documentation →](methods/character.md)

---

## Chat

| Method | Returns |
|--------|---------|
| `fetch_histories(character_id, amount)` | `List[ChatHistory]` |
| `fetch_chats(character_id)` | `List[Chat]` |
| `fetch_chat(chat_id)` | [`Chat`](../types/chat.md#chat-class) |
| `fetch_recent_chats()` | `List[Chat]` |
| `fetch_messages(chat_id, pinned_only, next_token)` | `Tuple[List[Turn], Optional[str]]` |
| `fetch_all_messages(chat_id, pinned_only)` | `List[Turn]` |
| `fetch_following_messages(chat_id, turn_id, pinned_only)` | `List[Turn]` |
| `fetch_pinned_messages(chat_id, next_token)` | `Tuple[List[Turn], Optional[str]]` |
| `fetch_all_pinned_messages(chat_id)` | `List[Turn]` |
| `update_chat_name(chat_id, name)` | `bool` |
| `archive_chat(chat_id)` | `bool` |
| `unarchive_chat(chat_id)` | `bool` |
| `copy_chat(chat_id, end_turn_id)` | `Optional[str]` |
| `create_chat(character_id, greeting, **kwargs)` | `Tuple[Chat, Optional[Turn]]` |
| `update_primary_candidate(chat_id, turn_id, candidate_id)` | `bool` |
| `send_message(character_id, chat_id, text, streaming)` | `Union[Turn, AsyncGenerator]` |
| `another_response(character_id, chat_id, turn_id, streaming)` | `Union[Turn, AsyncGenerator]` |
| `edit_message(chat_id, turn_id, candidate_id, text)` | [`Turn`](../types/message.md#turn-class) |
| `delete_messages(chat_id, turn_ids)` | `bool` |
| `delete_message(chat_id, turn_id)` | `bool` |
| `pin_message(chat_id, turn_id)` | `bool` |
| `unpin_message(chat_id, turn_id)` | `bool` |

[Full documentation →](methods/chat.md)

---

## User

| Method | Returns |
|--------|---------|
| `fetch_user(username)` | `Optional[PublicUser]` |
| `fetch_user_voices(username)` | `List[Voice]` |
| `follow_user(username)` | `bool` |
| `unfollow_user(username)` | `bool` |

[Full documentation →](methods/user.md)

---

## Utils

| Method | Returns |
|--------|---------|
| `ping()` | `bool` |
| `fetch_voice(voice_id)` | [`Voice`](../types/media.md#voice-class) |
| `search_voices(voice_name)` | `List[Voice]` |
| `generate_image(prompt)` | `List[str]` |
| `upload_avatar(image, check_image)` | [`Avatar`](../types/media.md#avatar-class) |
| `upload_voice(voice, name, description, visibility)` | [`Voice`](../types/media.md#voice-class) |
| `edit_voice(voice, name, description, visibility)` | [`Voice`](../types/media.md#voice-class) |
| `delete_voice(voice_id)` | `bool` |
| `generate_speech(chat_id, turn_id, candidate_id, voice_id)` | `Union[bytes, str]` |

[Full documentation →](methods/utils.md)

---

## Navigation

- [Welcome](../welcome.md)
- [Getting started](../getting_started.md)
- **Methods** ← you're here
  - [Account](methods/account.md)
  - [Character](methods/character.md)
  - [Chat](methods/chat.md)
  - [User](methods/user.md)
  - [Utils](methods/utils.md)
- [Types](../types.md)
  - [Account / User](../types/user.md)
  - [Character](../types/character.md)
  - [Chat](../types/chat.md)
  - [Message](../types/message.md)
  - [Media](../types/media.md)
