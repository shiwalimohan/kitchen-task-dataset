#!/usr/bin/python
### install inspector for verbnet and include it in the classpath
### extractVerbNetClasses.py -i [list-of-verbs-file] -o [output-org-file-name] -c [output-csv-file-name] -x [verbnet xml directory]


import sys, getopt, subprocess, re

def main(argv):

    #### extract file name from commandline arguments
    inputFile = ''
    outputFile = ''
    csvFile = ''
    xmlDir = ''

    try:
        opts, args = getopt.getopt(argv,"i:o:c:x:",["ifile=","orgfile=","xml=","csvfile="])
    except getopt.GetoptError:
        print 'extractVerbNetClasses.py -i <file-with-verb-list> -o <outputorgfile> -c <outputcsvfile> -x <verbnet-xml-directory>'
        sys.exit(2)


    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-c", "--csvfile"):
            csvFile = arg
        elif opt in ("-x", "--xml"):
            xmlDir = arg


    print "######"
    print "Input file: ", inputFile
    print "Output file: ", outputFile
    print "Output CSV file: ", csvFile
    print "xml directory: ", xmlDir
    print "######"

    ### open files
    iHandle = open(inputFile, 'r')
    oHandle = open(outputFile, 'w')
    cHandle = open(csvFile, 'w')


    ### for every verb in the input file extract classes from the verbnet
    for line in iHandle:
        verb = line.rstrip('\n')
        command = "java vn.Inspector "+ xmlDir + " -irhn -Vcm | grep -B1 \'MEMBER: " + verb +"$\'"
        print command
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for term in p.stdout.readlines():
            if re.search('CLASS', term):
                print "| " + verb + " | " + term.rstrip().split()[-1] + " | 1 |";
                oHandle.write("| " + verb + " | " + term.rstrip().split()[-1] + " | 1 |\n")
                cHandle.write(verb + "," + term.rstrip().split()[-1] + ",1\n")
                
    iHandle.close()
    oHandle.close()
    cHandle.close()

if __name__ == "__main__":
   main(sys.argv[1:])
