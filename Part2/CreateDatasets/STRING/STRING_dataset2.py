
from Bio import SeqIO

# Creating list of original proteins
original_proteins = []
with open("Original_dataset.txt") as original:
  for i in original:
    original_proteins.append(i[:-1])


# Creating list of converted ids
fasta_sequences = SeqIO.parse(open('string_converted.fasta'),'fasta')
string_proteins = []
for fasta in fasta_sequences:
  name = fasta.id
  proteins = name.split("|")[1]
  string_proteins.append(proteins)

# Make the union to create STRING dataset
string = set(original_proteins).union(string_proteins)

# Save the dataset
with open('STRING_dataset.txt', 'w') as f:
    for item in string:
        f.write("%s\n" % item)
