import sys
from types import ModuleType
from typing import Union


def error_message_detail(error: Union[str, Exception], error_detail: ModuleType = sys) -> str:
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    return (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"with message: [{error}]"
    )


class CustomException(Exception):
    def __init__(self, error_message: Union[str, Exception], error_detail: ModuleType = sys):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
