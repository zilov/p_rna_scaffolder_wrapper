# P_RNA_scaffolder wrapper

The wrapper was written to automate the work of P_RNA_scaffolder with the list of RNAseq reads.
It creates assembly index, reads alignment and runs P_RNA_scaffolder automatically with one command!

After first scaffold created wrapper takes it to build index and align next reads pair to the scaffold.

Wrapper based on Snakemake, so ypu do not need to install any tools into your system. 

# Installation

Use conda (or mamba) to install the wrapper into the new environment 

`> conda create -n p_rna_wrapper_env -c bioconda -c conda-forge -c aglab p_rna_wrapper`

Before running activate the environment:

```
> conda deactivate
> conda activate p_rna_wrapper_env
```

# Usage


To run wrapper use following command:

`> p_rna_wrapper.py -a {path_to_assemlby.fasta} -1 {space separated list of forward reads} -2 {reverse_reads} 
-p {output_prefix} -i {intron_length} -t {threads number}`

# Arguments
```
-a ASSEMBLY, --assembly ASSEMBLY
                        path to assembly file in FASTA format
-1 FORWARD_READS [FORWARD_READS ...], --forward_reads FORWARD_READS [FORWARD_READS ...]
                 path to forward short read file in FASTQ format, may be space-separated list of files
-2 REVERSE_READS [REVERSE_READS ...], --reverse_reads REVERSE_READS [REVERSE_READS ...]
                 path to reverse short read file in FASTQ format may be space-separated list of files
-p PREFIX, --prefix PREFIX
                 prefix for output scaffold [default == complete]
-i INTRON_LENGTH, --intron_length INTRON_LENGTH
                 maximum intron length [default == 100000]
-o OUTDIR, --outdir OUTDIR 
                 output directory
-t THREADS, --threads THREADS
                 number of threads [default == 8]
-d, --debug      debug mode
```

# Output

As an output you will get folder with "tmp" folder inside and complete scaffold file.

Tmp folder collects data from each index-alignment-scaffold cycle.
