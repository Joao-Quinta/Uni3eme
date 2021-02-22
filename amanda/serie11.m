liste = [5,6,3,4,1,2];
n=length(liste);
for i=1:n-1
    for j=1:n-i
        gauche=liste(j);
        droite=liste(j+1);
        if gauche> droite
            liste(j+1)=gauche;
            liste(j)=droite;
        end
    end
    liste
end
liste
