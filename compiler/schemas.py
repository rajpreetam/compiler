from pydantic import BaseModel


class ResponseBody(BaseModel):
    success: bool
    status_code: int
    message: str


class SubmissionRequest(BaseModel):
    language_id: int
    source_code: str
    stdin: str | None = ''


class SubmissionResponseData(BaseModel):
    status: str
    err_code: int | None = None
    stdout: str | None = None
    stderr: str | None = None


class SubmissionResponse(ResponseBody):
    data: SubmissionResponseData
