
function [message] = decode (s, Fe)
  
  warning('off','all');
  
  s_symbole = [];
  epc_vide = 500;
  nb_echantillon = 2000;
  Nt_ech = length(s);
  pivot = 0;
  message = [];
  
  %debut = nb_echantillon*i+1+i*epc_vide;

  while (Nt_ech - pivot >= 2000)
    debut  = pivot+1;
    s_symbole = s(debut:(debut+nb_echantillon-1));
    %length(s_symbole)
    
    % Analyse:
    freq = analyse_1symbole (s_symbole, Fe)
    l = traduction_lettre(freq);
    message = [message l];
    
    pivot = pivot + nb_echantillon + epc_vide;
  end
  
  
endfunction
;