

from Bio import SeqIO

# List of STRING ids (from string website)
string_ids = []
with open ('string_protein_sequences.fa') as inp:
    for line in inp:
        if line[0]==">":
            id_string = line.split("\t")[1]
            string_ids.append(id_string)
            print(id_string)


# Save the dataset
with open('String_ids.txt', 'w') as f:
    for item in string_ids:
        f.write("%s\n" % item)
