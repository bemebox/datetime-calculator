from datetime import datetime


def is_valid_datetime_format(datetime_string, datetime_format):
    """
    validates if a given datetime string matches the specified format.

    :Params
        datetime_string: a string representing a date and time.
        datetime_format: a string representing the expected format of the datetime_string.
    :Return:
        True if the datetime_string is in the correct format, False otherwise.
    """
    try:
        # try to parse the datetime string
        datetime.strptime(datetime_string, datetime_format)
        return True
    except ValueError:
        # raised when the format of the input string doesn't match the specified format
        return False


def is_datetime_greater(start_datetime_str, end_datetime_str, datetime_format):
    """
    checks if the datetime represented by start_datetime_str is greater than end_datetime_str.

    :Params
        start_datetime_str: string representation of the starting datetime.
        end_datetime_str: string representation of the ending datetime.
        datetime_format: format of the datetime strings.
    :Return:
        True if start_datetime is greater than end_datetime, False otherwise.
    """
    try:
        # Convert datetime strings to datetime objects
        start_datetime = datetime.strptime(start_datetime_str, datetime_format)
        end_datetime = datetime.strptime(end_datetime_str, datetime_format)

        # Compare datetime objects
        return start_datetime > end_datetime
    except ValueError as e:
        # Handle invalid datetime
        return False
