from __future__ import division
import numpy 
import os, sys
import cl_options
from itertools import tee, izip
import time
import doctest

def round_up(sequence):
    ''' used for window length calculation - always want more than window length of at least 10%! 
    >>> dna = 'AGCTA'
    >>> round_up(dna)
    1.0
    >>> round_up(dna*9)
    5.0
    '''
    return round((len(sequence)*0.1)+0.5)

def window(iterable, size):
    # used to get windows across sequence 
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters) 

def get_window(nthwindow, window_len, qscore): 
    ''' return qc score for nth window 
    >>> testscore = numpy.arange(100)
    >>> get_window(4, 10, testscore)
    array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
    >>> get_window(400, 10, testscore)
    array([], dtype=int64)
    '''
    return qscore[(nthwindow-1):(nthwindow-1)+window_len]

def calculate_window_average(qscore, window_len):
    '''calculate the average quality score for all windows 
    >>> testscore = numpy.arange(100)
    >>> calculate_window_average(testscore, 90)
    [44.5, 45.5, 46.5, 47.5, 48.5, 49.5, 50.5, 51.5, 52.5, 53.5, 54.5]
    '''
    qc_average = []
    for window_qscore in window(qscore, window_len):
        qc_average.extend([sum(window_qscore)/window_len])  
    return qc_average 
           
def make_cuts(read_sequence_dict,quality_char_dict, quality_scale_dict, quality_threshold=20, length_threshold=20, do_5prime=True):
    # make 3' (and 5' if indicated) cuts
    newseq_dict ={}
    for seqname in seq_dict.iterkeys():
        print 'cuting reads from', seqname
        qscore = quality_scale_dict[seqname]
        qcall = quality_char_dict[seqname]
        sequence = read_sequence_dict[seqname]
        #determine window length
        window_len = round_up(sequence)
        #determine average quality score for each window
        seq_averge_score = calculate_window_average(qscore, window_len)
        if do_5prime:
            # perform the 5' cut
            nwindow_cut5 = numpy.arange(len(numpy.array(seq_averge_score)))[numpy.array(seq_averge_score)>self.quality_threshold][0]
            window_cut5 = get_window(nwindow_cut5, window_len, qcscore)     
            cut5base = numpy.arange(window_len)[window_cut5>self.quality_threshold][0] + nwindow_cut5
        # perform the 3' cut 
        seq_averge_score3 = seq_averge_score[::-1]
        nwindow_cut3 = len(seq_average_score3) - numpy.arange(len(numpy.array(seq_averge_score3)))[numpy.array(seq_averge_score3)>self.quality_threshold][0]
        window_cut3 = get_window(nwindow_cut3, window_len, qcscore)     
        cut3base = numpy.arange(window_len)[window_cut5<self.quality_threshold][0] + nwindow_cut3
        if len(sequence[cut5base:cut3base])>length_threshold:
            newseq_dict[seqname] = [sequence[cut5base:cut3base], qcall[cut5base:cut3base], qscore[cut5base:cut3base]]
    return newseq_dict
                
def write_reads_file(outfilename, directory, sequence_dict):
    filename = os.path.join(directory, outfilename)        
    f = open(filename, 'wb')
    for k, seqname in enumerate(sequence_dict.iterkeys()):
        shortenedqcall = sequence_dict[seqname][1]
        shortenedsequence = sequence_dict[seqname][0]
        f.write(str(seqname) + '\n')
        f.write(shortenedsequence + '\n')
        f.write('+\n')
        f.write(shortenedqcall + '\n')                   
    f.close()

if __name__ == '__main__':
    doctest.testmod()
