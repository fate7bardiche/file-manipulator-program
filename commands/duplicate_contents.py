from io_utils import writeFlush, flushError
from path import expandPath


# duplicate-contentsコマンド
# ex: python3 file_manipulator.py duplicate-contents  example/duplicate_contents/input_file.txt 4
def duplicate_contents(command_args):
    if(len(command_args) < 4):
        flushError("引数が足りません")

    input_path = command_args[2]

    try: int(command_args[3])
    except ValueError:
        flushError("反復回数は数字で入力してください")
    
    count = int(command_args[3])
    if (count < 1):
        flushError("反復回数には1以上の数字を入力してください")

    input_contents = ""
    with open(expandPath(input_path)) as f:
        input_contents = f.read()

    with open(expandPath(input_path), "a") as f:
        for i in range(count):
            f.write(input_contents)
    
    writeFlush(f'{input_path}を{count}回複製しました')