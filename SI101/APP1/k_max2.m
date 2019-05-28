## Copyright (C) 2019 vero
## Author: vero <vero@vero-K501UX>
## Created: 2019-03-21

function [val] = k_max2 (y, largeur)
  kmax2 = 0;
  max2 = 0;
  val =ones(2);
  init = int16(largeur/2);
  
  for i = init:largeur
    if (y(i) > max2)
      max2 = y(i);
      kmax2 = i;
    endif
  end
  
  kmax2;
  max2;
  val = [kmax2 , max2];
endfunction
