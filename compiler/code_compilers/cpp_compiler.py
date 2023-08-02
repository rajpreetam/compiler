import os
import subprocess


def cpp_compiler(source_code: str, stdin: str):
    try:
        cpp_file = open('main.cpp', 'w')
        cpp_file.write(source_code)
        cpp_file.close()
        result = subprocess.run(
            ['g++', 'main.cpp', '-o', 'main'],
            capture_output=True,
            text=True,
            timeout=4
        )
        if result.returncode == 0:
            run_result = subprocess.run(
                ['./' + 'main'],
                input=stdin,
                capture_output=True,
                text=True
            )
            os.remove('main')
            os.remove('main.cpp')
            return run_result.stdout, run_result.stderr
        else:
            os.remove('main.cpp')
            return None, result.stderr
    except subprocess.CalledProcessError as e:
        print(e)
        return None, e
