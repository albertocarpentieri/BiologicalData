# Searching with PSSM against database containing SwissProt human proteins
# makeblastdb is used to create a database from our fasta file uniprot_reviewed_Homo_sapiens.fasta


makeblastdb -dbtype prot -in uniprot_reviewed_Homo_sapiens.fasta -parse_seqids

psiblast -in_pssm pssm_u90.pssm -db uniprot-reviewed_Homo_sapiens.fasta -num_iterations 1 -evalue 0.001 >result_search_pssm.txt
