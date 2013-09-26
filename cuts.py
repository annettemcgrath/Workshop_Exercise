from __future__ import division
import numpy 
import os, sys
import cl_options
from itertools import tee, izip
import time
from Cuts_tools import make_cuts,write_reads_file
from quality_scaling import quality_scaling
                    
def run(directory, inputfilename, outputfilename, remove_seqs_withN, quality_threshold, length_threshold, do_5prime):
    read_name,read_sequence_dict,quality_char_dict, quality_scale_dict, numberofreads = quality_scaling(filename, directory, remove_seqs_withN)
    newseq_dict = make_cuts(read_sequence_dict,quality_char_dict, quality_scale_dict, quality_threshold, length_threshold, do_5prime)
    write_reads_file(outfilename, directory, newseq_dict)

def config_options(parser):
    """sets up the command line options"""
    
    parser.add_option('-i', '--input_dir', default='.',
        help="path to directory to read alignments  [default: %default]")
    
    parser.add_option('-f', '--input_file', default='test.fastq',
        help="fastq file to read reads from[default: %default]")

    parser.add_option('-o', '--output_file', default='test.out.fastq',
        help="output file for shortened reads[default: %default]")

    parser.add_option('-n', '--remove_n', action='store_true', default=False,
        help="remove any reads with any 'N' present [default: %default]")

    parser.add_option('-p', '--do_5primecut', action='store_false', default=True,
        help="perform the 5' cut [default: %default]")

    parser.add_option('-l', '--length_threshold', default=20,
        help="Set the length threshold [default: %default]")

    parser.add_option('-q', '--quality_threshold', default=20, 
        help="set teh quality threshold [default: %default]")

if __name__ == '__main__':
    start = time.clock()
    opts, args = cl_options.parse_command_line_parameters(config_options)
    run(opts.input_dir, opts.input_file, opts.output_file, opts.remove_n, opts.quality_threshold, opts.length_threshold, opts.do_5primecut)
    end = time.clock()
    print "Time elapsed = ", end - start, "seconds"
