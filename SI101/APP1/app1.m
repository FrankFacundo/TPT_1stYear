 clear all;
 close all;
 % % Rapport App 1 : Fréquence perdue
 % Auteurs:
 % BRICENO ANICAMA Martin
 % VARGAS SALAS Veronica
 % FACUNDO RAIME Frank
 % AVILA Marko
 %

 %% ###############  ANALYSE DU PREMIER AUDIO ###############
 
 % 1. Pour estimer la fréquence du symbole envoyer on va faire la TF de la signal
 % et ainsi analyser la fréquence à plus grand coefficient
 %
 % 2. Programme:
 
 % *** I) ANALYSE : symboleA.wav ***
 
 symbole = "./symboleA2.wav"
 % Lecture du fichier
 [y,Fe]=audioread(symbole);
 
 nbE_1 = length(y);
 
 % Passage en fréquence du signal
 y_fft = abs(fft(y));
  figure;
  plot(y_fft,'linewidth',5);
  title("Spectre")
 
 % PLot de la TFD
 %plot(y_fft)
 
 % La valeur qu'on va trouver aura un erreur de 4Hz car on prend 2000 échantillons 
 % sur une plage de 8000Hz. Avec un erreur comme celui-ci on ne peut pas calculer
 % le symbole correcte car ils sont envoyés avec un difference de fréquence de 1Hz
 
 % On veut plus d'échantillons pour un erreur inferieur à 1Hz. On va prolonger
 % le signal de symboleA de telle facon à avoir comme minimum 8000 échantillons.
 
  nbE_2 = 8192;
  
  % TFD signal avec Nb2_Echantillons echantillons
  y2_fft = abs(fft(y,nbE_2));
  
  % Plot signal
  figure;
  plot(y2_fft,'linewidth',5);
  title("Spectre")
  % Recupere Kmax et x[kmax]
  z = ones(2);
  z = k_max(y2_fft, nbE_2);
  kmax = z(1);
  max = z(2);
  
  % Fréquence du symbole
  fsignal = f_transmise(kmax,nbE_2,Fe)
  
  %% Si on trouve un signal qui n'est pas dans l'intervale [501-526] on continue 
  %% à analyser le signal
  
  %condition = fsignal < 501 || f2 > 526
  if ( fsignal < 501 || fsignal > 526 )
    
    % On va analyser la deuxieme moitie du signal pour trouver le symetrique
    z2 = ones(2);
    z2 = k_max2(y2_fft, nbE_2);
    kmax2 = z2(1)
    max2 = z2(2)
    
    % Écart (k) entre le deux pics
    dif_f = kmax2 -kmax;
    
    % On cherche le signal differentiel entre les signaux symétriques. On trouvera 
    % Un pic qui le k appartenant au symbole envoyé
    
    plage = nbE_2-kmax2-1;
    for i=kmax:kmax+plage
      y_dif(i) = y2_fft(i)-y2_fft(i+dif_f);
    end
    
    % Plot de la difference
    figure
    plot(y_dif,'linewidth',5);title("Spectre differentiel");
    
    % Recupere Kmax et x[kmax] de y_dif (siganux differentiel)
    z3 = ones(2);
    long_dif = length(y_dif);
    z3 = k_max2(y_dif,length(y_dif));
    kmax_3 = z3(1)
    max_3 = z3(2);
    
    % Fréquence du symbole
    fsignal_2 = f_transmise(kmax_3,nbE_2,Fe)
    
    fsignal=fsignal_2;
    
  endif
  
  % Résultat final : lettre
  traduction_lettre(fsignal);
    
  % Conclusion: Puique le premier signal est composée du symbole et d'un bruit 
  % aléatoire on essaie de trouver une fŕéquence remarquable dans le
  % signal qui répresentera la fréquence su symbole. 
  % Dans le deuxième cas on ne peut pas utiliser la même méthode car le bruit
  % est beaucoup plus grand que le signal même. On passe à analyser la symétrie
  % de la TFD pour trouver la variation occasionée par la fréquence su signal.
  
  
  
  