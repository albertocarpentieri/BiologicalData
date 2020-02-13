

import requests
from Bio import SeqIO
import pandas as pd

URL = "https://www.uniprot.org"

# Set of original proteins
hmm = open("hmm_search_out.hmmer_align", "r")
original_proteins = ""
for line in hmm:
    if line[0:2]==">>":
        original_proteins+=' '+(line[6:12])


# Mapping Uniprot id to PDB id
r = requests.get("{}/uploadlists/".format(URL), params={'from': 'ACC', 'to': 'PDB_ID', 'format': 'tab', 'query': original_proteins})
print(r.status_code)
mapping = set()
for ele in r.text.split("\n")[1:-1]:
    uniprot_id, pdb_id = ele.split()
    mapping.add(pdb_id)


# Creating list of human SwissProt proteins id
fasta_sequences = SeqIO.parse(open('uniprot-reviewed_Homo_sapiens.fasta'),'fasta')
annotated_humans = []
for fasta in fasta_sequences:
    name = fasta.id
    proteins = name.split("|")[1]
    annotated_humans.append(proteins)


# Create a dictionary with all human proteins in PDB
pdb_human=pd.read_csv("pdb_chain_uniprot.csv")
pdb_human_dict = {}
for i,j in enumerate(pdb_human['SP_PRIMARY']):
    if j in annotated_humans:
        pdb_human_dict.setdefault(j, set()).add(pdb_human.iloc[i,0].upper())


# Add all the proteins not present in the original database which are found as other chains in the same PDB
new_protein = []
for i in pdb_human_dict:
    if len(pdb_human_dict[i].intersection(mapping))>0:
        new_protein.append(i)

# List of original proteins
originals_list = original_proteins.split(" ")[:-1]

# Build the PDB dataset
PDB_dataset = (set(new_protein)).union(set(originals_list))

# Save the dataset
with open('PDB_dataset.txt', 'w') as f:
    for item in PDB_dataset:
        f.write("%s\n" % item)
