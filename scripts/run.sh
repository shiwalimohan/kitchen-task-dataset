#!/bin/bash

dataDirectory=$1
dataString=$2
verbNetXML=$3

csvFileName='collatedData.csv'
csvVerbFileName='verb-classes.csv'
verbFileName='verbs.org'
verbClassesFileName='verbs-classes.org'
verbDataKeyFileName='data-key-file.txt'
verbClassesKeyFileName='classes-key-file.txt'

googleDataDirectory=`echo $dataDirectory| cut -d'/' -f 2`
googleVerbClasses='verb-classes'
googleVerbData='collatedData'


dataCSVFile=$1"csv/"$csvFileName
verbCSVFile=$1"csv/"$csvVerbFileName
verbOrgFile=$1"org/"$verbFileName
verbClassesOrgFile=$1"org/"$verbClassesFileName
orgDataDirectory=$1"org/"
verbDataKeyFile=$1$verbDataKeyFileName
verbClassesKeyFile=$1$verbClassesKeyFileName


echo "COLLECTING DATA ..."
echo ./generateCSV.py -o $dataCSVFile -v $verbOrgFile -i $orgDataDirectory -s $dataString
./generateCSV.py -o $dataCSVFile -v $verbOrgFile -i $orgDataDirectory -s $dataString
echo "COMPLETED COLLECTION"

echo "EXTRACTING VERB CLASSES ..."
echo ./extractVerbNetClasses.py -i $verbOrgFile -o $verbClassesOrgFile -c $verbCSVFile -x $verbNetXML
./extractVerbNetClasses.py -i $verbOrgFile -o $verbClassesOrgFile -c $verbCSVFile -x $verbNetXML
echo "COMPLETED EXTRACTION"

echo "UPLOADING FILES"
echo ./uploadGoogleSpreadSheet.py -s $googleVerbClasses -f $verbCSVFile -k $verbClassesKeyFile
./uploadGoogleSpreadSheet.py -s $googleVerbClasses -f $verbCSVFile -k $verbClassesKeyFile
echo ./uploadGoogleSpreadSheet.py -s $googleVerbData -f $dataCSVFile  -k $verbDataKeyFile
./uploadGoogleSpreadSheet.py -s $googleVerbData -f $dataCSVFile -k $verbDataKeyFile