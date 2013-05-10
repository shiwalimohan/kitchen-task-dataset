#!/usr/bin/python

import sys, getopt
import gdata.docs.service

def main(argv):
    
    ### extract username, password, filestring
    username = ''
    password = ''
    fileString= ''
    googleSpreadSheet= ''

    try:
        opts, args = getopt.getopt(argv, "u:p:f:g:", ["username=","password=","filestring=","spreadsheet="])
    except getopt.GetoptError as err:
        print 'uploadGoogleSpreadSheet.py -u <username> -p <password>'
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-f", "--filestring"):
            filestring = arg
        elif opt in ("-g", "--spreadsheet"):
            googleSpreadSheet = arg
    

    client = gdata.docs.service.DocsService()
    client.ClientLogin(username,password)


    documents_feed = client.GetDocumentListFeed()
    for document_entry in documents_feed.entry:
        print document_entry.title.text

if __name__ == "__main__":
   main(sys.argv[1:])
