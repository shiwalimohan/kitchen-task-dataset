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

def GetDirectory(directory, client):
    q = gdata.docs.client.DocsQuery(title=directory, title_exact='true', show_collections='true')
    folder = client.GetResources(q=q).entry[0]
    return folder

def CreateNewSpreadSheet(directory,googleSpreadSheet,file):
    client = CreateClient()
    folder = GetDirectory(directory, client)
    print "In folder: %s" % folder.title.text

    document = gdata.docs.data.Resource(type='spreadsheet', title=googleSpreadSheet)
    print "Uploading file at: %s" % file

    media = gdata.data.MediaSource()
    media.SetFileHandle(file, 'text/csv')
    
    document = client.CreateResource(document, media=media, collection=folder)
    print 'Created and uploaded:', document.title.text, document.resource_id.text

def main(argv):
    
    file= ''
    googleSpreadSheet= ''
    directory=''

    try:
        opts, args = getopt.getopt(argv, "f:d:s:", ["file=","directory=","spreadsheet="])
    except getopt.GetoptError:
        exit('uploadGoogleSpreadSheet.py -f <csvfile> -d <google-directory> -s <google-spread-sheet>')
        
    for opt, arg in opts:
        if opt in ("-f", "--filestring"):
            file = arg
        elif opt in ("-s", "--spreadsheet"):
            googleSpreadSheet = arg
        elif opt in ("-d", "--directory"):
            directory = arg

    CreateNewSpreadSheet(directory,googleSpreadSheet,file)



if __name__ == "__main__":
   main(sys.argv[1:])
