from pathlib import Path
import sys

IGNORE_FIRST_LINE = True


def get_char_frequency(lines):
    char_counts = {}
    for line in lines:
        for ch in line:
            if ch != '\n' and not (32 <= ord(ch) <= 126) and ch not in char_counts:
                print(f'non-ASCII character {ch!r}')
            char_counts[ch] = char_counts.get(ch, 0) + 1
    chars_by_freq = sorted(char_counts.items(), key=lambda x:x[1], reverse=True)
    return chars_by_freq


if __name__ == "__main__":
    choice = ''
    show_plot = len(sys.argv) > 2
    try:
        choice = sys.argv[1]
    except IndexError:
        print(f"\tusage: {sys.argv[0]} <filename>")
        sys.exit(1)

    TEXTFILES = {"macbeth.in", "frankenstein.in", }
    if choice not in TEXTFILES:
        print(f"\tinvalid input file: must be one of {TEXTFILES}")
        sys.exit(1)

    script_dir = Path(__file__).parent 
    filepath = script_dir / choice
    chars_by_freq = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        if IGNORE_FIRST_LINE:
            lines = lines[1:]
        chars_by_freq = get_char_frequency(lines)
        print('lines', len(lines))
        print('longest line', max([len(line) for line in lines]))
        print('unique characters', len(chars_by_freq))
        for i, (k, v) in enumerate(chars_by_freq):
            print(f'{i+1:02d}: {k!r:s} [{v}]')

    if show_plot:
        categories = [x[0] if x[0] != '\n' else '\\n' for x in tuple(chars_by_freq)]
        values = [x[1] for x in tuple(chars_by_freq)]
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.bar(categories, values, color='skyblue', edgecolor='black')
        ax.set_title(f'Symbol Frequency in \'{choice}\'')
        ax.set_xlabel('Symbol')
        ax.set_ylabel('Count')
        ax.grid(True, axis='y')
        plt.show()