#! /usr/local/bin/perl -w

use strict;
use warnings;

# Tableau des transitions q1→q2
my @transitions;

# Création de l'automate initial
for ( my $q1=0 ; $q1<7 ; $q1++ ) {
    for ( my $i=0 ; $i<10 ; $i++ ) {
	my $q2 = (3*$q1+$i)%7;
	push @{$transitions[$q1][$q2]}, $i;
    }
}

# Transformation des transitions en regexps
for ( my $q1=0 ; $q1<7 ; $q1++ ) {
    for ( my $q2=0 ; $q2<7 ; $q2++ ) {
	my $s = join("",@{$transitions[$q1][$q2]});
	$s = "[$s]" if length($s)>1;
	$transitions[$q1][$q2] = $s;
    }
}

# Élimination des états
for ( my $qelim=6 ; $qelim>=0 ; $qelim-- ) {
    for ( my $q1=0 ; $q1<$qelim ; $q1++ ) {
	for ( my $q2=0 ; $q2<$qelim ; $q2++ ) {
	    my $r12 = $transitions[$q1][$q2];
	    my $r1 = $transitions[$q1][$qelim];
	    my $s = $transitions[$qelim][$qelim];
	    my $r2 = $transitions[$qelim][$q2];
	    $transitions[$q1][$q2] = "(${r12}|${r1}${s}\*${r2})";
	}
    }
}

# Impression de la regexp finale
print "\^" . $transitions[0][0] . "\*\$\n";
