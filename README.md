[![PyPI version](https://badge.fury.io/py/modelestimator-v2.svg)](https://badge.fury.io/py/modelestimator-v2)
[![Build Status](https://travis-ci.com/arvestad/modelestimator-v2.svg?branch=master)](https://travis-ci.com/arvestad/modelestimator-v2)
# modelestimator --- Infer sequence evolution rate matrices from a MSA


## Example usage

``` shell
    modelestimator -t 0.001 file1.fa file2.fa file3.fa
```
Infer a rate matrix (written to stdout) from three alignment files in Fasta format.
The output is PAML format by default, and therefore applicable in a number of
available phylogenetic softwares.

``` shell
    modelestimator -b 200 file.fa
```
Try the experimental bootstrapping feature (200 replicates) on a Fasta multialignment.

## Syntax

```
modelestimator <options> infiles
```


`<format>` should be either FASTA, STOCKHOLM or PHYLIP format.

Output is a rate matrix and residue distribution vector.

### Options

```
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -a {iqtree,matlab,mrbayes,octave,paml,phyml}, --application {iqtree,matlab,mrbayes,octave,paml,phyml}
                        Choose output format to suit the application you want
                        to use for inference. The 'iqtree', 'paml' and 'phyml'
                        options are identical. The 'matlab' and 'octave'
                        optins are for import into MatLab-compatible programs
                        and are presenting the actual Q matrix rather than the
                        R matrix used by PAML/PhyML, etc. Default: paml
  -f {fasta,clustal,nexus,phylip,stockholm}, --format {fasta,clustal,nexus,phylip,stockholm}
                        Specify sequence format of input files. Default: fasta
  -t T, --threshold T   Stop when consecutive iterations do not change by more
                        than T. Default: 0.001
  -b N, --bootstrap N   Estimate the rate matrix using bootstrapping by
                        computing N resampled replicates of the input
                        multialignment. For each replicate, a rate matrix is
                        computed. The mean matrix the elementwise standard
                        deviation is returned. Only one infile should be given
                        in this mode.
  -B N, --bootstrapped_quality N
                        Estimate the quality of the rate matrix estimate using
                        a bootstrap procedure. The multialignment is resampled
                        N times and a Q matrix is computed for each replicate.
                        Then the difference (matrix norm) between rate matrix
                        estimated without resampling and each bootstrapped Q
                        is computed and the mean difference is returned. Only
                        one infile should be given in this mode. Returns
                        bootstrap norm.
```
