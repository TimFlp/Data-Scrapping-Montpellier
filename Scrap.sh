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
		echo "set output \"photo_graph/test.jpeg\"" >> settings
		echo "plot \""$PWD"/data_graph/voiture_velo.dat\" using 1:2 title\"Taux d'occupation des parkings routiers\" linewidth 2 with lines, \""$PWD"/data_graph/voiture_velo.dat\" using 1:3 title\"Taux d'utilisation des velos\" linewidth 2 with lines" >> settings
		gnuplot settings
}

commit (){
	echo "METTRE COMMANDES COMMIT"
	
	
	
	
}

trace_final (){
		date="$(date +%D)"
		echo > settings-final
		echo "set xrange [0:23]" >> settings-final
		echo "set yrange [0:100]" >> settings-final
		echo "set title\"Taux d'occupation des parkings | Taux d'utilisation des vélos"\"  >> settings-final
		echo "set xlabel \"Temps ( en heure )\"" >> settings-final
		echo "set ylabel \"Taux ( en % )\"" >> settings-final
		echo "set term jpeg" >> settings-final
		echo "set output \"historique_graphiques/$(date +%F).jpeg\"" >> settings-final
		echo "plot \""$PWD"/data_graph/voiture_velo.dat\" using 1:2 title\"Taux d'occupation des parkings routiers\" linewidth 2 with lines, \""$PWD"/data_graph/voiture_velo.dat\" using 1:3 title\"Taux d'utilisation des velos\" linewidth 2 with lines" >> settings-final
		gnuplot settings-final
}

while [ $h -ne 23 ]; 
do 
	trace_final
	trace
	commit
    ((h++))
	sleep 3700
done