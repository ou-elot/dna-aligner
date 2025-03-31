import argparse
from aligner_tools import global_alignment, localAlignment

def read_sequences(filepath):
    with open(filepath, "r") as file:
        lines = file.read().strip().split("\n")
        if len(lines) != 2:
            raise ValueError("File must contain exactly two lines for two DNA sequences.")
        return lines[0], lines[1]

def write_output(filepath, content):
    """Writes the alignment result to a file."""
    with open(filepath, "w") as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="DNA Sequence Alignment Tool")
    parser.add_argument("filepath", type=str, help="Path to the file containing two DNA sequences.")
    parser.add_argument("alignment_type", choices=["global", "local"], help="Type of alignment to perform.")
    parser.add_argument("--match", type=int, default=1, help="Match reward (default: 1)")
    parser.add_argument("--mismatch", type=int, default=1, help="Mismatch penalty (default: 1)")
    parser.add_argument("--gap_open", type=int, default=1, help="Gap opening penalty (default: 1)")
    parser.add_argument("--gap_extend", type=int, default=1, help="Gap extension penalty (default: 1)")
    parser.add_argument("--output", type=str, default="alignment_output.txt", help="Output file name (default: alignment_output.txt)")

    args = parser.parse_args()
    seq1, seq2 = read_sequences(args.filepath)

    output_content = ""

    if args.alignment_type == "global":
        score, aligned_s, aligned_t = global_alignment(
            args.match, args.mismatch, args.gap_open, args.gap_extend, seq1, seq2
        )
        output_content = f"Global Alignment:\n{aligned_s}\n{aligned_t}\n"

    elif args.alignment_type == "local":
        score, aligned_s, aligned_t, start_x, start_y = local_alignment(
            seq1, seq2, args.match, args.mismatch, args.gap_open
        )
        output_content = f"Local Alignment:\n{aligned_s} starting at position {start_x}\n{aligned_t} starting at position {start_y}\n"

    write_output(args.output, output_content)
    print(f"Alignment results saved to {args.output}")

if __name__ == "__main__":
    main()
