# Python TelegramBots

A pure and modern python package to communicate with telegram bot api.

## About

This is an async wrapper over telegram bot api written using python ( + 3.10 ).

This package tries to be close to the bot api interface and there are almost
nothing more than it. Of course the package is extendable and other features
can be installed separately.

- All objects and methods ( 6.0 ) are implemented in python using `dataclass`es.

- The serialization stuff are done to convert api python objects to json-like (`dict`, `list`) objects and then json-string and reverse.

- A simple and async http client is available using aiohttp to send requests

_This package contains no full-featured client or bound methods! there're only some classes and a client._

## How to

All api methods are available under following namespace:

```py
telegrambots.wrapper.types.methods
```

And for objects

```py
telegrambots.wrapper.types.methods
```

### Make a request

You can use our async client to make requests.

```py
import asyncio

from src.telegrambots.wrapper import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendMessage
from src.telegrambots.wrapper.types.objects import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def main():
    client = TelegramBotsClient("BOT_TOKEN")

    message = await client(
        SendMessage(
            123456789,
            "Here is a message from python-telegrambots",
            reply_markup=InlineKeyboardMarkup(
                InlineKeyboardButton.with_url(
                    "Repo", "https://github.com/python-telegrambots"
                )
            ),
        )
    )

    print(message.message_id)


if __name__ == "__main__":
    asyncio.run(main())

```

_Everything is documented and well type hinted._

Send a file or even multiple files ( local or online ).

```py
import asyncio
from pathlib import Path

from src.telegrambots.wrapper import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendMediaGroup
from src.telegrambots.wrapper.types.objects import InputFile, InputMediaPhoto


async def main():
    client = TelegramBotsClient("BOT_TOKEN")

    file_path_1 = Path(__file__).parent.resolve().joinpath("test_photo_1.jpg")
    file_path_2 = Path(__file__).parent.resolve().joinpath("test_photo_2.jpg")

    with InputFile(file_path_1) as file:
        with SendMediaGroup(
            123456789,
            [
                InputMediaPhoto(file, "My first photo"),
                InputMediaPhoto(InputFile(open(file_path_2, "rb"), "test_photo_2.jpg")),
                InputMediaPhoto("https://imgur.com/t/funny/MpMGFRQ"),
            ],
        ) as send_media_group:
            result = await client(send_media_group)

            print(result.__len__())


if __name__ == "__main__":
    asyncio.run(main())
```

Send multiple requests using one `aiohttp.ClientSession`.

``` py
import asyncio

from src.telegrambots.wrapper import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import (
    SendMessage,
    EditMessageText,
    DeleteMessage,
)


async def main():
    client = TelegramBotsClient("BOT_TOKEN")

    async with client:

        message = await client(
            SendMessage(12345678, "It's a long time that want to say ... I love you.")
        )

        edited_message = await client(
            EditMessageText(
                chat_id=message.chat.id,
                message_id=message.message_id,
                text="Oh sorry, how are you today??!",
            )
        )

        assert edited_message

        await client(
            DeleteMessage(
                chat_id=edited_message.chat.id, message_id=edited_message.message_id
            )
        )


if __name__ == "__main__":
    asyncio.run(main())

```

Print things! usual way or pretty.

```py
import asyncio

from src.telegrambots.wrapper import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendMessage


async def main():
    client = TelegramBotsClient("BOT_TOKEN")

    async with client:

        message = await client(SendMessage(12345678, "It's Show Time."))

        # let's see what we got.
        print(message)
        # Message(message_id=134, date=1651407978, chat=Chat(id=106296897, ...
        # ---- A long story here ----

        # make it more clear
        print(message.pretty_str())
        # {
        #     "chat": {
        #         "first_name": "A̤̮ʀαՏH",
        #         "id": 12345678,
        #         "type": "private"
        #     },
        #     "date": 1651407978,
        #     "from": {
        #         "first_name": "TelegramBots Test",
        #         "id": 87654321,
        #         "is_bot": true,
        #         "username": "TestBot"
        #     },
        #     "message_id": 134,
        #     "text": "It's Show Time."
        # }

if __name__ == "__main__":
    asyncio.run(main())
```

## Install

_The preview package is available at [PYPI](https://pypi.org/project/telegrambots)._
