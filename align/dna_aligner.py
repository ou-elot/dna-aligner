import argparse
from aligner_tools import global_alignment, localAlignment

def read_sequences(filepath):
    with open(filepath, "r") as file:
        lines = file.read().strip().split("\n")
        if len(lines) != 2:
            raise ValueError("File must contain exactly two lines for two DNA sequences.")
        return lines[0], lines[1]

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
    parser.add_argument("--global-align", action="store_true", help="Run only global alignment.")
    parser.add_argument("--local-align", action="store_true", help="Run only local alignment.")

    args = parser.parse_args()

    # Read sequences from file
    seq1, seq2 = read_sequences(args.filepath)

    results = []

    # Run Global Alignment if specified or if no specific option is given
    if args.global_align or (not args.global_align and not args.local_align):
        score, aligned_seq1, aligned_seq2 = global_alignment(
            args.match, args.mismatch, args.gap_open, args.gap_extend, seq1, seq2
        )
        results.append("Global Alignment:")
        results.append(aligned_seq1)
        results.append(aligned_seq2)
        results.append("")

    # Run Local Alignment if specified or if no specific option is given
    if args.local_align or (not args.global_align and not args.local_align):
        score, aligned_seq1, aligned_seq2, start_x, start_y = local_alignment(
            seq1, seq2, args.match, args.mismatch, args.gap_open
        )
        results.append("Local Alignment:")
        results.append(f"{aligned_seq1} starting at position {start_x}")
        results.append(f"{aligned_seq2} starting at position {start_y}")
        results.append("")

    # Write results to output file
    with open(args.output, "w") as f:
        f.write("\n".join(results))

    print(f"Alignment results saved to {args.output}")

if __name__ == "__main__":
    main()

