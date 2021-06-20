import time
from Motor import *
from ADC import *
class Light:
    def run(self):
        try:
            self.adc=Adc()
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            while True:
                L = self.adc.recvADC(0)
                R = self.adc.recvADC(1)
                print ("The photoresistor voltage on the right is "+str(R)+"V")
                print ("The photoresistor voltage on the left is "+str(L)+"V")
                if L < 2.99 and R < 2.99 :
                    self.PWM.setMotorModel(600,600,600,600)
                    
                elif abs(L-R)<0.15:
                    self.PWM.setMotorModel(0,0,0,0)
                    
                elif L > 3 or R > 3:
                    if L > R :
                        self.PWM.setMotorModel(-1200,-1200,1400,1400)
                        
                    elif R > L :
                        self.PWM.setMotorModel(1400,1400,-1200,-1200)
                    
        except KeyboardInterrupt:
           led_Car.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is starting ... ')
    led_Car=Light()
    led_Car.run()


        
    

