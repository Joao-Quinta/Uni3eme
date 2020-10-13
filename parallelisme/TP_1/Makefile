all: broadcastSimple broadcastAnneau broadcastHyper


broadcastSimple: broadcastSimple.o
        mpic++ broadcastSimple.o -o broadcastSimple
broadcastAnneau: broadcastAnneau.o
        mpic++ broadcastAnneau.o -o broadcastAnneau
broadcastHyper: broadcastHyper.o
        mpic++ broadcastHyper.o -o broadcastHyper

broadcastSimple.o: broadcastSimple.cpp
        g++ -c broadcastSimple.cpp -o broadcastSimple.o

broadcastAnneau.o: broadcastAnneau.cpp
        g++ -c broadcastAnneau.cpp -o broadcastAnneau.o

broadcastHyper.o: broadcastHyper.cpp
        g++ -c broadcastHyper.cpp -o broadcastHyper.o
