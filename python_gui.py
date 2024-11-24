import serial
from tkinter import *
import threading

arduino_port='COM6'                              #indicating the port to which Arduino UNO is connected
data_speed=9600                                  #determining the speed at which the data is being transferred

font_big=("Segoe UI",40)
font_big_2=("Segoe UI",120)
font_big_3=("Segoe UI",30)

           

def main():

    def reader(arduino):

        while True:
            

            data_received=arduino.readline()                                              #This will read the data from the arduino board
            data_decoded=data_received.decode()                                           #This will decode the data
            data_final=data_decoded.strip()                                               #This will clean the decoded data

            if data_final:                                                                #This will only allow the actual data to be printed

                l=data_final.split()                                                      #Getting humidity and temperature values

                humidity_val=l[2]                                                         #Getting humidity value from list
                temp_C_val=l[8]                                                           #Getting the temp in C value from list
                temp_F_val=l[14]                                                          #Getting the temp in F value from list
                heat_index=l[len(l)-2]                                                    #Getting the heat index value from list

                rain_con=l[19];                                                           #Getting the rain condition from list

                f21=Frame(a,height=1400,width=2240,bg="#d6eaf8")                          #Creating a background colored frame
                f21.place(x=0,y=0)                                                        #Placing the background frame 

                
                l11=Label(a,text="Humidity : "+humidity_val+" %",font=font_big,bg="#d6eaf8")   #Displaying the humidity value   
                l11.place(x=50,y=700)                                                          #Placing display value 
                
                l12=Label(a,text=temp_C_val+" C",font=font_big_2,bg="#d6eaf8")            #Displaying the temperature value in Centigrage
                l12.place(x=50,y=100)                                                     #Placing display value

                l17=Label(a,text="Feels like "+heat_index+" C",font=font_big,bg="#d6eaf8")                  #Displaying the temperature value in Fahrenhite
                l17.place(x=50,y=350)                                                                       #Placing display value

                
                l13=Label(a,text="Temperature in Fahrenhite : "+temp_F_val+" F",font=font_big,bg="#d6eaf8")             #Displaying the temperature value in Fahrenhite
                l13.place(x=50,y=550)                                                                                   #Placing display value

                l15=Label(a,text="Current Location",font=font_big,bg="#d6eaf8")           #Displaying current location 
                l15.place(x=950,y=100)                                                    #Placing current location         
                
                if (rain_con=="rain_detected"):

                        l14=Label(a,text="Rain Detected",font=font_big_3,bg="#d6eaf8")     #Displaying the alert that rain has been detected
                        l14.place(x=950,y=240)                                             #Placing the alert

                else:

                        l14=Label(a,text="No Rain Detected",font=font_big_3,bg="#d6eaf8")  #Displaying the alert that rain has not been detected 
                        l14.place(x=950,y=240)                                             #Placing the alert
        

    def start_reader(arduino):
    
         thread = threading.Thread(target=reader, args=(arduino,))
         thread.daemon = True
         thread.start()

    try:

    

         arduino=serial.Serial(arduino_port,data_speed,timeout=2)                          #This will create an object of the Serial class

         a=Tk()
         a.title("Weather App")
         a.geometry("2240x1400")

         f11=Frame(a,height=1400,width=2240,bg="#d6eaf8")                                  #Creating a background colored frame
         f11.place(x=0,y=0)                                                                #Placing the background frame

         l31=Label(a,text="Temperature in Fahrenhite : ",font=font_big,bg="#d6eaf8")                  #Displaying the temperature value in Fahrenhite
         l31.place(x=50,y=550)                                                                        #Placing display value

         l32=Label(a,text="Humidity : ",font=font_big,bg="#d6eaf8")                #Displaying the humidity value   
         l32.place(x=50,y=700)                                                     #Placing display value

         start_reader(arduino)

         a.mainloop()
    

    except:

         
         print("Cannot get the data.")                                                     #This will print to indicate that arduino is not connected


main()
