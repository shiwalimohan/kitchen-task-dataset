#!/usr/bin/python
### converts a group of org-mode table files to a single file in csv format

import sys, getopt, subprocess, re, glob

class config(object):
    VERB_COLUMN = 1

def collateFilesAsCSV(ifiles, ofile, vfile):
    oHandle = open(ofile, 'w')
    vHandle = open(vfile, 'w')
    
    verbList = []

    for file in ifiles:
        handle = open(file, 'r')
        for line in handle:
            string1 = line.strip('\n')
            if string1:
                string = string1.strip('|')
                words = string.split('|')
                for word in words:
                    wordStr = word.strip()
                    oHandle.write(wordStr + ",")
                oHandle.write("\n")
                verbList.append(words[config.VERB_COLUMN].strip() + "\n")
        print "added file: %s" % file
        handle.close()

    # write unique verbs to the file
    for line in set(verbList):
        vHandle.write("%s" % line)
    
    oHandle.close()
    vHandle.close()

def main(argv):
    idir= ''
    ofile=''
    vfile=''
    string = ''

    try:
        opts, args = getopt.getopt(argv, "i:o:v:s:", ["idirectory=","ofile=","vfile=","string="])
    except getopt.GetoptError:
        exit('generateCSV.py -i <input-files> -o <input-directory> -v <output-verb-file> -s <match-string>')
        
    for opt, arg in opts:
        if opt in ("-o", "--ofile"):
            ofile = arg
        elif opt in ("-v", "--vfile"):
            vfile = arg
        elif opt in ("-i", "--ifiles"):
            idir = arg
        elif opt in ("-s", "--string"):
            string = arg
            
    ifiles = glob.glob(idir + string)

    print "###############"
    print "Input files: ", ifiles
    print "Output file: ", ofile
    print "Output verb file: ", vfile
    print "###############"

    collateFilesAsCSV(ifiles, ofile, vfile)

if __name__ == "__main__":
   main(sys.argv[1:])
