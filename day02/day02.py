def run(instructions, input1, input2):
    ins = instructions[::]
    ins[1] = input1
    ins[2] = input2
    pos = 0
    while True:
        opcode = ins[pos]
        if opcode == 99:
            break

        fst, snd, tgt = ins[pos + 1 : pos + 4]
        ins[tgt] = ins[fst] + ins[snd] if opcode == 1 else ins[fst] * ins[snd]
        pos += 4

    return ins[0]


def solve1(instructions):
    return run(instructions, 12, 2)


def solve2(instructions):
    for noun in range(100):
        for verb in range(100):
            res = run(instructions, noun, verb)
            if res == 19690720:
                return 100 * noun + verb


def main():
    instructions = list(map(int, input().split(",")))
    print(solve1(instructions))
    print(solve2(instructions))


if __name__ == "__main__":
    main()
