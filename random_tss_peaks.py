#######################################################################
### Create set of random 'TSS peaks' for testing of the TFBS script ###
#######################################################################

# Imports
import pandas as pd
from Bio import SeqIO

genome_file = "/home/kevin/resources/genomes/GRCh38_v27_gencode/GRCh38.primary_assembly.genome.fa"

# Load genome
# Load the genome
print("\nLoading genome ....")
genome_dict = SeqIO.to_dict(SeqIO.parse(genome_file, "fasta"))
print("... loaded\n")