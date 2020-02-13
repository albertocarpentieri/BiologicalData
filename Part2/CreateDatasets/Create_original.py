

# Original dataset (sequences retrieved by HMM model)
hmm = open("hmm_search_out.hmmer_align", "r")

proteins_hmmer = []
for line in hmm:
    if line[0:2]==">>":
        proteins_hmmer.append(line[6:12])
original_proteins = set(proteins_hmmer)


# Save the dataset
with open('Original_dataset.txt', 'w') as f:
    for item in original_proteins:
        f.write("%s\n" % item)
