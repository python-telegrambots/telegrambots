import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendMessage
from src.telegrambots.wrapper.types.objects.message_entity import MessageEntity
from src.telegrambots.wrapper.types.objects import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from ...test_config import TestConfigs, test_config  # type: ignore


@pytest.mark.asyncio
async def test_send_text_message(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    message = await client(SendMessage(test_config.private_chat_id_1, "Hello, world!"))

    assert message.message_id
    assert message.chat.id == test_config.private_chat_id_1
    assert message.text == "Hello, world!"

    assert message.from_user is not None
    assert message.from_user.id == test_config.bot_user_id

    assert message.date


@pytest.mark.asyncio
async def test_send_text_message_with_entities(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    message = await client(
        SendMessage(
            test_config.private_chat_id_1,
            "Hello, world!",
            entities=[
                MessageEntity("bold", 0, 5),
            ],
        )
    )

    assert message.message_id
    assert message.chat.id == test_config.private_chat_id_1
    assert message.text == "Hello, world!"

    assert message.from_user is not None
    assert message.from_user.id == test_config.bot_user_id

    assert message.date

    assert message.entities
    assert message.entities[0].type == "bold"


@pytest.mark.asyncio
async def test_send_text_message_with_parse_mode(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    message = await client(
        SendMessage(
            test_config.private_chat_id_1,
            "/test *Hello*, world!",
            parse_mode="markdown",
        )
    )

    assert message.message_id
    assert message.chat.id == test_config.private_chat_id_1
    assert message.text == "/test Hello, world!"

    assert message.from_user is not None
    assert message.from_user.id == test_config.bot_user_id

    assert message.date

    assert message.entities
    assert message.entities[0].type == "bot_command"
    assert message.entities[0].offset == 0
    assert message.entities[0].length == 5

    assert message.entities[1].type == "bold"
    assert message.entities[1].offset == 6
    assert message.entities[1].length == 5


@pytest.mark.asyncio
async def test_send_text_message_with_reply_markup(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    message = await client(
        SendMessage(
            test_config.private_chat_id_1,
            "Hello, world!",
            reply_markup=InlineKeyboardMarkup(
                InlineKeyboardButton("Test", callback_data="test")
            ),
        )
    )

    assert message.message_id
    assert message.chat.id == test_config.private_chat_id_1
    assert message.text == "Hello, world!"

    assert message.from_user is not None
    assert message.from_user.id == test_config.bot_user_id

    assert message.date

    assert message.reply_markup
    assert message.reply_markup.inline_keyboard[0][0].text == "Test"
    assert message.reply_markup.inline_keyboard[0][0].callback_data == "test"
