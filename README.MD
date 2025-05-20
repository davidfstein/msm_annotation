A python package for annotating variants from a VCF file using Ensembl's VEP.

### Requirements
 - python>=3.11
 - python-dotenv
 - singularity

This package assumes a local copy of the VEP cache. It may be possible to run with a connection
to the Ensembl database, but this has not been tested and is not recommended. See https://useast.ensembl.org/info/docs/tools/vep/script/vep_download.html
for details on cache installation. Plugin scripts must also be installed, and may be retrieved along 
with the cache (see the link). Ensure that the plugin scripts and plugin data
are installed under the VEP cache directory so that they are exposed in the
singularity container.

The package defaults to VEP version 112. It should be possible to drop in different versions, however
the cache and plugins will need to be updated. 
 
### Installation
```
pip install .
```

### Setup
```
ml singularity/3.6.4
ml proxies
cp example.env .env
```
After copying the example.env file, update the values for your system.
```VEP_DATA``` should point to the location of the VEP cache. ```VEP_CACHEDIR``` is relative to the container and does not need to be changed. The remaining
variables may be updated according to your directory structure, but ensure that
the plugin directory and plugin data are children of the cache directory.

### Usage
```
annotate_msm -h
annotate_msm -i test.vcf -o test_output.tsv
```

```DEFAULT_VEP_OPTIONS``` constructs the VEP command that is run. This may be replaced or edited for different VEP behavior.
