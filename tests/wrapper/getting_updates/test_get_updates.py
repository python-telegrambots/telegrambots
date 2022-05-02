import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import GetUpdates

from src.telegrambots.wrapper.types.objects import Update

from ...test_config import TestConfigs, test_config  # type: ignore


@pytest.mark.asyncio
async def test_get_updates(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    updates = await client(
        GetUpdates(0, limit=100, timeout=0, allowed_updates=["message"])
    )

    assert isinstance(updates, list)

    if any(updates):
        assert isinstance(updates[0], Update)
