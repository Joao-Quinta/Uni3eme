%{
liste1 = [5 6 9 10];
liste2 = [1 ; 2 ;3 ;4];

liste4 = [1 ; 2 ; 3; 4];
liste3 = [];
i=1;
for i = [2 4]
    %a= liste1(i)
    %total= liste1(i)+total
    j = length(liste3)+1;
    i;
    liste3(j,1)= liste1(i)+ liste2(i);
    

end
liste3;
%liste3(1) = 4 # met 4 dans la liste3, à l indice 1

A=[1 2;3 4];
B=[2 3;4 5];
C=[];
taille = size(A);

ligne = taille(1)+1;
colonne = taille(2)+1;
i=1;


while i<ligne
    j=1;
    
    while j<colonne
        A(i,j)
        j=j+1;
    end
    i=i+1;
end


for i = 1:taille(1)
    for j=1:taille(2)
       C(i,j)=A(i,j) + B(i,j)
    end
end 



A=[1 2; 3 6];
B=[1 2; 3 4];
A(1,2)
C=[];
taille=size(A);
ligne=taille(1)+ 1;
colonne=taille(2)+1;
i=1;
while i < ligne 
   j=1;
    while j< colonne
        C(i,j)= A(i,j)*B(i,j)
         j=j+1;
    end
i=i+1;
end
%}

%{
A=[1 2; 3 4];
B= [1; 2];
C=[];
i=1;
taille=size(A);
ligne=taille(1) + 1;
colonne = taille(2) + 1;
while i< ligne 
    j=1;
    resultat=0;
    while j< colonne
        resultat= resultat + A(i,j)*B(j)
        j=j+1;
    end
    C(i,1)= resultat
    i=i+1;
end
%}

mat1=[1 2 3; 3 4 4];
mat2=[1 2 ; 3 4];
matRes = multiplication(mat1,mat2)


mat1=[1 2 3; 3 4 3];
mat2=[1 2 3 4 3 4; 3 4 4 5 6 7; 3 4 5 6 6 7];
matRes = multiplication(mat1,mat2)


%%
function C = multiplication(A,B)
    tailleB=size(B);
    bigcolonne=tailleB(2)+1;
    tailleA=size(A);
    ligne= tailleA(1)+1;
    colonne= tailleA(2)+1;
    compatible=verification(tailleA,tailleB)
    if compatible==1
        C=[];
        z=1;
        while z< bigcolonne
            i=1;
            while i<ligne
                resultat=0;
                j=1;
                while j< colonne
                   resultat= resultat + A(i,j)*B(j,z);
                    j=j+1;
                end
                C(i,z)=resultat;
                i=i+1; 
            end
            z=z+1;
        end 
    else
        C=0;
        disp("incompatible");
    end
end

function compatible= verification(tailleA,tailleB)
    compatible = 0
    if tailleA(2)==tailleB(1)
        compatible=1
    end
end













    