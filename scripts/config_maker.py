def config(forward_read, reverse_read, assembly, prefix, outdir, intron_length, config_file):
    assembly_prefix = os.path.splitext(os.path.basename(assembly))[0]
    config = f"""
assembly: "{assembly}"
forward_read: "{forward_read}"
reverse_read: "{reverse_read}"
prefix: "{prefix}"
intron_length = "{intron_length}"
tmp_dir = "{outdir}/tmp/"

assembly_index_dir = "{outdir}/tmp/assembly_index"
assembly_index = "{outdir}/tmp/assembly_index/{assembly_prefix}.1.ht2"
assembly_index_prefix = "{outdir}/tmp/assembly_index/{assembly_prefix}"
alignment: "{outdir}/tmp/alignment/{prefix}.sam"

scaffolder = "{outdir}/tmp/P_RNA_scaffolder/P_RNA_scaffolder.sh"
scaffolder_dir = "{outdir}/tmp/P_RNA_scaffolder"

scaffolds_dir = "{outdir}/tmp/scaffolds"
scaffold_raw: "{outdir}/tmp/scaffolds/P_RNA_scaffolder.fasta"
scaffold: "{outdir}/tmp/scaffolds/{prefix}.fasta"
    """

    with open(config_file, "w") as fw:
        fw.write(config)
