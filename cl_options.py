from __future__ import division

from optparse import OptionParser

usage_str = """usage: %prog [options] 

[] indicates optional input (order unimportant)
{} indicates required input (order unimportant)

Example usage:
"""



def parse_command_line_parameters(add_options_func, required_options=[]):
    """ Parses command line arguments """
    usage = usage_str
    #version = 'Version: %prog ' + __version__
    parser = OptionParser(usage=usage)
    #, version=version)
    
    # A binary 'verbose' flag
    parser.add_option('-v','--verbose',action='store_true',
        dest='verbose',help='Print information during execution -- '+\
        'useful for debugging [default: %default]')
    
    add_options_func(parser)
    
    # Set default values here if they should be other than None
    parser.set_defaults(verbose=False)
    
    opts,args = parser.parse_args()
    
    for option in required_options:
        if eval('opts.%s' % option) == None:
            parser.error('Required option --%s omitted.' % option)
    
    
    return opts,args


if __name__ == "__main__":
    opts,args = parse_command_line_parameters()
    verbose = opts.verbose
