import numpy as np
from scipy import signal

n=1440
AQI_readings=np.random.random(1440)
for i in range(0,1440):
    AQI_readings[i]=AQI_readings[i]*10
print(AQI_readings)
a=signal.savgol_filter(AQI_readings,23,2)
print(a)


def average_AQI(a):
    avg_hourly=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    n=1440//60
    for i in range(0,n):
        total_aqi_avg=0
        for j in range(0,60):
            total_aqi_avg=total_aqi_avg+a[i+j]
        
        avg_hour=total_aqi_avg/60
        avg_hourly[i]=(avg_hour)
     
    return  avg_hourly 
        
hour=average_AQI(a)
print(hour)

OUTPUT:
[8.46257336 8.63847001 4.18287463 ... 5.92074016 8.37087513 4.0999345 ]
[6.68772693 6.54532592 6.40577739 ... 4.98468685 4.94881912 4.90307769]
[4.9410606  4.88261175 4.83530626 4.7937525  4.75870971 4.72510727
 4.69544303 4.67427258 4.65264364 4.64159998 4.63568421 4.64148936
 4.65363326 4.66391212 4.67744714 4.69285788 4.70969542 4.7260116
 4.73408294 4.72743947 4.72976863 4.73813856 4.74054084 4.74517256]


import matplotlib.pyplot as plt
X=np.arange(1440)
plt.plot(X,AQI_readings,color="green")
plt.plot(X,a,color="blue")
plt.show()
import numpy as np
from scipy import signal

n=1440
AQI_readings=np.random.random(1440)
for i in range(0,1440):
    AQI_readings[i]=AQI_readings[i]*10
print(AQI_readings)
a=signal.savgol_filter(AQI_readings,23,2)
print(a)


def average_AQI(a):
    avg_hourly=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    n=1440//60
    for i in range(0,n):
        total_aqi_avg=0
        for j in range(0,60):
            total_aqi_avg=total_aqi_avg+a[i+j]
        
        avg_hour=total_aqi_avg/60
        avg_hourly[i]=(avg_hour)
     
    return  avg_hourly 
        
hour=average_AQI(a)
print(hour)

OUTPUT:
[8.46257336 8.63847001 4.18287463 ... 5.92074016 8.37087513 4.0999345 ]
[6.68772693 6.54532592 6.40577739 ... 4.98468685 4.94881912 4.90307769]
[4.9410606  4.88261175 4.83530626 4.7937525  4.75870971 4.72510727
 4.69544303 4.67427258 4.65264364 4.64159998 4.63568421 4.64148936
 4.65363326 4.66391212 4.67744714 4.69285788 4.70969542 4.7260116
 4.73408294 4.72743947 4.72976863 4.73813856 4.74054084 4.74517256]


import matplotlib.pyplot as plt
X=np.arange(1440)
plt.plot(X,AQI_readings,color="green")
plt.plot(X,a,color="blue")
plt.show()



X2=np.arange(23)
plt.plot(X2,avg_hourly,color="green")





X2=np.arange(23)
plt.plot(X2,avg_hourly,color="green")


