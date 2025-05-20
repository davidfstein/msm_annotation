import os

'''
Add plugins and adjust plugin options.
'''
PLUGINS = [
    f'AlphaMissense,file={os.environ.get('ALPHAMISSENSE_DATA')},transcript_match=1',
    'Blosum62',
    f'CADD,snv={os.environ.get('CADD_SNV_DATA')},indels={os.environ.get('CADD_INDEL')}',
    'Carol',
    'Conservation',
    f'dbNSFP,{os.environ.get('DBNSFP_DATA')},transcript_match=1,ALL',
    f'dbscSNV,{os.environ.get('DBSCSNV_DATA')}',
    f'DisGeNET,file={os.environ.get('DISGENET_DATA')},disease=1',
    f'DosageSensitivity,file={os.environ.get('DOSAGESENSITIVITY_DATA')}',
    f'Enformer,file={os.environ.get('ENFORMER_DATA')}',
    f'IntAct,mutation_file={os.environ.get('INTACT_MUTATION_DATA')},mapping_file={os.environ.get('INTACT_MAPPING_DATA')}',
    f'LoFtool,{os.environ.get('LOFTOOL_DATA')}',
    f'MaveDB,file={os.environ.get('MAVEDB_DATA')},transcript_match=1',
    f'MaxEntScan,{os.environ.get('MAXENTSCAN_DATA')}',
    f'mutfunc,db={os.environ.get('MUTFUNC_DATA')}',
    'NearestExonJB',
    'NMD',
    f'OpenTargets,file={os.environ.get('OPENTARGETS_DATA')}',
    f'PhenotypeOrthologous,file={os.environ.get('PHENOTYPESORTHOLOGOUS_DATA')}',
    f'PrimateAI,{os.environ.get('PRIMATEAI_DATA')}',
    f'ReferenceQuality,{os.environ.get('REFERENCEQUALITY_DATA')}',
    f'REVEL,file={os.environ.get('REVEL_DATA')}',
    f'RiboseqORFs,file={os.environ.get('RIBOSEQSORFS_DATA')}',
    f'satMutMPRA,file={os.environ.get('SATMUTMPRA_DATA')}',
    f'SpliceAI,snv={os.environ.get('SPLICEAI_SNV_DATA')},indel={os.environ.get('SPLICEAI_INDEL_DATA')}',
    'TSSDistance',
    f'UTRAnnotator,file={os.environ.get('UTRANNOTATOR_SNV_DATA')}',
    f'LoF,loftee_path:{os.environ.get('VEP_PLUGDIR')},conservation_file:{os.environ.get('VEP_PLUGDIR')}/phylocsf_gerp.sql,human_ancestor_fa:{os.environ.get('VEP_PLUGDIR')}/human_ancestor.fa.gz',
]

'''
Add custom annotation options and adjust options.
'''
CUSTOM = [
    f'file={os.environ.get('APPARENT2_DATA')},format=vcf,short_name=Apparent2,fields=delta_usage%delta_logodds%delta_usage_narrow%delta_logodds_narrow,type=exact',
    f'file={os.environ.get('LOGOFUNC_DATA')},format=vcf,short_name=LoGoFunc,type=exact,fields=prediction%neutral%GOF%LOF',
    f'file={os.environ.get('REPEATMASKER_DATA')},format=bed,short_name=RepeatMasker,type=surrounding',
    f'file={os.environ.get('UNIPROTREPETITIVE_DATA')},format=bed,short_name=UniProtRepetitive,type=surrounding',
    f'file={os.environ.get('ZOONOMIA_241_DATA')},format=bigwig,short_name=Zoonomia241,type=exact',
    f'file={os.environ.get('ZOONOMIA_PRIMATES_DATA')},format=bigwig,short_name=ZoonomiaPrimates,type=exact',
    f'file={os.environ.get('ZOONOMIA_ROCC_DATA')},format=bed,short_name=ZoonomiaRoCCs,type=overlap',
    f'file={os.environ.get('ZOONOMIA_UCE_DATA')},format=bed,short_name=ZoonomiaUCEs,type=overlap',
]

'''
Initialize the default parameters and arguments for VEP. Parameters that do not 
accept arguments may be initialized with None. Parameters such as buffer_size and
fork may be tuned for performance as necessary. 
'''
DEFAULT_VEP_OPTIONS = lambda in_path, out_path: {
    '-i': '/input/' + in_path,
    '-o': '/vep_output/' + out_path,
    '--dir_cache': os.environ.get('VEP_CACHEDIR'),
    '--dir_plugins': os.environ.get('VEP_PLUGDIR'),
    '--tab': None,
    '--assembly': 'GRCh38',
    '--pick_allele_gene': None,
    '--no_stats': None,
    '--domains': None,
    '--uniprot': None,
    '--symbol': None,
    '--numbers': None,
    '--canonical': None,
    '--protein': None,
    '--regulatory': None,
    '--af_gnomade': None,
    '--af_gnomadg': None,
    '--show_ref_allele': None,
    '--force_overwrite': None,
    '--cache': None,
    '--total_length': None,
    '--offline': None,
    '--fasta': os.environ.get('VEP_REF_FASTA'),
    '--buffer_size': 100000,
    '--fork': 8,
    '--plugin': PLUGINS,
    '--custom': CUSTOM,       
}