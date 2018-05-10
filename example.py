import Si5351

#Instance of generator, connected to I2C1 in the raspberry pi
RFGen = Si5351.Si5351(busnum=1)

#Generate frequency 10.45896KHz in output 0
RFGen.setFreq(1045896, 0)

