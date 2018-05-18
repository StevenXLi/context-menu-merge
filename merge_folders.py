import sys
import glob
import os

merged_folder_name = sys.argv[1] + "-merged"
allfiles = []

for arg in sys.argv[1:]:
    allfiles += glob.glob(arg+"/*")

if not os.path.exists(merged_folder_name):
    os.makedirs(merged_folder_name)
    for afile in allfiles:
        os.rename(afile, merged_folder_name + afile[afile.rfind("\\"):])