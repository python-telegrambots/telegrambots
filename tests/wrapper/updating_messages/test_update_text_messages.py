import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendMessage, EditMessageText

from src.telegrambots.wrapper.types.objects import Message

from ...test_config import TestConfigs, test_config  # type: ignore


@pytest.mark.asyncio
async def test_edit_text_message_text(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1

    result = await client(SendMessage(chat_id, "new text"))

    assert result.message_id
    assert result.text == "new text"

    updated = await client(
        EditMessageText(
            text="new text 2", chat_id=chat_id, message_id=result.message_id
        )
    )

    assert isinstance(updated, Message)
    assert updated.message_id == result.message_id
    assert updated.text == "new text 2"
