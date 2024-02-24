from sys import exit
from datetime import datetime
from collections import namedtuple
from datetime_utils import is_valid_datetime_format, is_datetime_greater

# create constant values
Constants = namedtuple("Constants", ["date_time_format"])
constants = Constants("%Y-%m-%d %H:%M:%S")


def main():
    try:
        input_date_time = input("Give a date and time (YYYY-MM-DD HH:MM:SS): ").strip()
        # check the input date time format
        if not input_date_time:
            exit(f"Missing date and time value.")
        elif not is_valid_datetime_format(input_date_time, constants.date_time_format):
            exit(
                f"Invalid date time format {input_date_time}. the correct format is YYYY-MM-DD HH:MM:SS."
            )

        # input_date_time cannot be a datetime after the current date.
        if not is_datetime_greater(
            datetime.now().strftime(constants.date_time_format),
            input_date_time,
            constants.date_time_format,
        ):
            exit(
                f"Invalid date time. {input_date_time} cannot be greater than current date time."
            )

        output_type = input("Type (n) for number or (t) for text output: ").strip()
        # check the output format
        if not is_valid_output_type(output_type):
            exit(f"Invalid output type {output_type}. must be 'n' or 't'.")

        # TODO: print the output
        print()
    except ValueError:
        exit("Something went wrong!")


def is_valid_output_type(output_type):
    """
    checks if the provided output type is valid.

    :Params
        output_type: A string representing the output type.
    :Return:
        True if the output type is valid (either 'n' or 't'), False otherwise.
    """
    valid_output_types = ("n", "t")

    return output_type in valid_output_types


if __name__ == "__main__":
    main()
