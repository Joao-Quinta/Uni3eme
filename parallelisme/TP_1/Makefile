all: broadcastSimple broadcastAnneau broadcastHyper broadcast


broadcastSimple: broadcastSimple.o
	mpic++ broadcastSimple.o -o broadcastSimple
broadcastAnneau: broadcastAnneau.o
	mpic++ broadcastAnneau.o -o broadcastAnneau
broadcastHyper: broadcastHyper.o
	mpic++ broadcastHyper.o -o broadcastHyper
broadcast: broadcast.o
	mpic++ broadcast.o -o broadcast

broadcastSimple.o: broadcastSimple.cpp
	g++ -c broadcastSimple.cpp -o broadcastSimple.o
broadcastAnneau.o: broadcastAnneau.cpp
	g++ -c broadcastAnneau.cpp -o broadcastAnneau.o
broadcastHyper.o: broadcastHyper.cpp
	g++ -c broadcastHyper.cpp -o broadcastHyper.o
broadcast.o: broadcast.cpp
	g++ -c broadcast.cpp -o broadcast.o

clean:
	rm -r *.o
