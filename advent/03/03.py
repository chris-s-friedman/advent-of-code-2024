import re

with open("input", "r", encoding="utf8") as f:
    program = f.read()


def run_program(program):
    # Regular expression to match "mul(number,number)"
    pattern = r"mul\(\d+,\d+\)"
    matches = [re.findall(r"\d+", i) for i in re.findall(pattern, program)]

    multiples = [int(i[0]) * int(i[1]) for i in matches]

    return sum(multiples)


program_sum = run_program(program)

print(f"Sum of all multiples: {program_sum}")

# Part 2

enabled_program = "do()" + program.replace("\n", "") + "don't()"

enabled_program_parts = re.findall(r"do\(\)(.*?)don\'t\(\)", enabled_program)

parts = [run_program(part) for part in enabled_program_parts]

enabled_program_sum = sum(parts)

print(f"Sum of all multiples in enabled program: {enabled_program_sum}")
