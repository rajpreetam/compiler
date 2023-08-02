import ast
import re
from ..utils.custom_response import custom_response
from fastapi import status


def sanitize_python_code(source_code: str):
    word_set = set()
    word_arr = source_code.replace('\n', ' ').replace('.', ' ').split(' ')
    for word in word_arr:
        word_set.add(word)

    if 'os' in word_set:
        result = custom_response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            data=None,
            message='Opps, you cannot work with os module'
        )
        is_vulnerable = True
        return is_vulnerable, result

    if 'subprocess' in word_set:
        result = custom_response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            data=None,
            message='Opps, you cannot work with subprocess module'
        )
        is_vulnerable = True
        return is_vulnerable, result

    is_vulnerable = False
    return is_vulnerable, None
