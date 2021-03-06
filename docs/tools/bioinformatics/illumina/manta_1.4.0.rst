:orphan:

Manta
=============

1 contributor · 2 versions

:ID: ``manta``
:Python: ``janis_bioinformatics.tools.illumina.manta.manta import Manta_1_4_0``
:Versions: 1.5.0, 1.4.0
:Container: michaelfranklin/manta:1.4.0
:Authors: Michael Franklin
:Citations: Chen, X. et al. (2016) Manta: rapid detection of structural variants and indels for germline and cancer sequencing applications. Bioinformatics, 32, 1220-1222. doi:10.1093/bioinformatics/btv710
:DOI:  doi:10.1093/bioinformatics/btv710
:Created: 2019-02-12
:Updated: 2019-02-19
:Required inputs:
   - ``bam: BamPair``

   - ``reference: FastaWithDict``
:Outputs: 
   - ``python: File``

   - ``pickle: File``

   - ``candidateSV: CompressedIndexedVCF``

   - ``candidateSmallIndels: CompressedIndexedVCF``

   - ``diploidSV: CompressedIndexedVCF``

   - ``alignmentStatsSummary: File``

   - ``svCandidateGenerationStats: tsv``

   - ``svLocusGraphStats: tsv``

Documentation
-------------

URL: `https://github.com/Illumina/manta <https://github.com/Illumina/manta>`_

Manta calls structural variants (SVs) and indels from mapped paired-end sequencing reads. 
It is optimized for analysis of germline variation in small sets of individuals and somatic 
variation in tumor/normal sample pairs. Manta discovers, assembles and scores large-scale SVs, 
medium-sized indels and large insertions within a single efficient workflow. The method is 
designed for rapid analysis on standard compute hardware: NA12878 at 50x genomic coverage is 
analyzed in less than 20 minutes on a 20 core server, and most WGS tumor/normal analyses 
can be completed within 2 hours. Manta combines paired and split-read evidence during SV 
discovery and scoring to improve accuracy, but does not require split-reads or successful 
breakpoint assemblies to report a variant in cases where there is strong evidence otherwise. 

It provides scoring models for germline variants in small sets of diploid samples and somatic 
variants in matched tumor/normal sample pairs. There is experimental support for analysis of 
unmatched tumor samples as well. Manta accepts input read mappings from BAM or CRAM files and 
reports all SV and indel inferences in VCF 4.1 format. See the user guide for a full description 
of capabilities and limitations.

------

Arguments
----------

==================================================================  ========  ==========  ====================================================================================================================================
value                                                               prefix      position  documentation
==================================================================  ========  ==========  ====================================================================================================================================
configManta.py                                                                         0
<janis_core.types.selectors.StringFormatter object at 0x10d38b978>                     2
<janis_core.types.selectors.CpuSelector object at 0x10d38bda0>      -j                 3  (-j) number of jobs, must be an integer or 'unlimited' (default: Estimate total cores on this node for local mode, 128 for sge mode)
==================================================================  ========  ==========  ====================================================================================================================================

Additional configuration (inputs)
---------------------------------

==============  ==================  ================  ==========  ====================================================================================================================================================================================================================================================================================================================================================
name            type                prefix              position  documentation
==============  ==================  ================  ==========  ====================================================================================================================================================================================================================================================================================================================================================
bam             BamPair             --bam                      1  FILE Normal sample BAM or CRAM file. May be specified more than once, multiple inputs will be treated as each BAM file representing a different sample. [optional] (no default)
reference       FastaWithDict       --referenceFasta           1  samtools-indexed reference fasta file [required]
config          Optional<File>      --config                   1  provide a configuration file to override defaults in global config file (/opt/conda/share/manta-1.2.1-0/bin/configManta.py.ini)
runDir          Optional<Filename>  --runDir                   1  Run script and run output will be written to this directory [required] (default: MantaWorkflow)
tumorBam        Optional<BamPair>   --tumorBam                 1  Tumor sample BAM or CRAM file. Only up to one tumor bam file accepted. [optional=null]
exome           Optional<Boolean>   --exome                    1  Set options for WES input: turn off depth filters
rna             Optional<BAM>       --rna                      1  Set options for RNA-Seq input. Must specify exactly one bam input file
unstrandedRNA   Optional<File>      --unstrandedRNA            1  Set if RNA-Seq input is unstranded: Allows splice-junctions on either strand
outputContig    Optional<File>      --outputContig             1  Output assembled contig sequences in VCF file
callRegions     Optional<BedTABIX>  --callRegions              1  Optionally provide a bgzip-compressed/tabix-indexed BED file containing the set of regions to call. No VCF output will be provided outside of these regions. The full genome will still be used to estimate statistics from the input (such as expected depth per chromosome). Only one BED file may be specified. (default: call the entire genome)
mode            Optional<String>    --mode                     3  (-m) select run mode (local|sge)
quiet           Optional<Boolean>   --quiet                    3  Don't write any log output to stderr (but still write to workspace/pyflow.data/logs/pyflow_log.txt)
queue           Optional<String>    --queue                    3  (-q) specify scheduler queue name
memgb           Optional<Integer>   --memGb                    3  (-g) gigabytes of memory available to run workflow -- only meaningful in local mode, must be an integer (default: Estimate the total memory for this node for local  mode, 'unlimited' for sge mode)
maxTaskRuntime  Optional<String>    --maxTaskRuntime           3  (format: hh:mm:ss) Specify scheduler max runtime per task, argument is provided to the 'h_rt' resource limit if using SGE (no default)
==============  ==================  ================  ==========  ====================================================================================================================================================================================================================================================================================================================================================

