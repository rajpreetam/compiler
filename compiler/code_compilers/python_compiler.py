import subprocess


def python_compiler(source_code: str, stdin: str):
    try:
        result = subprocess.run(
            ['python3', '-c', source_code],
            capture_output=True,
            input=stdin,
            text=True,
            timeout=4
        )
        if result.returncode == 0:
            return result.stdout, result.stderr
        else:
            return None, result.stderr
    except subprocess.CalledProcessError as e:
        print(e)
        return None, e


