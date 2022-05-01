import json
from typing import Any
import pytest
from src.telegrambots.wrapper.types.objects import Update, Message


@pytest.fixture
def custom_types():
    return {
        "pinned_message": [Message],  # in Chat object
        "reply_to_message": [Message],
    }


def test_serialize_callback_query(custom_types: dict[str, list[type[Any]]]):
    json_object = """
    {
        "update_id":10000,
        "callback_query": {
            "id": "4382bfdwdsb323b2d9",
            "from": {
                "last_name":"Test Lastname",
                "type": "private",
                "id":1111111,
                "first_name":"Test Firstname",
                "username":"Testusername",
                "is_bot":false
            },
            "chat_instance":"4382bfdwdsb323b2d9",
            "data": "Data from button callback",
            "inline_message_id": "1234csdbsk4839"
        }
    }
    """

    update = Update.deserialize(json.loads(json_object), custom_types)

    assert update.update_id == 10000
    assert update.callback_query
    assert update.callback_query.id == "4382bfdwdsb323b2d9"
    assert update.callback_query.from_user.id == 1111111
    assert update.callback_query.from_user.first_name == "Test Firstname"
    assert update.callback_query.from_user.last_name == "Test Lastname"
    assert update.callback_query.from_user.username == "Testusername"
    assert update.callback_query.data == "Data from button callback"
    assert update.callback_query.inline_message_id == "1234csdbsk4839"


def test_serialize_message(custom_types: dict[str, list[type[Any]]]):
    json_object = """
    {
        "update_id": 10000,
        "message": {
            "date": 1441645532,
            "chat": {
                "type": "private",
                "last_name": "Test Lastname",
                "id": 1111111,
                "first_name": "Test",
                "username": "Test"
            },
            "message_id": 1365,
            "from": {
                "last_name": "Test Lastname",
                "id": 1111111,
                "first_name": "Test",
                "username": "Test",
                "is_bot": false
            },
            "text": "/start"
        }
    }
    """

    update = Update.deserialize(json.loads(json_object), custom_types)

    assert update.update_id == 10000
    assert update.message
    assert update.message.text == "/start"
    assert update.message.from_user
    assert update.message.from_user.id == 1111111
    assert update.message.from_user.first_name == "Test"
    assert update.message.from_user.last_name == "Test Lastname"
    assert update.message.from_user.username == "Test"
    assert update.message.chat.id == 1111111
    assert update.message.chat.first_name == "Test"
    assert update.message.chat.last_name == "Test Lastname"
    assert update.message.chat.username == "Test"
    assert update.message.date == 1441645532
    assert update.message.message_id == 1365


def test_serialize_forwarded_message(custom_types: dict[str, list[type[Any]]]):
    json_object = """
    {
        "update_id": 10000,
        "message": {
            "date": 1441645532,
            "chat": {
                "type": "private",
                "last_name": "Test Lastname",
                "id": 1111111,
                "type": "private",
                "first_name": "Test Firstname",
                "username": "Testusername"
            },
            "message_id": 1365,
            "from": {
                "last_name": "Test Lastname",
                "id": 1111111,
                "first_name": "Test Firstname",
                "username": "Testusername",
                "is_bot": false
            },
            "forward_from": {
                "last_name": "Forward Lastname",
                "id": 222222,
                "first_name": "Forward Firstname",
                "is_bot": false
            },
            "forward_date": 1441645550,
            "text": "/start"
        }
    }
    """

    update = Update.deserialize(json.loads(json_object), custom_types)

    assert update.update_id == 10000
    assert update.message
    assert update.message.text == "/start"
    assert update.message.from_user
    assert update.message.from_user.id == 1111111
    assert update.message.from_user.first_name == "Test Firstname"
    assert update.message.from_user.last_name == "Test Lastname"
    assert update.message.from_user.username == "Testusername"
    assert update.message.chat.id == 1111111
    assert update.message.chat.first_name == "Test Firstname"
    assert update.message.chat.last_name == "Test Lastname"
    assert update.message.chat.username == "Testusername"
    assert update.message.date == 1441645532
    assert update.message.message_id == 1365
    assert update.message.forward_from
    assert update.message.forward_from.id == 222222
    assert update.message.forward_from.first_name == "Forward Firstname"
    assert update.message.forward_from.last_name == "Forward Lastname"
    assert update.message.forward_date == 1441645550


def test_serialize_inline_query(custom_types: dict[str, list[type[Any]]]):
    json_object = """
    {
        "update_id": 10000,
        "inline_query": {
            "id": 134567890097,
            "from": {
                "last_name": "Test Lastname",
                "type": "private",
                "id": 1111111,
                "first_name": "Test Firstname",
                "username": "Testusername",
                "is_bot": false
            },
            "query": "inline query",
            "offset": ""
        }
    }
    """

    update = Update.deserialize(json.loads(json_object), custom_types)

    assert update.update_id == 10000
    assert update.inline_query
    assert update.inline_query.id == 134567890097
    assert update.inline_query.from_user
    assert update.inline_query.from_user.id == 1111111
    assert update.inline_query.from_user.first_name == "Test Firstname"
    assert update.inline_query.from_user.last_name == "Test Lastname"
    assert update.inline_query.from_user.username == "Testusername"
    assert update.inline_query.query == "inline query"
    assert update.inline_query.offset == ""


def test_serialize_chosen_inline_query(custom_types: dict[str, list[type[Any]]]):
    json_object = """
    {
        "update_id": 10000,
        "chosen_inline_result": {
            "result_id": "12",
            "from": {
                "last_name": "Test Lastname",
                "type": "private",
                "id": 1111111,
                "first_name": "Test Firstname",
                "username": "Testusername",
                "is_bot": false
            },
            "query": "inline query",
            "inline_message_id": "1234csdbsk4839"
        }
    }
    """

    update = Update.deserialize(json.loads(json_object), custom_types)

    assert update.update_id == 10000
    assert update.chosen_inline_result
    assert update.chosen_inline_result.result_id == "12"
    assert update.chosen_inline_result.from_user
    assert update.chosen_inline_result.from_user.id == 1111111
    assert update.chosen_inline_result.from_user.first_name == "Test Firstname"
    assert update.chosen_inline_result.from_user.last_name == "Test Lastname"
    assert update.chosen_inline_result.from_user.username == "Testusername"
    assert update.chosen_inline_result.query == "inline query"
    assert update.chosen_inline_result.inline_message_id == "1234csdbsk4839"
