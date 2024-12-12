import sys
from io_utils import flushError
from commands.reverse import reverse
from commands.copy import copy
from commands.duplicate_contents import duplicate_contents
from commands.replace_string import replace_string

def main():
    if(len(sys.argv) == 1): flushError("コマンドを入力してください\n")

    command =  sys.argv[1]
    if(command == "reverse"):
        reverse(sys.argv)
    elif(command == "copy"):
        copy(sys.argv)
    elif(command == "duplicate-contents"):
        duplicate_contents(sys.argv)
    elif(command == "replace-string"):
        replace_string(sys.argv)
    else:
        flushError(f"{command}: コマンドが見つかりません")

main()