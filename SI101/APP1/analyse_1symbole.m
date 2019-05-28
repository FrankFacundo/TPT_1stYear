## Copyright (C) 2019 vero
## Author: vero <vero@vero-K501UX>
## Created: 2019-03-24

function [freq_s] = analyse_1symbole (s_t, Fe)

# Data
M_echantillon = 8000 * 10;
nb_symbole = 2000;
s_tfd_k = [];
s_tfd_f = [];
valeur = [];
freq_s = 0;
freq_m = 0;

%% s_t(1,1:10) //test

#Analyse 1:

%s_tfd_k = abs(real(fft(s_t,M_echantillon)));
s_tfd_k = abs(fft(s_t,M_echantillon));
k = 1:M_echantillon;

% Image de la TFD
%plot(k,s_tfd_k);

% Frequence du signal
valeur = k_max(s_tfd_k, M_echantillon);
  kmax_1 = valeur(1);
  max_1 = valeur(2);

  freq_s = f_transmise(kmax_1, M_echantillon, Fe);

if ( freq_s < 501 || freq_s > 526 )
  
  #Analyse 2:
  valeur = k_max2(s_tfd_k, M_echantillon);
    kmax_2 = valeur(1);
    max_2 = valeur(2);
    
    % Écart (k) entre le deux pics
    dif_k = kmax_2 -kmax_1;
    
    %Signal differentiel
    plage = M_echantillon-kmax_2-1;
    for i = kmax_1:kmax_1+plage
      s_dif(i) = s_tfd_k(i)-s_tfd_k(i+dif_k);
    end
    
    
    %Recupere Kmax et x[kmax] de y_dif (siganux differentiel)
    long_dif = length(s_dif);
    valeur = k_max2(s_dif,length(s_dif));
      kmax_3 = valeur(1);
      max_3 = valeur(2);
    
    
    %Fréquence du symbole
    freq_m = f_transmise(kmax_3,M_echantillon,Fe);
    
  
    freq_s = freq_m;
    
  endif
  
    if (freq_m >= 500 && freq_m <= 502)
      figure
      plot(k,s_tfd_k);
      title("TFD")
      figure
      plot(s_dif);
      title("Signal differentiel")
    endif
endfunction
