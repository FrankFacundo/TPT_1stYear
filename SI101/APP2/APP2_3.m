hold on
P = 12;
somme = 0;
valeur = [zeros(1,144)];
for c = 1:144
    for r = -12: 12
        if ( (c + r > 0) && (c + r <= 144) )
          somme = somme + cco2(c + r);
        end 
        
    end
    if c <= 12
      valeur(c) = NaN;
    elseif c >= 133
      valeur(c) = NaN;
    else
    valeur(c) = somme/25;
    endif
    
    somme = 0;
end

%plot(valeur, 'linewidth',5)

a = 0.125862;
b = 329.9838;
%x = 13:132;
x = 1:132;
%plot(b + a*x , 'linewidth',5)

plot(cco2 , 'linewidth',5)

b_filter = 25
a_filter = 1
%y = filter(b_filter,a_filter,valeur);


%2e solution : utilisation de 
A = 1 ;
B = ones(1,(2*P+1))/(2*P+1) ;

X = filter(B,A,cco2);

%off_set = (2*P+1:144)' - X(2*P+1:144) ;
%X = mean(off_set) + X ;

%plot(y(2*P+1:144),X((2*P+1):144),'r');

for r = 1: 24
  X(r) = NaN;
end

X2 = [zeros(1,144)];
for r = 1: 144
  if r <= 12
    X2(r) = NaN;
  elseif r<=132
    X2(r) = X(r+12);
  else
    X2(r) = NaN;
  end
end
plot(X2)
