# BiologicalData

1- We've done 3 iterations of PSIBLAST, providing our sequence as input. We've used BLOSUM-62 substitution matrix and UniprotKB database. E-Threshold value was set to 0.001. ,  500 sequences
2 - Blast, uniref90, evalue 0.01,  500 sequences
3 - Blast, uniref90, evalue 0.001,  500 sequences
	
	Output: psiblast.fasta.

I've generated MSA from psiblast.fasta using Clustal Omega.
Output: clustalo.clustal

	We’ve cut the sequences with Jalview.
	Output: msa_cut.aln

Build a PSSM model starting from the MSA using BLAST
	Output: pssm_s.pssm


Build a HMM model starting from the MSA using HMMER.
Output: hmm.hmm
logo: logo.png (with skylign)

Evaluate your model against human proteins available in SwissProt
1.Define you ground truth/reference by finding all human proteins in SwissProt annotated (and not annotated) with the assigned Pfam ID (provided).
To obtain all human proteins containing our domain we have searched Uniprot with query: PF00595 AND reviewed:yes AND organism:"Homo sapiens (Human) [9606]"
Output: uniprot-PF00595 -reviewed_Homo_sapiens

 	We then downloaded all human protein from SwissProt:
reviewed:yes AND organism:"Homo sapiens (Human) [9606]"
	Output: uniprot -reviewed_Homo_sapiens

2."Find significant hits using HMM-SEARCH and PSI-BLAST respectively for the HMM and PSSM model"

	hmm: hmmsearch.hmmer_dotblout & hmm_search_out.hmmer_align
		pssm: output_psiblast.txt


3.‘Evaluate the ability of retrieving proteins with that domain’
    evaluation.py
  
  4.‘Evaluate the ability of matching the domain position, i.e. the alignment position of the model in the retrieved proteins (Pfam reference position is available in InterPro).’

export.json contain a list of approximately 621 UniProt proteins which match with the pfam entry with accession PF00595 and the uniprot taxon with accession 9606, obtained searching in interpro website
	
evaluation_position.py

PART 2


A) Create Datasets
create the architectures datasets from the output of  SearchHMM
  script: architectures_dicts_split.py (output: architectures_datasets)

	
create PDB network
script: PDB_dataset.py 		output: PDB_dataset.txt 


Create STRING network
script: 					output: 

B)Annotation enrichment

GO tree terms used in code:
http://geneontology.org/docs/ontology-relations/


Python code:


C) Structural classification
CATH DB:
search results: http://www.cathdb.info/version/v4_2_0/superfamily/2.30.42.10

Superfamily 2.30.42.10
Superfamily: PDZ domain
This superfamily entry comprises PDZ domains, also known as Discs-large homologous regions (DHR) or glycine-leucine-glycine-phenylalanine (GLGF), which are found in diverse signalling proteins in bacteria, yeasts, plants, insects and vertebrates. PDZ is an acronym derived from the names of the first proteins in which the domain was observed - post-synaptic density protein 95 (PSD-95), a synaptic protein found in the brain, Discs large from Drosophila (Dlg1) and zona occludens 1 (ZO-1), which are involved in cell signalling.
No of domains in this family:878
Unique Species:15649
Unique GO terms: 1685


