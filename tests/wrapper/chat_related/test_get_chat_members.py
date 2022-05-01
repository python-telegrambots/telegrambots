import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import (
    GetChatAdministrators,
    GetChatMember,
    GetChatMemberCount,
    PinChatMessage,
    GetChat,
    SetChatTitle,
    SetChatDescription,
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


async def test_get_chat_member_1(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1
    user_id = test_config.private_chat_id_1  # the user should be admin

    result = await client(GetChatMember(chat_id, user_id))

    assert isinstance(result, ChatMemberAdministrator)


async def test_get_chat_member_2(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1
    user_id = test_config.private_chat_id_2  # the user should be member

    result = await client(GetChatMember(chat_id, user_id))

    assert isinstance(result, ChatMemberMember)


async def test_get_chat_member_count(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    chat_id = test_config.super_group_chat_id_1

    result = await client(GetChatMemberCount(chat_id))

    assert isinstance(result, int)
    assert result > 0


async def test_pin_chat_message(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)  # bot should have pin rights

    chat_id = test_config.super_group_chat_id_1
    message_id = test_config.super_group_1_existing_message_id

    result = await client(PinChatMessage(chat_id, message_id))

    assert isinstance(result, bool)
    assert result is True

    chat = await client(GetChat(chat_id))

    assert chat.pinned_message
    assert chat.pinned_message.message_id == message_id


async def test_set_chat_title(test_config: TestConfigs):
    client = TelegramBotsClient(
        test_config.bot_token
    )  # bot should have change group info rights

    chat_id = test_config.super_group_chat_id_1
    new_title = "new title"

    result = await client(SetChatTitle(chat_id, new_title))

    assert isinstance(result, bool)
    assert result is True

    chat = await client(GetChat(chat_id))

    assert chat.title == new_title


async def test_set_chat_description(test_config: TestConfigs):
    client = TelegramBotsClient(
        test_config.bot_token
    )  # bot should have change group info rights

    chat_id = test_config.super_group_chat_id_1
    new_description = "new description"

    result = await client(SetChatDescription(chat_id, new_description))

    assert isinstance(result, bool)
    assert result is True

    chat = await client(GetChat(chat_id))

    assert chat.description == new_description
