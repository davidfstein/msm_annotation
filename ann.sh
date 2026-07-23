#!/usr/bin/env bash
#BSUB -P acc_Itan_lab
#BSUB -q premium
#BSUB -n 20
#BSUB -R span[hosts=1]
#BSUB -o %J.stdout
#BSUB -e %J.stderr
#BSUB -R rusage[mem=4000MB]
#BSUB -W 48:00

ml proxies

for f in /sc/arion/projects/MSM/data/WES/new_rgn/batch_002/pVCF/*vcf.gz; do
    if [[ ! -f $(basename $f .vcf.gz).tsv ]]; then
        bcftools view -G $f -Oz -o sites_only.vcf.gz
        annotate_msm -i sites_only.vcf.gz -o $(basename $f .vcf.gz).tsv --bind_dirs /sc/arion/projects/Itan_lab/david/.vep/
        rm sites_only.vcf.gz
    fi
done
