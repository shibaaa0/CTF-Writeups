import sys

class Op:
    IncPointer = "skibidi"
    DecPointer = "rizz"
    IncData = "sigma"
    DecData = "gyatt"
    OutData = "ohio"         # ✅ Đổi từ 'yap' thành 'ohio'
    InpData = "blud"
    CondJumpForward = "grimaceshake"
    CondJumpBackward = "fanumtax"

def tokenize(code):
    keywords = {
        "skibidi": Op.IncPointer,
        "rizz": Op.DecPointer,
        "sigma": Op.IncData,
        "gyatt": Op.DecData,
        "ohio": Op.OutData,      # ✅ Đổi từ 'yap' thành 'ohio'
        "blud": Op.InpData,
        "grimaceshake": Op.CondJumpForward,
        "fanumtax": Op.CondJumpBackward,
    }
    tokens = []
    words = code.split()
    for word in words:
        if word in keywords:
            tokens.append(keywords[word])
    return tokens

def print_byte(byte):
    sys.stdout.write(chr(byte))
    sys.stdout.flush()

def read_byte():
    return ord(sys.stdin.read(1))

def execute(code):
    operations = tokenize(code)
    data = [0] * 30000
    pointer = 0
    i = 0
    len_ops = len(operations)

    # Preprocess jumps
    pairs = {}
    stack = []

    for idx, op in enumerate(operations):
        if op == Op.CondJumpForward:
            stack.append(idx)
        elif op == Op.CondJumpBackward:
            if not stack:
                raise Exception(f"Unmatched 'fanumtax' at position {idx}")
            start = stack.pop()
            pairs[start] = idx
            pairs[idx] = start

    if stack:
        raise Exception(f"Unmatched 'grimaceshake' at positions {stack}")

    # Interpreter
    while i < len_ops:
        op = operations[i]
        if op == Op.IncPointer:
            pointer += 1
        elif op == Op.DecPointer:
            pointer -= 1
        elif op == Op.IncData:
            data[pointer] = (data[pointer] + 1) % 256
        elif op == Op.DecData:
            data[pointer] = (data[pointer] - 1) % 256
        elif op == Op.OutData:
            print_byte(data[pointer])
        elif op == Op.InpData:
            data[pointer] = read_byte()
        elif op == Op.CondJumpForward:
            if data[pointer] == 0:
                i = pairs[i]
        elif op == Op.CondJumpBackward:
            if data[pointer] != 0:
                i = pairs[i]
        i += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 skibidi.py <sourcefile>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        source = f.read()

    execute(source)
