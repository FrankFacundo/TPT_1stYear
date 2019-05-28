## Copyright (C) 2019 vero
## Author: vero <vero@vero-K501UX>
## Created: 2019-03-21

function [val] = k_max (y, largeur)
  kmax = 0;
  max = 0;
  val =ones(2);
  
  for i = 1:(largeur/2)
    if (y(i)> max)
      max = y(i);
      kmax = i;
    endif
  end
  kmax;
  max;
  val = [kmax , max];
endfunction
