from random import uniform



a = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1]
b = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1]

u1 = [uniform(0,3) for i in xrange(101)]
u2 = [uniform(0,3) for i in xrange(101)]

py = [[0.25,0.75],[0.1,0.9]]
px = [ [[0.5,0.5],[0.6,0.4]], [[0.8,0.2],[0.2,0.8]] ]

y = [0]
for i in xrange(100):
    if uniform(0,1) < py[y[i]][0]:
        y.append(0)
    else:
        y.append(1)


x = [0]
for i in xrange(100):
    if uniform(0,1) < px[y[i]][x[i]][0]:
        x.append(0)
    else:
        x.append(1)




In [43]: transferEntropyPermutationA(b,a,1,2,200,2)
Out[43]: 
[0.010781798401705813,
 0.028856364016895553, 
 0.025471743733881509,
 -0.7095927865805145,
 136.0,
 0.68]

In [44]: transferEntropyPermutationA(a,b,1,2,1000,2)
Out[44]: 
[0.043410100997428896,
 0.027027759874135714,
 0.025233141585304257,
 0.64923905998428011,
 213.0,
 0.213]



In [45]: transferEntropyPermutationA(u1,u2,1,2,1000,2)
Out[45]: 
[0.0019658610240205652,
 0.0047437192409420896,
 0.0045737590087260504,
 -0.60734686974582286,
 668.0,
 0.668]

In [46]: transferEntropyPermutationA(u2,u1,1,2,1000,2)
Out[46]: 
[0.00080272261156165957,
 0.0044598405482513962,
 0.0044420955979002884,
 -0.82328663489781739,
 827.0,
 0.827]

In [47]: transferEntropyPermutationA(x,y,1,2,1000,2)
Out[47]: 
[0.053400723502321959,
 0.0049774705027626895,
 0.0045268081275294967,
 10.696997008792206,
 0,
 0]

In [48]: transferEntropyPermutationA(y,x,1,2,1000,2)
Out[48]: 
[0.009910320086376833,
 0.0045433772690964339,
 0.0040129841412708984,
 1.3373944746217479,
 92.0,
 0.092]