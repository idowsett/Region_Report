# hg38 files
# BLACKLIST="https://www.encodeproject.org/files/ENCFF356LFX/@@download/ENCFF356LFX.bed.gz"
mkdir ./ref
wget -O ./ref/hg38_blacklist.bed.gz "https://www.encodeproject.org/files/ENCFF356LFX/@@download/ENCFF356LFX.bed.gz"
    # TSS="https://www.encodeproject.org/files/ENCFF493CCB/@@download/ENCFF493CCB.bed.gz"
wget -O ./ref/hg38_tss.bed.gz "https://www.encodeproject.org/files/ENCFF493CCB/@@download/ENCFF493CCB.bed.gz"
    # DNASE="https://www.encodeproject.org/files/ENCFF304XEX/@@download/ENCFF304XEX.bed.gz"
wget -O ./ref/hg38_dhs.bed.gz "https://www.encodeproject.org/files/ENCFF304XEX/@@download/ENCFF304XEX.bed.gz"
    # PROM="https://www.encodeproject.org/files/ENCFF140XLU/@@download/ENCFF140XLU.bed.gz"
wget -O ./ref/hg38_promoter.bed.gz "https://www.encodeproject.org/files/ENCFF140XLU/@@download/ENCFF140XLU.bed.gz"
    # ENH="https://www.encodeproject.org/files/ENCFF212UAV/@@download/ENCFF212UAV.bed.gz"
wget -O ./ref/hg38_enhancer.bed.gz "https://www.encodeproject.org/files/ENCFF212UAV/@@download/ENCFF212UAV.bed.gz"

#mm10 files
# BLACKLIST="https://www.encodeproject.org/files/ENCFF547MET/@@download/ENCFF547MET.bed.gz"
wget -O ./ref/mm10_blacklist.bed.gz "https://www.encodeproject.org/files/ENCFF547MET/@@download/ENCFF547MET.bed.gz"
# TSS="https://www.encodeproject.org/files/ENCFF498BEJ/@@download/ENCFF498BEJ.bed.gz"
wget -O ./ref/mm10_tss.bed.gz "https://www.encodeproject.org/files/ENCFF498BEJ/@@download/ENCFF498BEJ.bed.gz"
# DNASE="https://www.encodeproject.org/files/ENCFF015KVI/@@download/ENCFF015KVI.bed.gz"
wget -O ./ref/mm10_dhs.bed.gz "https://www.encodeproject.org/files/ENCFF015KVI/@@download/ENCFF015KVI.bed.gz"
# PROM="https://www.encodeproject.org/files/ENCFF206BQS/@@download/ENCFF206BQS.bed.gz"
wget -O ./ref/mm10_promoter.bed.gz "https://www.encodeproject.org/files/ENCFF206BQS/@@download/ENCFF206BQS.bed.gz"
# ENH="https://www.encodeproject.org/files/ENCFF580RGZ/@@download/ENCFF580RGZ.bed.gz"
wget -O ./ref/mm10_enhancer.bed.gz "https://www.encodeproject.org/files/ENCFF580RGZ/@@download/ENCFF580RGZ.bed.gz"

