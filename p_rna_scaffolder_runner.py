#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @created: 26.07.2021
# @author: Danil Zilov
# @contact: zilov.d@gmail.com

import argparse
import os
from inspect import getsourcefile
from datetime import datetime
import string
import random
from scripts.config_maker import config
from tqdm import tqdm

def snakerun(snakefile, threads, config_file, debug):
    if debug:
        snake_debug = "-n"
    else:
        snake_debug = ""

    command = f"snakemake --snakefile {snakefile} --configfile {config_file} " \
              f"--cores {threads} --use-conda --conda-frontend mamba {snake_debug}"
    print(command)
    os.system(command)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Wrapper to use few RNA reads pairs')
    parser.add_argument('-a', '--assembly', help="path to assembly file in FASTA format", required=True)
    parser.add_argument('-1', '--forward_reads', help="path to forward short read file in FASTQ format, "
                                                      "may be list of files", nargs= "+", required=True)
    parser.add_argument('-2', '--reverse_reads', help="path to reverse short read file in FASTQ format "
                                                      "may be list of files", nargs= "+", required=True)
    parser.add_argument('-p', '--prefix', help="prefix for output scaffold", default="complete")
    parser.add_argument('-o', '--outdir', help='output directory [Required]', required=True)
    parser.add_argument('-t', '--threads', help='number of threads [default == 8]', default="8")
    parser.add_argument('-d', '--debug', help='debug mode', action='store_true')
    parser.add_argument('-i', '--intron_length', help='maximum intron length', default="100000")

    args = vars(parser.parse_args())

    assembly = args["assembly"]
    forward_reads = args["forward_reads"]
    reverse_reads = args["reverse_reads"]
    prefix = args["prefix"]
    outdir = os.path.abspath(args["outdir"])
    intron_length = args["intron_length"]
    threads = args["threads"]
    debug = args["debug"]

    if len(forward_reads) != len(reverse_reads):
        raise ValueError("Number of forward and reverse reads should be equal, please check the command!")
    else:
        forward_reads.sort()
        reverse_reads.sort()

    execution_folder = os.path.dirname(os.path.dirname(os.path.abspath(getsourcefile(lambda: 0))))
    snakefile = os.path.join(execution_folder, 'scripts/Snakefile')

    for i in tqdm(range(len(forward_reads))):
        run_prefix = os.path.splitext(os.path.basename(forward_reads[i]))[0]

        execution_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        random_letters = "".join([random.choice(string.ascii_letters) for n in range(3)])
        config_file = os.path.join(execution_folder, f"config/config_{random_letters}{execution_time}.yaml")

        config(os.path.abspath(forward_reads[i]), os.path.abspath(reverse_reads[i]), assembly,
               run_prefix, outdir, intron_length, config_file)
        snakerun(snakefile, threads, config_file, debug)
        assembly = os.path.join(outdir, f"tmp/scaffolds/{run_prefix}.fasta")
        if i == len(forward_reads):
            complete_assembly = os.path.join(outdir, f"{prefix}_scaffolds.fasta")
            os.system(f"mv {assembly} {complete_assembly}")
            print("Complete!")
