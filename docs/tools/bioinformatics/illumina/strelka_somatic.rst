
.. include:: strelka_somatic_2.9.10
.. include:: strelka_somatic_2.9.9

Strelka (Somatic)
===================================

Description
-------------

Tool identifier: ``strelka_somatic``

Tool path: ``janis_bioinformatics.tools.illumina.strelkasomatic.strelkasomatic import StrelkaSomatic_2_9_10``

Version: 2.9.10

Container: ``michaelfranklin/strelka:2.9.10``

Versions
*********

- 2.9.10 (current)
- `2.9.9 <strelka_somatic_2.9.9.html>`_

Documentation
-------------

URL
******
*No URL to the documentation was provided*

Tool documentation
******************
Usage: configureStrelkaSomaticWorkflow.py [options]
Version: 2.9.10
This script configures Strelka somatic small variant calling.
You must specify an alignment file (BAM or CRAM) for each sample of a matched tumor-normal pair.
Configuration will produce a workflow run script which can execute the workflow on a single node or through
sge and resume any interrupted execution.

Outputs
-------
============  ==========  ===========================================================================================================================================================================================================================================
name          type        documentation
============  ==========  ===========================================================================================================================================================================================================================================
configPickle  File
script        File
stats         tsv         A tab-delimited report of various internal statistics from the variant calling process: Runtime information accumulated for each genome segment, excluding auxiliary steps such as BAM indexing and vcf merging. Indel candidacy statistics
indels        vcf-gz-tbi
snvs          vcf-gz-tbi
============  ==========  ===========================================================================================================================================================================================================================================

Inputs
------
Find the inputs below

Required inputs
***************

=========  =============  =================  ==========  ====================================================================
name       type           prefix               position  documentation
=========  =============  =================  ==========  ====================================================================
normalBam  BamPair        --normalBam=                1  Normal sample BAM or CRAM file. (no default)
tumorBam   BamPair        --tumourBam=                1  (--tumorBam)  Tumor sample BAM or CRAM file. [required] (no default)
reference  FastaWithDict  --referenceFasta=           1  samtools-indexed reference fasta file [required]
=========  =============  =================  ==========  ====================================================================

Optional inputs
***************

=====================  ====================  ========================  ==========  ====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
name                   type                  prefix                      position  documentation
=====================  ====================  ========================  ==========  ====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
rundir                 Optional<Filename>    --runDir=                          1  Name of directory to be created where all workflow scripts and output will be written. Each analysis requires a separate directory. (default: StrelkaSomaticWorkflow)
region                 Optional<bed>         --region=                          1  Limit the analysis to one or more genome region(s) for debugging purposes. If this argument is provided multiple times the union of all specified regions will be analyzed. All regions must be non-overlapping to get a meaningful result. Examples: '--region chr20' (whole chromosome), '--region chr2:100-2000 --region chr3:2500-3000' (two regions)'. If this option is specified (one or more times) together with the 'callRegions' BED file,then all region arguments will be intersected with the callRegions BED track.
config                 Optional<File>        --config=                          1  provide a configuration file to override defaults in global config file (/opt/strelka/bin/configureStrelkaSomaticWorkflow.py.ini)
outputcallableregions  Optional<bed>         --outputCallableRegions            1  Output a bed file describing somatic callable regions of the genome
indelCandidates        Optional<vcf-gz-tbi>  --indelCandidates=                 1  Specify a VCF of candidate indel alleles. These alleles are always evaluated but only reported in the output when they are inferred to exist in the sample. The VCF must be tabix indexed. All indel alleles must be left-shifted/normalized, any unnormalized alleles will be ignored. This option may be specified more than once, multiple input VCFs will be merged. (default: None)
forcedgt               Optional<File>        --forcedGT=                        1  Specify a VCF of candidate alleles. These alleles are always evaluated and reported even if they are unlikely to exist in the sample. The VCF must be tabix indexed. All indel alleles must be left- shifted/normalized, any unnormalized allele will trigger a runtime error. This option may be specified more than once, multiple input VCFs will be merged. Note that for any SNVs provided in the VCF, the SNV site will be reported (and for gVCF, excluded from block compression), but the specific SNV alleles are ignored. (default: None)
targeted               Optional<Boolean>     --targeted                         1  (--exome)  Set options for exome or other targeted input: note in particular that this flag turns off high-depth filters
callRegions            Optional<BedTABIX>    --callRegions=                     1  Optionally provide a bgzip-compressed/tabix-indexed BED file containing the set of regions to call. No VCF output will be provided outside of these regions. The full genome will still be used to estimate statistics from the input (such as expected depth per chromosome). Only one BED file may be specified. (default: call the entire genome)
noisevcf               Optional<File>        --noiseVcf=                        1  Noise vcf file (submit argument multiple times for more than one file)
scansizemb             Optional<Integer>     --scanSizeMb=                      1  Maximum sequence region size (in megabases) scanned by each task during genome variant calling. (default: 12)
callmemmb              Optional<Integer>     --callMemMb=                       1  Set variant calling task memory limit (in megabytes). It is not recommended to change the default in most cases, but this might be required for a sample of unusual depth.
retaintempfiles        Optional<Boolean>     --retainTempFiles                  1  Keep all temporary files (for workflow debugging)
disableevs             Optional<Boolean>     --disableEVS                       1  Disable empirical variant scoring (EVS).
reportevsfeatures      Optional<Boolean>     --reportEVSFeatures                1  Report all empirical variant scoring features in VCF output.
snvscoringmodelfile    Optional<File>        --snvScoringModelFile=             1  Provide a custom empirical scoring model file for SNVs (default: /opt/strelka/share/config/somaticSNVScoringM odels.json)
indelscoringmodelfile  Optional<File>        --indelScoringModelFile=           1  Provide a custom empirical scoring model file for indels (default: /opt/strelka/share/config/somaticInde lScoringModels.json)
mode                   Optional<String>      --mode                             3  (-m MODE)  select run mode (local|sge)
queue                  Optional<String>      --queue                            3  (-q QUEUE) specify scheduler queue name
memGb                  Optional<String>      --memGb                            3  (-g MEMGB) gigabytes of memory available to run workflow -- only meaningful in local mode, must be an integer (default: Estimate the total memory for this node for local mode, 'unlimited' for sge mode)
quiet                  Optional<Boolean>     --quiet                            3  Don't write any log output to stderr (but still write to workspace/pyflow.data/logs/pyflow_log.txt)
=====================  ====================  ========================  ==========  ====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================


Metadata
********

Author: **Unknown**


*Strelka (Somatic) was last updated on 2019-05-27*.
*This page was automatically generated on 2019-08-12*.