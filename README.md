## Si5351 Raspberry Pi


Python library for easy frequency synthesis using an Si5351 clock generator connected to Raspberry Pi's I2C bus.
This library is currently under development and testing.

### Features

* For Silicon Labs Si5351A ([datasheet](https://www.silabs.com/documents/public/data-sheets/Si5351-B.pdf)).
* Allows easy frequency synthesis for any frequency between 4Khz and 150Mhz with a resolution of 0.01Hz.
* Oriented to radio ham projects.

### Usage

    RFGen = Si5351.Si5351(busnum=1)

    desired_output = 0
    desired_freq   = 1045896  #10.45896KHz (0.01Hz resolution)  

    RFGen.setFreq(desired_freq, desired_output)



