
a=100000000;
p = calcule_tous_premiers(a);
l=dichotomie(p,a)



function p = calcule_tous_premiers(a)
% limite sup du tableau
    p=[];
    for i=2:a
        premier = 0;
      for j=2:i-1
          div=i/j;
         if floor(div)==div
             premier=1;
             %la = pas premier -> pas le mettre dans p
             %j = i
         end
         %j = j+1
      end
      if premier == 0
          taille = length(p);
          p(taille+1) = i;
      end
      
    end
end

function l=dichotomie(p,a)
for i=1:a
    l(i)=0;
end
for j=1:length(p)
  val=p(j);
  l(val)=1;
end
end
