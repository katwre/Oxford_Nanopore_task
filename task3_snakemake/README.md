-----
# Summary

It's a small Snakemake pipeline that takes the input reads in the FASTA format (hard-coded as ../../data/read.fa) and the 10-species reference in the FASTA format (hard-coded as ../../data/ten_species_community_refs.fa) and outputs an indexed and sorted BAM file (mapped_reads/reads.sorted.bam).

# How to run it

snakemake -s ./snakemake.py --cores INT, where INT is a number of cores

For example:
snakemake -s ./snakemake.py --cores 1

For more information on snakemake check out https://snakemake.readthedocs.io.

# Dependencies

The following tools must be available:
- snakemake (tested with version 6.15.1) 
- minimap2 (tested with version 1.13)
- samtools (tested with version 2.24-r1122)





