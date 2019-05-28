### Main 
clear all;
close all;

%% Information signal:
symbole = "./mess.wav"
[s,Fe]=audioread(symbole);


#Modification matrice y
if(length(s(1,:)) < length(s(:,1)))
  s = s';
end

message = decode(s,Fe)