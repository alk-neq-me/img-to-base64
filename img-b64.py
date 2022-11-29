import sys
import base64


def start():
    if len(sys.argv) > 1:
        try:
            is_output: bool = sys.argv[2]
        except IndexError as e:
            is_output: bool = False
        file_name: str = sys.argv[1]
        if (file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png") or file_name.endswith(".gif") or file_name.endswith(".webp")):
            file = open(file_name, "rb").read()
            data64: str = f"data:image/{file_name.split('.')[1]};base64, " + base64.b64encode(file).decode('ascii')
            if (is_output):
                with open(file_name.split(".")[0]+".txt", mode="w", encoding="utf-8") as f:
                    f.write(data64)
                    f.close()
            else:
                print(data64)


if __name__ == "__main__":
    start()
