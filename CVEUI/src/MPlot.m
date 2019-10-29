clc;
clear all;
close all;

staticTDB = [6,4,1,96,41,19,1,44,7];
figure(1)
bar(staticTDB,0.5,'b');
set(gca,'XTickLabel',{'Meter', 'PowerSCADA','AMI', 'WebAccess','SQL','Controller','PowerHMI','PLC','RTU'}) 
figure(2)
explode=[1 1 1  0 0 0 1 0 1]
pie(staticTDB,explode)
colormap(cool)