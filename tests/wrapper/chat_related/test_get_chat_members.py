import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import (
    GetChatAdministrators,
    GetChatMember,
    GetChatMemberCount,
)

from src.telegrambots.wrapper.types.objects import (
    ChatMemberOwner,
    ChatMemberAdministrator,
    ChatMemberMember,
)

from ...test_config import TestConfigs, test_config  # type: ignore


@pytest.mark.asyncio
async def test_get_chat_administrators(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1

    result = await client(GetChatAdministrators(chat_id))

    # the chat is expected to be a super group with a single admin and owner

    assert any([x for x in result if isinstance(x, ChatMemberOwner)])
    assert any([x for x in result if isinstance(x, ChatMemberAdministrator)])


@pytest.mark.asyncio
async def test_get_chat_member_1(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1
    user_id = test_config.private_chat_id_1  # the user should be admin

    result = await client(GetChatMember(chat_id, user_id))

    assert isinstance(result, ChatMemberAdministrator)


@pytest.mark.asyncio
async def test_get_chat_member_2(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1
    user_id = test_config.private_chat_id_2  # the user should be member

    result = await client(GetChatMember(chat_id, user_id))

    assert isinstance(result, ChatMemberMember)


@pytest.mark.asyncio
async def test_get_chat_member_count(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1

    result = await client(GetChatMemberCount(chat_id))

    assert isinstance(result, int)
    assert result > 0
