"""Yikes - not the prettiest solution"""
import itertools
import sys


def mode_transform(instructions, parameters, modes):
    return [p if m else instructions[p] for p, m in zip(parameters, modes)]


def run(instructions, pos, queue):
    ins = instructions[::]
    while True:
        operation = str(ins[pos]).zfill(5)
        opcode = int(operation[-2:])
        modes = list(map(int, operation[:3]))[::-1]
        if opcode == 99:
            pos += 1
            return None

        if opcode in (1, 2, 7, 8):
            fst, snd = mode_transform(ins, ins[pos + 1 : pos + 3], modes)
            tgt = ins[pos + 3]
            pos += 4
            if opcode in (1, 2):
                ins[tgt] = fst + snd if opcode == 1 else fst * snd
            elif opcode == 7:
                ins[tgt] = 1 if fst < snd else 0
            else:
                ins[tgt] = 1 if fst == snd else 0

        if opcode in (3, 4):
            tgt = ins[pos + 1]
            pos += 2

            if opcode == 3:
                ins[tgt] = queue.pop(0)
            else:
                v = mode_transform(ins, [tgt], modes)[0]
                return ins, pos, v

        if opcode in (5, 6):
            fst, snd = mode_transform(ins, ins[pos + 1 : pos + 3], modes)
            if opcode == 5:
                pos = snd if fst else pos + 3
            else:
                pos = snd if fst == 0 else pos + 3


def part2(instructions):
    options = itertools.permutations(range(5, 10))
    best = 0
    for option in options:
        state = {s: (instructions, 0) for s in option}
        queues = {s: [s] for s in option}
        signal = 0
        for s in itertools.cycle(option):
            queue = queues[s]
            queue.append(signal)
            code, pos = state[s]
            res = run(code, pos, queue)
            if res is None:
                break

            code, pos, signal = res
            state[s] = (code, pos)

        if signal > best:
            best = signal

    return best


def part1(instructions):
    options = itertools.permutations(range(5))
    best = 0
    for option in options:
        queues = {s: [s] for s in option}
        signal = 0
        for s in option:
            queue = queues[s]
            queue.append(signal)
            _code, _pos, signal = run(instructions, 0, queue)

        if signal > best:
            best = signal

    return best


def main():
    instructions = list(map(int, open(sys.argv[1]).read().strip().split(",")))
    print(part1(instructions))
    print(part2(instructions))


if __name__ == "__main__":
    main()
