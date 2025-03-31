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
    parser = argparse.ArgumentParser(
        description="DNA Sequence Alignment Tool: Perform global or local sequence alignment."
    )
    parser.add_argument("filepath", help="Path to the file containing two DNA sequences.")
    parser.add_argument("--match", type=int, required=True, help="Match score (required).")
    parser.add_argument("--mismatch", type=int, required=True, help="Mismatch penalty (required).")
    parser.add_argument("--gap_open", type=int, required=True, help="Gap opening penalty (required).")
    parser.add_argument("--gap_extend", type=int, required=True, help="Gap extension penalty (required).")
    parser.add_argument("--output", type=str, default="result.txt", help="Output file (default: result.txt).")
    parser.add_argument("--global", action="store_true", help="Run only global alignment.")
    parser.add_argument("--local", action="store_true", help="Run only local alignment.")

    args = parser.parse_args()
    seq1, seq2 = read_sequences(args.filepath)

    with open(args.output, "w") as f:
        if args.global:
            score, aligned_s, aligned_t = global_alignment(args.match, args.mismatch, args.gap_open, args.gap_extend, seq1, seq2)
            f.write(f"Global Alignment:\n{aligned_s}\n{aligned_t}\n\n")
        elif args.local:
            score, aligned_s, aligned_t, x, y = local_alignment(seq1, seq2, args.match, args.mismatch, args.gap_open)
            f.write(f"Local Alignment:\n{aligned_s} starting at position {x}\n{aligned_t} starting at position {y}\n")
        else:
            # Default: Run both
            f.write("Running both alignments...\n\n")
            main()  # Call itself to run both

if __name__ == "__main__":
    main()
