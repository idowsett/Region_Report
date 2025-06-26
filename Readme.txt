This script's goal is to provide specific region data for single cell ATAC-seq, or other chromatin accessibility assay type, test files. This is a function baked into ENCODE for bulk ATAC-seq data but is not available as a standalone function compatible to be slotted into custom single cell scATAC-seq analysis pipelines. The goal is to isolate that function and make it generally agnostic to up- or downstream processing steps.
It also allows for this step to run quickly and efficiently as a quick quality check.

How it works: 
The script targets specific regions of interest (enhancer, promoter, ENCODE blacklist and TSS regions) and reports how many reads in user sequencing data (from a processed BED file or tsv file) overlap these regions.

Reference files pulled from the ENCODE project:
https://github.com/ENCODE-DCC/atac-seq-pipeline/blob/master/scripts/download_genome_data.sh

Specific files available by default and included in this script:
hg38
    BLACKLIST="https://www.encodeproject.org/files/ENCFF356LFX/@@download/ENCFF356LFX.bed.gz"
    TSS="https://www.encodeproject.org/files/ENCFF493CCB/@@download/ENCFF493CCB.bed.gz"
    DNASE="https://www.encodeproject.org/files/ENCFF304XEX/@@download/ENCFF304XEX.bed.gz"
    PROM="https://www.encodeproject.org/files/ENCFF140XLU/@@download/ENCFF140XLU.bed.gz"
    ENH="https://www.encodeproject.org/files/ENCFF212UAV/@@download/ENCFF212UAV.bed.gz"

mm10
    BLACKLIST="https://www.encodeproject.org/files/ENCFF547MET/@@download/ENCFF547MET.bed.gz"
    TSS="https://www.encodeproject.org/files/ENCFF498BEJ/@@download/ENCFF498BEJ.bed.gz"
    DNASE="https://www.encodeproject.org/files/ENCFF015KVI/@@download/ENCFF015KVI.bed.gz"
    PROM="https://www.encodeproject.org/files/ENCFF206BQS/@@download/ENCFF206BQS.bed.gz"
    ENH="https://www.encodeproject.org/files/ENCFF580RGZ/@@download/ENCFF580RGZ.bed.gz"

Initial setup:
Run the download.sh script to download the appropriate files from ENCODE. Optionally, customize this script or manually download alternate
reference files for other genomes (eg hg19), available on ENCODE's git listed above and execute using the simple bash command:
bash download.sh

New or alternate reference files can be used, simply add to ref folder and save using a matching naming scheme [genome_name]_[feature_type].bed.gz

Script Usage directions:
python --input [test file (bed format)] --genome [species/genome ID, either hg38 or mm10 by default] --ref [reference folder, default: ./ref]

Testing initial installation, use the debug function (any specified other arguments will work in this case, be sure to remove debug option otherwise): 
python --input [test file (bed format)] --genome [species/genome ID, either hg38 or mm10 by default] --ref [reference folder, default: ./ref] --debug True

example:
python --input test_file.bed --genome hg38 --ref ./ref

note: Actual reference genome is not needed for the script to function merely the name and reference bed files of region annotation.
