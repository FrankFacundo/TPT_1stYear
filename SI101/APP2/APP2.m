%plot(cco2)

minus = 0;
%new_co2 = cco2 - minus;

%new_co2 =[cco2 * hamming(144); zeros(8192,1)];
new_co2 =[cco2 ; zeros(8192,1)];
fft_co2 = fft(new_co2);
plot(20*log10(abs(fft_co2)), 'linewidth',5)

