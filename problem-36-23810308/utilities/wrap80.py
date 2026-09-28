from pathlib import Path
import sys

LIMIT = 79

def wrap_file(input_path: Path, output_path: Path) -> None:
    with input_path.open("r", newline="") as input_file, output_path.open(
        "w", newline=""
    ) as output_file:
        for line in input_file:
            has_newline = line.endswith(("\n", "\r"))
            content = line.rstrip("\r\n")
            while len(content) > LIMIT:
                output_file.write(content[:LIMIT] + "\n")
                content = content[LIMIT:]
            output_file.write(content)
            if has_newline:
                output_file.write("\n")

if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} <input-file> <output-file>")
    sys.exit(1)

wrap_file(Path(sys.argv[1]), Path(sys.argv[2]))