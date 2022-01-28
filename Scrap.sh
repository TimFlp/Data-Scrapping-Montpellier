#!/bin/sh

h=0
dir=$PWD'/data_graph/voiture_velo.dat'

trace (){
		echo > settings
		echo "set xrange [0:23]" >> settings
		echo "set yrange [0:100]" >> settings
		echo "set title\"Taux d'occupation des parkings | Taux d'utilisation des vélos"\"  >> settings
		echo "set xlabel \"Temps ( en heure )\"" >> settings
		echo "set ylabel \"Taux ( en % )\"" >> settings
		echo "set term jpeg" >> settings
		echo "set output \"test.jpeg\"" >> settings
		echo "plot \""$PWD"/data_graph/voiture_velo.dat\" using 1:2 title\"Taux d'occupation des parkings routiers\" linewidth 2 with lines, \""$PWD"/data_graph/voiture_velo.dat\" using 1:3 title\"Taux d'utilisation des velos\" linewidth 2 with lines" >> settings
		gnuplot settings
}

commit (){
	echo "METTRE COMMANDES COMMIT"
	
	
	
	
}

while [ $h -ne 23 ]; 
do 
	trace
	commit
    ((h++))
	sleep 3700
done
