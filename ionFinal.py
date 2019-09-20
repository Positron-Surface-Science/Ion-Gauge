# -*- coding: utf-8 -*-

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

t = time.clock();

ser = serial.Serial('COM3', 9600);

#if ser.isOpen() == False:
#    ser.open();
#ser.open();   

ser.close();

dataVoltS = list();
dataVoltE = list();
pressure = list();
x = list();

#plt.axis(0,10,-1,10);
fig = plt.figure();
ax = plt.gca();#axes(xlim=(0,30), ylim=(0,0.0099));
#ax.set_yscale('linear');
ax.set_yscale('log');

line, = ax.plot([], [], lw=2);
#ax1 = fig.add_subplot(1,1,1);

def init():
    line.set_data([], []);
    return line,

def animate(i):
    ser.open();
    foundS = False;
    foundE = False;
    #reading2 = ser.readline();
    

    while foundS == False or foundE == False:
        
        readingValue = 0;
        
        readingValue = ser.readline()#.decode("utf-8");
        stringValue = str(readingValue);
        
        if (stringValue[stringValue.find("*")-1:stringValue.find("*")] == "s") and foundS == False:
            
            readingSignificand = readingValue[stringValue.find("*")-10:stringValue.find("*")-4];
            foundS = True;
            
        elif (stringValue[stringValue.find("*")-1:stringValue.find("*")] == "e") and foundE == False:
            
            readingExponent = readingValue[stringValue.find("*")-10:stringValue.find("*")-4];
            foundE = True;
            
        else:
            continue;
            
         
    ser.close();
    
    exponent = round((float(readingExponent)*10 - 11));      
    significand = (float(readingSignificand)*100);

    
    

    #dataVoltS.append(significand);
    #dataVoltE.append(exponent);

    pressure.append(significand*(10**exponent));#m.pow(significand,exponent));

    x.append((time.clock() - t)/60);# = range(len(pressure));
    #ax.set_xlim(len(dataVolt)+10);

    line.set_data(x, pressure);
    
    ax.relim();
    ax.autoscale_view();
   
#    ax1.clear();
#    ax1.plot(xar,dataVolt);
    
    return line,
    
plt.ylabel('Pressure (Torr)');
plt.xlabel('Time (Minutes)');

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, interval=5000, blit=False);

#plt.grid();
plt.tick_params(axis='y', which='minor');
#ax.yaxis.set_minor_formatter(FormatStrFormatter("%.1f"));
plt.grid(True, which="both", ls="-");

ax.set_yticks(np.logspace(min(pressure),max(pressure)));
plt.show();

ser.close();
       
#    while True:
 #       counter += 1;
  #      reading = ser.readline();
   #     ymin = 0;
    #    ymax = 5;
     #   plt.ylim([ymin,ymax])
      #  dataVolt.append(reading[0:8]);
       # del dataVolt[0]
        #p.set_xdata(range(len(dataVolt)));
        #p.set_ydata(dataVolt)
        #plt.draw()
             
        #if counter == 10:
         #   break;

#plt.plot(dataVolt); 
#ax = plt.gca();

#print(dataVolt);