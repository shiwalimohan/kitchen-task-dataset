#!/usr/bin/perl

### extractVerbNetClasses [list-of-verbs-file] [output-file-name] [verbnet xml directory]

$inputFile=$ARGV[0];
$outputFile=$ARGV[1];
$xmlDir=$ARGV[2];

print "######\ninput file: ".$inputFile. "\noutput file: ".$outputFile."\nxml directory: ".$xmlDir."\n########\n";

open IFILE, "<", $inputFile or die $!;
open OFILE, ">", $outputFile or die $!;

my @verbs = <IFILE>;

foreach(@verbs){
    chomp($_);
    $verb=$_;
    $command = "java vn.Inspector ".$xmlDir." -irhn -Vcm | grep -B1 \'MEMBER: ".$_."\$\'";
    print $command."\n";
    @op = `$command`;
    @classes = grep {/CLASS/} @op;

    foreach(@classes){
	chomp($_);
	$_ =~ s/.*[^\w._-](\w)/$1/;
	print "| ".$verb. " | ".$_." | 1 | \n";
	print OFILE "| ".$verb. " | ".$_." | 1 | \n";
    }

}

close IFILE;
close OFILE;
