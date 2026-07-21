import asyncio

from OpenCharAI import get_client
from OpenCharAI.exceptions import SessionClosedError

token = "TOKEN"
character_id = "ID"


async def main():
    client = await get_client(token=token)

    me = await client.account.fetch_me()
    print(f"Authenticated as @{me.username}")

    chat, greeting_message = await client.chat.create_chat(
        character_id,
        model_type="MODEL_TYPE_DEEP_SYNTH_LITE",
    )

    print(f"Using model: {chat.preferred_model_type}")
    print(f"{greeting_message.author_name}: {greeting_message.get_primary_candidate().text}")

    try:
        while True:
            message = input(f"[{me.name}]: ")

            answer = await client.chat.send_message(character_id, chat.chat_id, message)
            print(f"[{answer.author_name}]: {answer.get_primary_candidate().text}")

    except SessionClosedError:
        print("session closed. Bye!")

    finally:
        await client.close_session()


asyncio.run(main())
