#!/usr/bin/python

import sys, getopt
import gdata.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util

class SampleConfig(object):
  APP_NAME = 'GDataDocumentsListAPISample-v1.0'
  DEBUG = False

def CreateClient():
    client = gdata.docs.client.DocsClient()
    client.http_client.debug = SampleConfig.DEBUG
    
    #authenticate the user with login
    try:
        gdata.sample_util.authorize_client(
            client,
            service=client.auth_service,
            source=client.source,
            scopes=client.auth_scopes
            )
    except gdata.client.BadAuthentication:
        exit('Invalid user credentials given.')
    except gdata.client.Error:
        exit('Login Error')
    return client

def CreateNewSpreadSheet(googleSpreadSheet,file,keyfile):
    client = CreateClient()
    kHandle = open(keyfile, 'r')

    document = client.GetResourceById(kHandle.readline().strip())
    print "Uploading file at: %s" % file

    media = gdata.data.MediaSource()
    media.SetFileHandle(file, 'text/csv')
    
    document = client.UpdateResource(document, media=media)
    print 'Created and uploaded:', document.title.text, document.resource_id.text
    kHandle.close

def main(argv):
    
    file= ''
    googleSpreadSheet= ''
    directory=''
    keyfile=''

    try:
        opts, args = getopt.getopt(argv, "f:s:k:", ["file=","spreadsheet=","keyfile="])
    except getopt.GetoptError:
        exit('uploadGoogleSpreadSheet.py -f <csvfile> -s <google-spread-sheet> -k <file-with-spreadsheet-key')
        
    for opt, arg in opts:
        if opt in ("-f", "--filestring"):
            file = arg
        elif opt in ("-s", "--spreadsheet"):
            googleSpreadSheet = arg
        elif opt in ("-k", "--keyfile"):
            keyfile = arg
    CreateNewSpreadSheet(googleSpreadSheet,file,keyfile)

if __name__ == "__main__":
   main(sys.argv[1:])
