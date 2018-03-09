#######################################################################
### Create set of random 'TSS peaks' for testing of the TFBS script ###
#######################################################################

# Imports
import pandas as pd
from Bio import SeqIO
import random
import numpy as np

genome_file = "/home/kevin/resources/genomes/GRCh38_v27_gencode/GRCh38.primary_assembly.genome.fa"

# Load genome
# Load the genome
print("\nLoading genome ....")
genome_dict = SeqIO.to_dict(SeqIO.parse(genome_file, "fasta"))
print("... loaded\n")

peak_length = 27
no_of_peaks = 3000
ext_range = 500

peaks = []
random.seed(12345)
for i in range(no_of_peaks):
    chr_no = random.randint(1,22)
    chr = "chr" + str(chr_no)
    seq = genome_dict[chr]
    max_end = len(seq) - ext_range
    pos = random.randint(ext_range, max_end)
    start = pos
    end = pos + peak_length
    strand = '-'
    if random.randint(1,2) == 1:
        strand = '+'
    final_peak = chr + "_" + str(start) + "_" + str(end) + "_" + strand
    peaks.append(final_peak)

padj = np.repeat(0.01, no_of_peaks)
lfc = np.repeat(1.5, no_of_peaks)

cols = ['', 'padj', 'log2FoldChange']
df1 = pd.DataFrame(pd.Series(peaks))
df2 = pd.DataFrame(pd.Series(padj))
df3 = pd.DataFrame(pd.Series(lfc))
df = pd.concat([df1, df2, df3], axis=1)

df.to_csv("test_data_frame.txt", sep="\t")

