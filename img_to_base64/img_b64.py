import sys
import base64


def start(file_name, ext: str):
    file = file_name.read() # open(file_name, "rb").read()
    data64: str = f"data:image/{ext};base64, " + base64.b64encode(file).decode('ascii')
    return data64
    return ""
