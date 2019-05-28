## Copyright (C) 2019 vero
## Author: vero <vero@vero-K501UX>
## Created: 2019-03-21

function [l] = traduction_lettre(f)
  
  if ( f >= 501 && f <= 526 )
    f_int = int32(f);
    dif = abs(f_int-f);
    
    if (dif >= 0.5) 
      f= f_int+1;
    else
      f= f_int;
    end
    
    %Lettres
    lettre = ['A','B','C','D','E','F','G,','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    
    %% Traduction lettre:
    pos = f-500;
    
    l = lettre(1,pos);
 else
    l = " ";
    endif

endfunction
