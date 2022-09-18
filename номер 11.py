import math #номер 11
x=6.251
y=0.827
z=25.001

s=y**((abs(x))**(1./3.))+(math.cos(y)*math.cos(y)*math.cos(y))*(abs(x-y)*(1+(math.sin(z)*math.sin(z))/ \
(math.sqrt(x+y))))/((math.e**(abs(x-y)))+(x)/(2))
print(round(s,6))