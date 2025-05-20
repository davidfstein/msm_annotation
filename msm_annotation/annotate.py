from dotenv import load_dotenv
load_dotenv()
import os
import argparse
from .utils.sh_utils import vep, default_vep_options

def parse_args():
    parser = argparse.ArgumentParser(
        description="Annotate a VCF file using Ensembl's VEP"
    )

    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help="Path to the VCF file to annotate"
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help="Desired location of the output file"
    )

    parser.add_argument(
        '--vep_container',
        type=str,
        required=False,
        default='ensemblorg/ensembl-vep:release_112.0',
        help="(optional) Name of a VEP container to be pulled from docker hub. Default: ensemblorg/ensembl-vep:release_112.0"
    )

    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help="Suppress VEP command information"
    )
    return parser.parse_args()


def run_vep(input_path, output_path, vep_container, quiet):
    vep_command = vep.generate_vep_command(**default_vep_options.DEFAULT_VEP_OPTIONS(input_path, output_path))
    if not quiet:
        print(vep_command)
    vep.vep(vep_command, os.path.abspath(os.path.dirname(input_path)), vep_container)

def main():
    args = parse_args()
    run_vep(args.input, args.output, args.vep_container, args.quiet)

if __name__ == '__main__':
    main()