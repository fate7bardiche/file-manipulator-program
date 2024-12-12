from io_utils import writeFlush, flushError
from path import expandPath


# copyコマンド
# ex: python3 file_manipulator.py copy example/copy/input_file.txt example/copy/output_file.txt
def copy(command_args):
    if(len(command_args) < 4):
        flushError("引数が足りません")

    input_path = command_args[2]
    output_path = command_args[3]

    input_file_contents = ""
    with open(expandPath(input_path)) as f:
        input_file_contents = f.read()
    
    with open(expandPath(output_path), "w") as f:
        f.write(input_file_contents)

    writeFlush(f"{output_path}を作成しました")