from rubik import Rubik
from tetra_cell import TetraCell
from octa_cell import OctaCell
from explore import explore

def create_pyraminx
    pyraminx = Rubik(TetraCell.factory, OctaCell.factory)
    #TODO: populate faces
    return pyraminx

def main():
    pyraminx = create_pyraminx()
    navigate(pyraminx)

if __name__ == '__main__':
    main()
