from pathlib import Path
import pytest
from src.telegrambots.wrapper.client import TelegramBotsClient
from src.telegrambots.wrapper.types.methods import SendPhoto, SendMediaGroup
from src.telegrambots.wrapper.types.objects import InputFile, InputMediaPhoto

from ...test_config import TestConfigs, test_config  # type: ignore


@pytest.mark.asyncio
async def test_send_photo_local_file_1(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    file_path = Path(__file__).parent.resolve().joinpath("test_photo_1.jpg")

    with SendPhoto(
        test_config.private_chat_id_1,
        InputFile(open(file_path, "rb"), "test_photo_1.jpg"),
    ) as send_photo:
        send_photo.caption = "Hello, world!"

        result = await client(send_photo)

    assert result.message_id
    assert result.caption == "Hello, world!"
    assert result.photo
    assert result.photo[0].file_id


@pytest.mark.asyncio
async def test_send_photo_local_file_2(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    file_path = Path(__file__).parent.resolve().joinpath("test_photo_2.jpg")

    with InputFile(file_path) as file:
        send_photo = SendPhoto(test_config.private_chat_id_1, file)
        send_photo.caption = "Hello, world!"

        result = await client(send_photo)

    assert result.message_id
    assert result.caption == "Hello, world!"
    assert result.photo
    assert result.photo[0].file_id


@pytest.mark.asyncio
async def test_send_photo_online_file(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    send_photo = SendPhoto(
        test_config.private_chat_id_1, "https://imgur.com/t/funny/MpMGFRQ"
    )
    send_photo.caption = "Hello, world!"

    result = await client(send_photo)

    assert result.message_id
    assert result.caption == "Hello, world!"
    assert result.photo
    assert result.photo[0].file_id


@pytest.mark.asyncio
async def test_send_media_group(test_config: TestConfigs):
    client = TelegramBotsClient(test_config.bot_token)

    file_path_1 = Path(__file__).parent.resolve().joinpath("test_photo_1.jpg")
    file_path_2 = Path(__file__).parent.resolve().joinpath("test_photo_2.jpg")

    with InputFile(file_path_1) as file:
        with SendMediaGroup(
            test_config.private_chat_id_1,
            [
                InputMediaPhoto(file, "My first photo"),
                InputMediaPhoto(InputFile(open(file_path_2, "rb"), "test_photo_2.jpg")),
                InputMediaPhoto("https://imgur.com/t/funny/MpMGFRQ"),
            ],
        ) as send_media_group:
            result = await client(send_media_group)

    assert result
    assert len(result) == 3
    assert result[0].message_id
    assert result[0].caption == "My first photo"
    assert result[0].photo
    assert result[0].photo[0].file_id
    assert result[1].message_id
    assert result[1].photo
    assert result[1].photo[0].file_id
    assert result[2].message_id
    assert result[2].photo
    assert result[2].photo[0].file_id
