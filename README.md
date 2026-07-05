# BioPython Lab Programs

A collection of beginner-friendly **BioPython lab programs** covering essential bioinformatics tasks such as sequence handling, FASTA processing, GenBank parsing, Entrez queries, sequence alignment, phylogenetic analysis, and 3D structure visualization.

## Programs Included

| File                | Description                                       |
| ------------------- | ------------------------------------------------- |
| `1_basic.py`        | Introduction to BioPython and sequence objects    |
| `2_fasta.py`        | Read and write FASTA files                        |
| `3_genbank.py`      | Parse GenBank records                             |
| `4_fasta2gen.py`    | Convert FASTA data into GenBank-compatible format |
| `5_seqrec.py`       | Work with `SeqRecord` objects                     |
| `6_entrez.py`       | Retrieve biological data using NCBI Entrez        |
| `7_pairwiseAlgn.py` | Perform pairwise sequence alignment               |
| `8.1_fasMuscle.py`  | Prepare FASTA files for MUSCLE alignment          |
| `8.2_genMuscle.py`  | Process MUSCLE alignment results                  |
| `9_phylo.py`        | Construct and visualize phylogenetic trees        |
| `10_3d.py`          | Basic 3D molecular structure visualization        |

## Topics Covered

* DNA, RNA, and Protein sequence manipulation
* FASTA and GenBank file handling
* `Seq` and `SeqRecord` objects
* NCBI Entrez database access
* Pairwise sequence alignment
* Multiple sequence alignment (MUSCLE)
* Phylogenetic tree analysis
* Basic structural bioinformatics

## Requirements

* Python 3.9+
* BioPython

Install BioPython:

```bash
pip install biopython
```

For MUSCLE-related programs, install MUSCLE separately and ensure it is available in your system PATH.

## Repository Structure

```
bio/
├── 1_basic.py
├── 2_fasta.py
├── 3_genbank.py
├── 4_fasta2gen.py
├── 5_seqrec.py
├── 6_entrez.py
├── 7_pairwiseAlgn.py
├── 8.1_fasMuscle.py
├── 8.2_genMuscle.py
├── 9_phylo.py
└── 10_3d.py
```

## Learning Outcomes

After completing these programs, you will be able to:

* Read and manipulate biological sequences using BioPython.
* Parse common bioinformatics file formats.
* Retrieve sequence data from NCBI databases.
* Perform sequence alignments.
* Generate and analyze phylogenetic trees.
* Work with biological sequence metadata.
* Explore basic molecular structure visualization.

## References

* BioPython Documentation: [https://biopython.org/](https://biopython.org/)
* NCBI Entrez: [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/)
* MUSCLE: [https://www.drive5.com/muscle/](https://www.drive5.com/muscle/)

---

*These programs were created as part of a BioPython laboratory course to demonstrate core bioinformatics workflows using the BioPython library.*
