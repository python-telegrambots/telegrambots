import pytest
import src.telegrambots.wrapper.serializations as serializations


def test_custom_deserialize_1():

    result = serializations.deserialize(str, "test")

    assert isinstance(result, str)
    assert result == "test"


def test_custom_deserialize_2():

    result = serializations.deserialize(str, ["test", "test2"])

    assert isinstance(result, list)
    assert result[0] == "test"
