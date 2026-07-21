# Models

OpenCharAI lets you choose which Character AI model to use, both per-chat and as a global default.

## Available model types

| Constant | Description |
|----------|-------------|
| `MODEL_TYPE_DEEP_SYNTH` | DeepSqueak — premium roleplay model (c.ai+ paid tier) |
| `MODEL_TYPE_DEEP_SYNTH_LITE` | PipSqueak 2 — default free-tier model |
| `MODEL_TYPE_SMART` | Smart/thoughtful responses |
| `MODEL_TYPE_BALANCED` | Balanced responses |
| `MODEL_TYPE_FAST` | Fast responses |
| `MODEL_TYPE_FAMILY_FRIENDLY` | Family-friendly mode |

## Per-chat model

Set the model when creating a chat:

```python
chat, greeting = await client.chat.create_chat(
    character_id,
    model_type="MODEL_TYPE_DEEP_SYNTH_LITE",
)
```

Inspect which model a chat is using:

```python
print(chat.preferred_model_type)        # e.g. "MODEL_TYPE_DEEP_SYNTH_LITE"
print(chat.model_preference_version)    # e.g. "v2"
```

## Global default model

Set your account-wide default model:

```python
await client.account.set_model_preference("MODEL_TYPE_DEEP_SYNTH_LITE")
```

Read your current preference:

```python
pref = await client.account.fetch_model_preference()
print(pref)  # {"defaultModelType": "MODEL_TYPE_DEEP_SYNTH_LITE"}
```

## Output styles

You can also set an output style per-chat or globally:

| Style | Description |
|-------|-------------|
| `creative` | More imaginative responses |
| `balanced` | Balanced creativity and precision |
| `precise` | More focused/deterministic responses |
| `default` | Character AI's default setting |

```python
# Per-chat
chat, greeting = await client.chat.create_chat(
    character_id,
    output_style="creative",
)

# Global default
await client.account.set_output_style("creative")
```

## Full example

See [`docs/examples/simple_example_with_model.py`](examples/simple_example_with_model.py) for a complete runnable example.

## Navigation

- [Welcome](welcome.md)
- [Getting started](getting_started.md)
- **Models** ← you're here
- API Reference:
  - [Methods](api_reference/methods.md)
    - [Account](api_reference/methods/account.md)
    - [Character](api_reference/methods/character.md)
    - [Chat](api_reference/methods/chat.md)
    - [User](api_reference/methods/user.md)
    - [Utils](api_reference/methods/utils.md)
  - [Types](api_reference/types.md)
    - [Account / User](api_reference/types/user.md)
    - [Character](api_reference/types/character.md)
    - [Chat](api_reference/types/chat.md)
    - [Message](api_reference/types/message.md)
    - [Media](api_reference/types/media.md)
