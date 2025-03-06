import subprocess
import csv
import argparse

#Run commands in this module with Popen
def run_shell_cmd(cmd,echo=True,cwd=[]):
    stdout_holder=[]
    if cwd:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,cwd=cwd)
    else:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in process.stdout:
        if echo:
            stdout_holder.append(line.strip())
            process.wait()
    return stdout_holder

#Get number of lines, also an ENCODE function
def get_num_lines(lines):
    command = 'zcat -f {} | wc -l'.format(lines)
    run = ((run_shell_cmd(command)))
    run = run[0].decode("utf-8")
    return (int(run))

#Run shell commands to count total reads and identify intersections with reference file.
#This function adapted from ENCODE's encode_task_annot_enrich.py script, get_fract_reads_in_regions function.
def get_fract_reads_in_regions(input_reads, region_ref):
    print(f'recording overlaps with reference file: {region_ref}')
    cmd = "bedtools sort -i {} | "
    cmd += "bedtools merge -i stdin | "
    cmd += "bedtools intersect -u -nonamecheck -a {} -b stdin | "
    cmd += "wc -l"
    cmd = cmd.format(region_ref, input_reads)
    intersect_read_count = (run_shell_cmd(cmd))
    intersect_read_count = int(intersect_read_count[0].decode("utf-8")) #converting intersection results broken apart
    total_read_count = get_num_lines(input_reads)
    fract_reads = float(intersect_read_count) / total_read_count
    return fract_reads

def filter_reference(input_reads, genome):
    dhs_ref = ref_files_location + genome + '_dhs.bed.gz'
    blacklist_ref = ref_files_location + genome + '_blacklist.bed.gz'
    promoter_ref = ref_files_location + genome + '_promoter.bed.gz'
    enhancer_ref = ref_files_location + genome + '_enhancer.bed.gz'
    dhs = get_fract_reads_in_regions(input_reads, dhs_ref)
    blacklist = get_fract_reads_in_regions(input_reads, blacklist_ref)
    promoter = get_fract_reads_in_regions(input_reads, promoter_ref)
    enhancer = get_fract_reads_in_regions(input_reads, enhancer_ref)
    return dhs, blacklist, promoter, enhancer

if __name__ == "__main__":
    #assign argument parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='file input (.tsv, .csv, or BED file format, .gz optional)')
    parser.add_argument('--genome', type=str, help='species/genome type, name must match reference files')
    parser.add_argument('--ref', type=str, help='region reference folder containing minimum DHS, blacklist, enhancer and promoter files')
    #Only use the below argument 'debug; to verify installation. Ignore if the script works correctly.
    parser.add_argument( '-d', '--debug', default=False, help='Set this optional argument to True to test correct setup of this script using default verification files')
    args = parser.parse_args()  
    ref_files_location = args.ref 
    input = args.input
    genome = args.genome
    
    # debug input lines below, use the debug option argument to verify script (and pre-req) installation
    if args.debug == "True":
        print("Debug mode enabled, using test files")    
        # input = "./debug/pbmc_granulocyte_sorted_10k_atac_fragments.tsv.gz"
        input = "./debug/micro.tsv"
        genome = 'hg38'
        ref = './ref/'
    
    print(f"getting intersecting reads from {input}")
    intersect = filter_reference(input, genome)

    # optional terminal output:
    print(f"fraction of reads in DHS: {intersect[0]}")
    print(f"fraction of reads in Blacklist: {intersect[1]}")
    print(f"fraction of reads in Promoter: {intersect[2]}")
    print(f"fraction of reads in Enhancer: {intersect[3]}")

    # get output file name and export as .csv
    file = str(input)
    try: #attempt to split file name using standard .tsv naming scheme
        file = file.split('/')[-1].split('.tsv')[0]
    except IndexError: #if that fails just grab the full name
        file = file
    out = file + '_regionreport.csv'
    print(f"writing to file: {out}")
    compiled_overlaps = [['DHS', intersect[0]], ['Blacklist', intersect[1]], ['Promoter', intersect[2]], ['Enhancer', intersect[3]]]
    with open(out, 'w', newline='') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerows(compiled_overlaps)