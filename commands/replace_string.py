from io_utils import writeFlush, flushError
from path import expandPath

# replace-stringコマンド
# ex: python3 file_manipulator.py replace-string example/replace_string/input_file.txt string integer
def replace_string(command_args):
    if(len(command_args) < 5):
        flushError("引数が足りません")

    input_path = command_args[2]
    needle = command_args[3]
    new_string = command_args[4]

    input_contents = ""
    with open(expandPath(input_path)) as f:
        input_contents = f.read()

    if(not ( needle in input_contents)):
        flushError(f"{needle}がファイルに含まれていませんでした")

    new_contents = input_contents.replace(needle, new_string)
    with open(expandPath(input_path), "w") as f:
        f.write(new_contents)

    writeFlush(f"{needle}を{new_string}に置き換えました")
