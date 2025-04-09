# dna-aligner: Command Line Sequence Alignment Tool 
DNA sequence alignment is a bioinformatics tool used to analyze mutation detection, common evolutionary descent, and protein structure and function, etc.

This sequence alignment tool uses Hirschberg's dynamic programming algorithm to implement global alignment (Needleman-Wunsch) with affine gap penalties and local alignment (Smith-Waterman).

The dna-aligner tool is a simple command line tool that reads a .txt file. It processes this .txt file and generates the global alignment and local alignment. It also specifies the specific starting location of the local alignment for both strings. The result is output to a file. 

No extra required packages such as Numpy are needed. 

## Steps To Install
* Git Clone
    * In your own terminal, run the following command:
      ```
      git clone https://github.com/ou-elot/dna-aligner
      ```
    * run `ls` in your terminal to make sure there is a directory called `dna-aligner`.
* Swap Directories
    1. Swap to `dna-aligner` by running command `cd dna-aligner`
    2. One more directory swap to `align` by running command `cd align`
    3. Now when running command `ls`, there should be three files: `aligner_tools.py`, `dna_aligner.py`, and `sequence_test.txt`
## Usage
* Help Page
    * Run `python3 dna_aligner.py -h` to see all required args for this python script.
* Example Usage
    * Runs both global and local alignment: `python3 dna_aligner.py sequences.txt --match 1 --mismatch 1 --gap_open 2 --gap_extend 1`
    * Runs only global alignment: `python3 dna_aligner.py sequences.txt --match 1 --mismatch 1 --gap_open 2 --gap_extend 1 --global_align`
    * Runs only local alignment: `python3 dna_aligner.py sequences.txt --match 1 --mismatch 1 --gap_open 2 --gap_extend 1 --local_align`
    * Specifies ouput file location: `python3 dna_aligner.py sequences.txt --match 1 --mismatch 1 --gap_open 2 --gap_extend 1 --output my_results.txt`
    * **Note that all integer inputs for alignment scoring args should be positive. The dna-aligner tool automatically calculates penalties as negative** 
