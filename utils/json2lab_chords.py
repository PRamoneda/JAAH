import argparse
from pychord_tools.common_utils import json_to_lab

def get_args():
    parser = argparse.ArgumentParser(
        description='convert input .json file to MIREX .lab file with chord segments')
    parser.add_argument(
        '-c', '--choose', type=str, default='chords', help='choose information to extract (options: chords/keys)', action='store', choices=['chords', 'keys'])
    parser.add_argument(
        '-i', '--input', type=str, help='input annotation file in .json file', required = True)
    parser.add_argument(
        '-o', '--output', type=str, default='output.lab', help='output file in .lab file (default output.lab)', required = True)
    args = parser.parse_args()
    choice = args.choose
    infile = args.input
    outfile = args.output 
    
    return choice, infile, outfile


choice, infile, outfile = get_args()
    
    
json_to_lab(choice, infile, outfile)
