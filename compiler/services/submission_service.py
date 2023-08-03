from fastapi import status
from ..schemas import SubmissionRequest
from ..code_compilers.cpp_compiler import cpp_compiler
from ..code_compilers.python_compiler import python_compiler
from core.utils.custom_response import custom_response
from core.utils.custom_exceptions import CustomInternalServerException
from ..utils.sanitize_code import (
    sanitize_python_code,
    sanitize_cpp_code
)


def compiler_logic(stdout, stderr):
    if stdout is None:
        _data = {
            'stdout': stdout,
            'stderr': stderr,
            'status': 'Compilation Error',
            'err_code': 1
        }
        return custom_response(
            success=True,
            status_code=status.HTTP_200_OK,
            data=_data,
            message='Successful http request'
        )
    return custom_response(
        success=True,
        status_code=status.HTTP_200_OK,
        data={
            'stdout': stdout,
            'stderr': stderr,
            'status': 'Accepted',
            'err_code': None
        },
        message='Successful http request'
    )


def submission_service(data: SubmissionRequest):
    try:
        source_code = data.source_code
        language_id = data.language_id
        stdin = data.stdin

        if language_id == 1:
            is_vulnerable, result = sanitize_cpp_code(source_code)
            if is_vulnerable:
                return result

            stdout, stderr = cpp_compiler(source_code, stdin)
            return compiler_logic(stdout, stderr)

        elif language_id == 2:
            is_vulnerable, result = sanitize_python_code(source_code)
            if is_vulnerable:
                return result

            stdout, stderr = python_compiler(source_code, stdin)
            return compiler_logic(stdout, stderr)
        else:
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='Invalid language id'
            )

    except Exception as e:
        print('Error 62:', e)
        raise CustomInternalServerException
