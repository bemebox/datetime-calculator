from main import is_valid_output_type


def test_valid_output_type():
    assert is_valid_output_type("n") is True
    assert is_valid_output_type("t") is True


def test_invalid_output_type():
    assert is_valid_output_type("x") is False
    assert is_valid_output_type("") is False
    assert is_valid_output_type(None) is False
