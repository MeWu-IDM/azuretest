import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-o','--outfolder', help='output folder', required=True)
parser.add_argument('-n','--filename', help='input folder')
args = parser.parse_args()

if not os.path.isdir(args.outfolder):
    os.mkdir(args.outfolder)
with open(os.path.join(args.outfolder, args.filename), "w") as f:
    f.write("This is a test")
    f.close()