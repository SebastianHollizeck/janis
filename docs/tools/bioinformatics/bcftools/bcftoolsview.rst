:orphan:

BCFTools: View
=============================

0 contributors · 2 versions

:ID: ``bcftoolsview``
:Python: ``janis_bioinformatics.tools.bcftools.view.versions import BcfToolsView_1_9``
:Versions: v1.9, v1.5
:Container: michaelfranklin/bcftools:1.9
:Authors: 
:Citations: Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R, and 1000 Genome Project Data Processing Subgroup, The Sequence alignment/map (SAM) format and SAMtools, Bioinformatics (2009) 25(16) 2078-9
:DOI: http://www.ncbi.nlm.nih.gov/pubmed/19505943
:Created: None
:Updated: 2019-01-24
:Required inputs:
   - ``file: CompressedVCF``
:Outputs: 
   - ``out: stdout<CompressedVCF>``

Documentation
-------------

URL: `https://samtools.github.io/bcftools/bcftools.html#view <https://samtools.github.io/bcftools/bcftools.html#view>`_

________________________________
 
        View, subset and filter VCF or BCF files by position and filtering expression
        Convert between VCF and BCF. Former bcftools subset.

------

Arguments
----------

=======  =============  ==========  ===================================================================================================
value    prefix           position  documentation
=======  =============  ==========  ===================================================================================================
z        --output-type           1  (-O) [<b|u|z|v>] b: compressed BCF, u: uncompressed BCF, z: compressed VCF, v: uncompressed VCF [v]
=======  =============  ==========  ===================================================================================================

Additional configuration (inputs)
---------------------------------

================  =======================  ===================  ==========  ==============================================================================================================================================================================
name              type                     prefix                 position  documentation
================  =======================  ===================  ==========  ==============================================================================================================================================================================
file              CompressedVCF                                          2
dropGenotypes     Optional<Boolean>        --drop-genotypes              1  (-G) drop individual genotype information (after subsetting if -s option set)
headerOnly        Optional<Boolean>        --header-only                 1  (-h) print the header only
noHeader          Optional<Boolean>        --no-header                   1  (-H) suppress the header in VCF output
compressionLevel  Optional<Integer>        --compression-level           1  (-l) compression level: 0 uncompressed, 1 best speed, 9 best compression [-1]
noVersion         Optional<Boolean>        --no-version                  1  do not append version and command line to the header
regions           Optional<String>         --regions                     1  (-r) restrict to comma-separated list of regions
regionsFile       Optional<File>           --regions-file                1  (-R) restrict to regions listed in a file
targets           Optional<String>         --targets                     1  (-t) similar to -r but streams rather than index-jumps. Exclude regions with '^' prefix
targetsFile       Optional<File>           --targets-file                1  (-T) similar to -R but streams rather than index-jumps. Exclude regions with '^' prefix
threads           Optional<Integer>        --threads                     1  number of extra output compression threads [0]
trimAltAlleles    Optional<Boolean>        --trim-alt-alleles            1  (-a) trim alternate alleles not seen in the subset
noUpdate          Optional<Boolean>        --no-update                   1  (-I) do not (re)calculate INFO fields for the subset (currently INFO/AC and INFO/AN)
samples           Optional<Array<String>>  --samples                     1  (-s) comma separated list of samples to include (or exclude with '^' prefix)
samplesFile       Optional<File>           --samples-file                1  (-S) file of samples to include (or exclude with '^' prefix)
forceSamples      Optional<Boolean>        --force-samples               1  only warn about unknown subset samples
minAc             Optional<Integer>        --min-ac                      1  (-c) minimum count for non-reference (nref), 1st alternate (alt1), least frequent (minor), most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]
maxAc             Optional<Integer>        --max-ac                      1  (-C) maximum count for non-reference (nref), 1st alternate (alt1), least frequent (minor), most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]
applyFilters      Optional<Array<String>>  --apply-filters               1  (-f) require at least one of the listed FILTER strings (e.g. 'PASS,.'')
genotype          Optional<String>         --genotype                    1  (-g) [<hom|het|miss>] require one or more hom/het/missing genotype or, if prefixed with '^', exclude sites with hom/het/missing genotypes
include           Optional<String>         --include                     1  (-i) select sites for which the expression is true (see man page for details)
exclude           Optional<String>         --exclude                     1  (-e) exclude sites for which the expression is true (see man page for details)
known             Optional<Boolean>        --known                       1  (-k) select known sites only (ID is not/is '.')
novel             Optional<Boolean>        --novel                       1  (-n) select novel sites only (ID is not/is '.')
minAlleles        Optional<Integer>        --min-alleles                 1  (-m) minimum number of alleles listed in REF and ALT (e.g. -m2 -M2 for biallelic sites)
maxAlleles        Optional<Integer>        --max-alleles                 1  (-M) maximum number of alleles listed in REF and ALT (e.g. -m2 -M2 for biallelic sites)
phased            Optional<Boolean>        --phased                      1  (-p) select sites where all samples are phased
excludePhased     Optional<Boolean>        --exclude-phased              1  (-P) exclude sites where all samples are phased
minAf             Optional<Float>          --min-af                      1  (-q) minimum frequency for non-reference (nref), 1st alternate (alt1), least frequent (minor), most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]
maxAf             Optional<Float>          --max-af                      1  (-Q) maximum frequency for non-reference (nref), 1st alternate (alt1), least frequent (minor), most frequent (major) or sum of all but most frequent (nonmajor) alleles [nref]
uncalled          Optional<Boolean>        --uncalled                    1  (-u) select sites without a called genotype
excludeUncalled   Optional<Boolean>        --exclude-uncalled            1  (-U) exclude sites without a called genotype
types             Optional<Array<String>>  --types                       1  (-v) select comma-separated list of variant types: snps,indels,mnps,other [null]
excludeTypes      Optional<Array<String>>  --exclude-types               1  (-V) exclude comma-separated list of variant types: snps,indels,mnps,other [null]
private           Optional<Boolean>        --private                     1  (-x) select sites where the non-reference alleles are exclusive (private) to the subset samples
excludePrivate    Optional<Boolean>        --exclude-private             1  (-X) exclude sites where the non-reference alleles are exclusive (private) to the subset samples
================  =======================  ===================  ==========  ==============================================================================================================================================================================

