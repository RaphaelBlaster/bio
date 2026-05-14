import subprocess
from Bio import AlignIO

muscle_exe = r"C:\Users\Admin\muscle3.8.31_i86win32.exe"

try:
    subprocess.run([muscle_exe, "-in", "input_sequences.fasta", "-out", "aligned_sequences.fasta"], check=True)
    alignment = AlignIO.read("aligned_sequences.fasta", "fasta")
    print(alignment)
except FileNotFoundError:
    print("Error: MUSCLE executable not found. Check the path:", muscle_exe)
except subprocess.CalledProcessError as e:
    print(f"Error running MUSCLE: {e}")
