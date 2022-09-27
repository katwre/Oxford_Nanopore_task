#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculate number of reads that map to Enterococcus faecalis (to a genome called "Enterococcus_faecalis_complete_genome").

Example usage: 
task4_pysam.py bam_file
where bam_file is a path to a sorted and indexed BAM file
"""


import argparse
import os.path
import pysam


# helper function to check whether input file exists
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)

parser = argparse.ArgumentParser(description='''Task 4. \n
It's a small script that accepts a sorted and indexed BAM file as input and counts how many reads in your BAM file map to Enterococcus faecalis. \n
Example usage: task4_pysam.py reads.sorted.bam''',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('bam_file',
                    # print a help message for the argument
                    help="A sorted and indexed BAM file",
                    # print error message if argument is not valid
                    type=argparse.FileType('r', encoding='UTF-8'))

args = parser.parse_args()
config = vars(args)

# get path to the input file
filename = config["bam_file"]

# read an input bam file
bamfile = pysam.AlignmentFile(filename, "rb")

# count number of all reads that map to Enterococcus faecalis 
n_reads_ef = bamfile.count(contig="Enterococcus_faecalis_complete_genome")
print("Number of mapped reads into Enterococcus faecalis = %d" % n_reads_ef)

# close the input BAM file
bamfile.close()
