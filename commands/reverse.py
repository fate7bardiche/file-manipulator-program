from io_utils import writeFlush, flushError
from path import expandPath


# reverseコマンド
# ex: python3 file_manipulator.py reverse example/reverse/input_file.txt example/reverse/output_file.txt
def reverse(command_args):
    if(len(command_args) < 4):
        flushError("引数が足りません")

    input_path = command_args[2]
    output_path = command_args[3]

    input_file_contents = ""
    with open(expandPath(input_path)) as f:
        input_file_contents = f.read()

    reversed_cpntents = reverseHelper(input_file_contents, "", len(input_file_contents) - 1)
    with open(expandPath(output_path), 'w') as f:
        f.write(reversed_cpntents)

    writeFlush(f"{output_path}を作成しました")
    
def reverseHelper(s, res, count):
    if(len(s) == len(res)): return res
    return reverseHelper(s, res + s[count], count - 1)