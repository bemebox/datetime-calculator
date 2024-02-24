from datetime_utils import is_valid_datetime_format, is_datetime_greater


def test_valid_datetime_format():
    assert is_valid_datetime_format("2024-02-24 12:30:45", "%Y-%m-%d %H:%M:%S") is True
    assert is_valid_datetime_format("2021-12-01", "%Y-%m-%d") is True


def test_invalid_datetime_format():
    assert is_valid_datetime_format("24-02-2024", "%Y-%m-%d") is False
    assert is_valid_datetime_format("2024-02-24 12:30:45", "%d-%m-%Y %H:%M:%S") is False


def test_is_valid_datetime_format_empty_datetime_string():
    assert is_valid_datetime_format("", "%Y-%m-%d %H:%M:%S") is False


def test_is_valid_datetime_format_invalid_format():
    assert is_valid_datetime_format("2024-02-24 12:30:45", "invalid_format") is False


def test_is_valid_datetime_format_datetime_greater():
    assert (
        is_datetime_greater(
            "2024-02-24 12:30:45", "2024-02-24 10:15:30", "%Y-%m-%d %H:%M:%S"
        )
        is True
    )
    assert is_datetime_greater("2021-12-01", "2021-11-30", "%Y-%m-%d") is True


def test_is_valid_datetime_format_datetime_not_greater():
    assert (
        is_datetime_greater(
            "2024-02-24 12:30:45", "2024-02-24 14:45:30", "%Y-%m-%d %H:%M:%S"
        )
        is False
    )
    assert is_datetime_greater("2021-11-30", "2021-12-01", "%Y-%m-%d") is False


def test_is_valid_datetime_format_invalid_datetime_format():
    assert (
        is_datetime_greater(
            "2024-02-24 12:30:45", "invalid_datetime", "%Y-%m-%d %H:%M:%S"
        )
        is False
    )
