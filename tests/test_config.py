from typing import cast
import pytest
import os
import dataclasses
from dotenv import load_dotenv  # type: ignore


@dataclasses.dataclass(init=True, frozen=True)
class TestConfigs:
    bot_token: str
    bot_user_id: int
    private_chat_id_1: int
    private_chat_id_2: int
    super_group_chat_id_1: int


@pytest.fixture(scope="package")
def test_config():
    load_dotenv()

    return TestConfigs(
        bot_token=str(os.getenv("bot_token")),
        bot_user_id=int(cast(str, os.getenv("bot_user_id"))),
        private_chat_id_1=int(cast(str, os.getenv("private_chat_id_1"))),
        private_chat_id_2=int(cast(str, os.getenv("private_chat_id_2"))),
        super_group_chat_id_1=int(cast(str, os.getenv("super_group_chat_id_1"))),
    )
