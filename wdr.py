#!/usr/bin/env python3

import argparse
from dataclasses import dataclass
from enum import StrEnum, auto


class Opcode(StrEnum):
    INC = auto()
    DEC = auto()
    JMP = auto()
    ISZ = auto()
    STP = auto()


class Register(StrEnum):
    R0 = auto()
    R1 = auto()
    R2 = auto()
    R3 = auto()


type Operand = Register.value | int | None


@dataclass
class Instruction:
    opcode: Opcode
    operand: Operand


def parse(filename: str) -> list[Instruction]:
    instructions: list[Instruction] = []
    with open(filename) as f:
        for lineno, line in enumerate(iterable=f, start=1):
            if line.isspace():
                continue

            parts = line.strip().split()
            if len(parts) > 2:
                raise ValueError(f"Line {lineno}: Invalid instruction: {line}")

            try:
                opcode = Opcode[parts[0].upper()]
            except KeyError:
                raise ValueError(f"Line {lineno}: Invalid opcode: {parts[0]}")

            operand: Operand = None
            match opcode:
                case Opcode.INC | Opcode.DEC | Opcode.ISZ:
                    try:
                        operand = Register[parts[1].upper()]
                    except KeyError:
                        raise ValueError(
                            f"Line {lineno}: Invalid register '{parts[1]}'"
                        )
                case Opcode.JMP:
                    try:
                        operand = int(parts[1])
                    except ValueError:
                        raise ValueError(f"Line {lineno}: Invalid operand '{parts[1]}'")
                case Opcode.STP:
                    if len(parts) != 1:
                        raise ValueError(f"Line {lineno}: stp requires no operand")

            instructions.append(Instruction(opcode, operand))

    return instructions


class Interpreter:
    def __init__(
        self,
        initial_state: dict[Register, int] | None,
        instructions: list[Instruction],
    ) -> None:
        self.registers = {reg: 0 for reg in Register}
        self.program_counter = 0

        if initial_state is not None:
            for reg, val in initial_state.items():
                self.registers[reg] = val

        self.instructions = instructions

    def eval(self) -> None:
        print("=== Initial state ===")
        print(f"R0: {self.registers[Register.R0]}")
        print(f"R1: {self.registers[Register.R1]}")
        print(f"R2: {self.registers[Register.R2]}")
        print(f"R3: {self.registers[Register.R3]}")

        while self.program_counter < len(self.instructions):
            current_instruction = self.instructions[self.program_counter]
            opcode = current_instruction.opcode
            operand = current_instruction.operand
            match opcode:
                case Opcode.INC:
                    self.registers[operand] += 1
                    self.program_counter += 1
                case Opcode.DEC:
                    if self.registers[operand] == 0:
                        raise ValueError(
                            f"Line {self.program_counter + 1}: Error: decrementing zero register"
                        )
                    self.registers[operand] -= 1
                    self.program_counter += 1
                case Opcode.JMP:
                    if operand < 1 or operand > len(self.instructions):
                        raise ValueError(
                            f"Line {self.program_counter + 1}: Invalid jump to line {operand}"
                        )
                    self.program_counter = operand - 1
                case Opcode.ISZ:
                    if self.registers[operand] == 0:
                        if self.program_counter + 2 < len(self.instructions):
                            self.program_counter += 2
                        else:
                            raise ValueError(
                                f"Line {self.program_counter + 1}: Invalid jump to line {self.program_counter + 2}"
                            )
                    else:
                        self.program_counter += 1
                case Opcode.STP:
                    break
                case _:
                    raise ValueError(f"Illegal opcode: {opcode}")

        print("=== Final state ===")
        print(f"R0: {self.registers[Register.R0]}")
        print(f"R1: {self.registers[Register.R1]}")
        print(f"R2: {self.registers[Register.R2]}")
        print(f"R3: {self.registers[Register.R3]}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="WDR Paper Computer Interpreter",
        epilog="Example: ./wdr.py program.asm 1 2 3 4",
    )
    parser.add_argument("filename", help="Path to the program file")
    parser.add_argument(
        "registers",
        nargs="*",
        type=int,
        help="Initial values for registers R0, R1, R2, R3",
    )
    args = parser.parse_args()

    instructions = parse(args.filename)

    initial_state: dict[Register, int] | None = None
    if args.registers:
        initial_state = {
            Register[f"R{i}"]: value for i, value in enumerate(args.registers)
        }

    interpreter = Interpreter(initial_state, instructions)
    interpreter.eval()


if __name__ == "__main__":
    main()
