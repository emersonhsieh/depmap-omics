# depmap-omics

Python scripts for cleaning up gene expression data from the DepMap project.

## Required Data

Omics data are downloaded from https://depmap.org/portal/data_page.

Download the following two files and place them in the `csv directory.

`OmicsExpressionProteinCodingGenesTPMLogp1.csv`

- Gene expression TPM values of the protein coding genes for DepMap cell lines. Values are inferred from RNA-seq data using RSEM (unstranded mode), and are reported after log2 transformation, using a pseudo-count of 1; log2(TPM+1). Additional RNA-seq-based expression measurements are available for download as part of the full DepMap Data Release. More information on the DepMap Omics processing pipeline is available at https://github.com/broadinstitute/depmap_omics.
- 460.9 MB

`OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv`

- Gene expression TPM values of the protein coding genes for DepMap cell lines. Values are inferred from RNA-seq data using RSEM (stranded or unstranded mode, depending on each sample's sequencing protocol) and are reported after log2 transformation, using a pseudo-count of 1; log2(TPM+1). To see if a sample was run using the stranded or unstranded protocol, please refer to OmicsProfiles and OmicsDefaultModelProfiles. Batch-corrected for strandedness using ComBat https://academic.oup.com/nargab/article/2/3/lqaa078/5909519. Additional RNA-seq-based expression measurements are available for download as part of the full DepMap Data Release. More information on the DepMap Omics processing pipeline is available at https://github.com/broadinstitute/depmap_omics.
- 558.9 MB

## Setup

For an existing clone of this repository, run the following:

```python3
# Create virtual environment
python3 -m venv .venv
source ./.venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

Run script:

```python3
# Activate environment
source ./.venv/bin/activate

# Run script
cd scripts
python3 -i collate.py
python3 -i reshuffle.py
```

## Notes

Installing new packages:

```python3
pip3 install pandas
```

Freezing requirements:

```python3
pip3 freeze > requirements.txt
```

## Linear Association

`reshuffle_compound_to_expression.py` shuffles data to match the order of the data.
