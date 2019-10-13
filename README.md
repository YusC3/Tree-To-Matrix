# Tree-To-Matrix:
## Info:
#### Code I made for Computational Biology at UW Bothell
#### This is a code meant to be used to obtain pairwise distance from all species in the tree. The code will return a Nxn Matrix output file, which can be uploaded to a code to run a certian test, and a file titled 'Distance Matrix', which contains a taxon labeled matrix (so the viewer can understand the data visually).

## Usage:
### Command Line Options:
- -p: path to tree file (ex: path/to/tree.nwk)
- -t: type, or tree format (ex NEWICK or nwk trees files should be typed in as "newick")
- -q: output file, a csv matrix (either 'y' for yes or 'n' no to ouput a file)

## Python Libraries:
#### ArgumentParser, Tree, dendropy, Pandas, Numpy
