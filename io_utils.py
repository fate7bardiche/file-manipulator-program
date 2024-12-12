import sys

def writeFlush(message, has_new_line = True): 
    write(message, has_new_line)
    flush()

def write(message, has_new_line = True):
    new_line = "\n" if has_new_line else ""
    sys.stdout.buffer.write(f'{message}{new_line}'.encode())

def flush():
    sys.stdout.buffer.flush()

def flushError(message, has_new_line = True):
    new_line = "\n" if has_new_line else ""
    sys.stdout.buffer.write(f'{message}{new_line}'.encode())
    sys.stdout.buffer.flush()
    sys.exit()