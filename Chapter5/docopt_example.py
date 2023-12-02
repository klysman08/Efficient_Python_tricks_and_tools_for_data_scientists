"""Extract keywords of an input file
Usage:
    docopt_example.py --data-dir=<data-directory> [--input-path=<path>]
Options:
    --data-dir=<path>    Directory of the data
    --input-path=<path>  Name of the input file [default: input_text.txt]
"""


from docopt import docopt 

if __name__ == '__main__':
    args = docopt(__doc__, argv=None, help=True)
    input_path = args['--input-path']

    if data_dir := args['--data-dir']:
        print(f"Extracting keywords from {data_dir}/{input_path}")