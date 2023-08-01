from fastapi import status
from ..schemas import SubmissionRequest
from ..code_compilers.cpp_compiler import cpp_compiler
from ..utils.custom_response import custom_response


def submission_service(data: SubmissionRequest):
    try:
        source_code = data.source_code
        language_id = data.language_id
        stdin = data.stdin

        if language_id == 1:
            stdout, stderr = cpp_compiler(source_code, stdin)
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
        else:
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='Invalid language id'
            )

    except Exception as e:
        print(e)
        return custom_response(
            success=False,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data=None,
            message='Something went wrong'
        )
