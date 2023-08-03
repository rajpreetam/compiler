from core.utils.custom_response import custom_response
from fastapi import status
import re


def sanitize_python_code(source_code: str):
    word_set = set()
    word_arr = source_code.replace('\n', ' ').replace('.', ' ').split(' ')
    for word in word_arr:
        word_set.add(word)

    if 'os' in word_set or 'subprocess' in word_set:
        result = custom_response(
            success=False,
            status_code=status.HTTP_400_BAD_REQUEST,
            data=None,
            message='Opps, you cannot work with \'os\' or \'subprocess\' modules'
        )
        is_vulnerable = True
        return is_vulnerable, result

    is_vulnerable = False
    return is_vulnerable, None


def sanitize_cpp_code(source_code: str):
    vulnerable_commands = [
        r'\bsystem\s*\(',
        r'\bpopen\s*\(',
        r'\bfopen\s*\(\s*".*"\s*,\s*"w"\s*\)|\bfopen\s*\(\s*".*"\s*,\s*"a"\s*\)',
        r'\bremove\s*\(',
        r'\bstrcpy\s*\(',
        r'\bstrcat\s*\(',
        r'\bscanf\s*\(',
        # Add more vulnerable command patterns as needed
    ]

    for command in vulnerable_commands:
        if re.search(command, source_code):
            result = custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='Opps, you cannot work with system vulnerable modules'
            )
            is_vulnerable = True
            return is_vulnerable, result
    return False, None
