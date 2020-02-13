from Bio import SeqIO
import math

# Sequences really containing the domain PF00595 (from swissprot)
fasta_sequences = SeqIO.parse(open('uniprot-PF00595_reviewed_Homosapiens.fasta'),'fasta')
proteins_true = []
for fasta in fasta_sequences:
    name = fasta.id
    proteins = name.split("|")[1]
    print(proteins)
    proteins_true.append(proteins)

# print the number of proteins found
print(len(proteins_true))


# PSSM evaluation

# Sequences retrieved by PSIBLAST
psi = open("psiblast_out.txt", "r")
proteins_psi = []
for line in psi:
    if line[0]==">":
        proteins_psi.append(line[1:7])

# How many?
print(len(proteins_psi))

# True positive
TP = len(list(set(proteins_true).intersection(proteins_psi)))
# False Positive
FP=len(proteins_psi)-TP
# False Negative
FN = len(proteins_true)-TP
# True Negative
TN = 20367- (TP + FP + FN)
print("TP: {}\nFP: {}\nFN: {}\nTN:{}".format(TP,FP,FN,TN))

# PSSM metrics
acc = (TP + TN) / (TP + TN + FP + FN)
pre = (TP) / (TP + FP)
sen = TP / (TP + FN)
spe = TN / (TN + FP)
mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))

print("PSSM metrics:")
print(f"accuracy: {acc}")
print(f"precision: {pre}")
print(f"sensitivity: {sen}")
print(f"specificity: {spe}")
print(f"mcc: {mcc}")




# HMM evaluation

# Sequences retrieved by HMMER
psi = open("results/hmmsearch_out.hmmer_align", "r")
proteins_hmmer = []
for line in psi:
    if line[0:2]==">>":
        proteins_hmmer.append(line[6:12])

# How many?
print(len(proteins_hmmer))

# True positive
TP = len(list(set(proteins_true).intersection(proteins_hmmer)))
# False Positive
FP=len(proteins_hmmer)-TP
# False Negative
FN = len(proteins_true)-TP
# True Negative
TN = 20367- (TP + FP + FN)
print("TP: {}\nFP: {}\nFN: {}\nTN:{}".format(TP,FP,FN,TN))

# HMM metrics
acc = (TP + TN) / (TP + TN + FP + FN)
pre = (TP) / (TP + FP)
sen = TP / (TP + FN)
spe = TN / (TN + FP)
mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))

print("HMM metrics:")
print(f"accuracy: {acc}")
print(f"precision: {pre}")
print(f"sensitivity: {sen}")
print(f"specificity: {spe}")
print(f"mcc: {mcc}")
