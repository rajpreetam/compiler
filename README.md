# API for compiling code online
## Created using Python and FastAPI

### Deployed: `http://13.126.114.213`
### Documentation: `http://13.126.114.213/docs`

This online compiler uses `subprocess` module under the hood which uses the actual compilers and interpreter installed on the ubuntu server deployed on the `AWS EC2`. Contribute to this project by forking the repo.

1. Supported Languages
    - C++: `language_id: 1`
    - Python: `language_id: 2`

2. Requests:
   - `POST: /api/v1/compiler/submission`
   - Request Body:
      ```
      {
          "language_id": integer,
          "source_code": string,
          "stdin": string | None
      } 
      ```
   - Response Body:
       ```
       {
           "success": true,
           "status_code": integer,
           "message": string,
           "data": {
               "status": string,
               "err_code": integer,
               "stdout": string,
               "stderr": string
           }
       }
       ```