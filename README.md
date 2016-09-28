# tex
    RaspberryPi super controller board for multiple uses: for example museum static airplanes, solar tracker and off-grid water turbine automation.  

### features
<pre>
Overview
    Sensors
        8 analog inputs multiplexed to 12bit ADC at 3KSPS
            Used for temperature, light, voltage, current,
            pressure, flow, AC line sync, etc
        1 power supply current sense ADC

    User Interface
        2 board-mounted user input switches
        3 board-mounted indicator LEDS: R,G,B
        1 128x64 White OLED Display Module
        All connectors are plug-type for easy board replacement
        
    Control
        16 PWM-driven voltage outputs at 7A max with board indicator
        4 dry-contact 10A relays with COM/NC/NO connector
        2 120VAC/8A solid-state relays
        2 DC Motor H-bridge drivers with current sense
            * uses 4 of 16 outputs from above
            Motor direction indicator
        2 opto-coupled inputs for DC motor motion encoders
        2 stepper motor driver signalling outputs, EN/DIR/PULSE
        10 uncommitted digital +5 I/O signals
        
    Peripherals
        Board tempurature sensor
        Battery backed real-time clock 

    Power Supply
        12-26VDC operation, PWM outputs switch this voltage
        +5V DC/DC converter
        Reverse battery protection
        ATF automobile fuse
        
    Communication
        WiFi/Bluetooth 4.0/Ethernet supplied on Raspberry Pi 3
        RS-485 2/4 wire with termination resistor
        External I2C/Power/Ground connector
</pre>
<hr>
<pre>
Detailed
    DC motor 1 h-bridge            discrete fets
    DC motor 1 encoder             cpu interrupt opto-coupled
    DC motor 1 current detect      gain
    DC motor 2 h bridge            discrete fets
    DC motor 2 encoder             cpu interrupt opto-coupled
    DC motor 2 current detect      gain
    AC SSR 1                       i/o slow, unfused
    AC SSR 2                       i/o slow, unfused
    Temperature sensor 1           multiplexed, 10k pullup
    Temperature sensor 2           multiplexed, 10k pullup
    Temperature sensor 3           multiplexed, 10k pullup
    Temperature sensor 4           multiplexed, 10k pullup
    Pyranometer                    analog input with gain
    LED Driver 0                   pwm
    LED Driver 1                   pwm
    LED Driver 2                   pwm
    LED Driver 3                   pwm
    LED Driver 4                   pwm
    LED Driver 5                   pwm
    LED Driver 6                   pwm
    LED Driver 7                   pwm
    LED Driver 8                   pwm
    LED Driver 9                   pwm
    LED Driver 10                  pwm
    LED Driver 11                  pwm
    LED Driver 12                  pwm, push-pull coupled with 13
    LED Driver 13                  pwm, push-pull coupled with 12
    LED Driver 14                  pwm, push-pull coupled with 15
    LED Driver 15                  pwm, push-pull coupled with 14
    Relay 0                        i/o slow, NO/NC contacts
    Relay 1                        i/o slow, NO/NC contacts
    Relay 2                        i/o slow, NO/NC contacts
    Relay 3                        i/o slow, NO/NC contacts
    E-stop input                   cpu interrupt
    Water Pressure                 0-5VDC input
    Water Flow Rate                0-5VDC input with scaler
    External AC voltage detect     0-5VDC input with scaler, half-wave
    External AC current sensor     0-5VDC input with scaler, half-wave
    External AC frequency sensor   use adc from AC V or I sensor
    External 5VDC I/O 0            I/O slow, change interrupt exists
    External 5VDC I/O 1            I/O slow, change interrupt exists
    External 5VDC I/O 2            I/O slow, change interrupt exists
    External 5VDC I/O 3            I/O slow, change interrupt exists
    External 5VDC I/O 4            I/O slow, change interrupt exists
    External 5VDC I/O 5            I/O slow, change interrupt exists
    External 5VDC I/O 6            I/O slow, change interrupt exists
    External 5VDC I/O 7            I/O slow, change interrupt exists
    External 5VDC I/O 8            I/O slow, change interrupt exists
    External 5VDC I/O 9            I/O slow, change interrupt exists
    Stepper control A              enable, direction, step outputs
    Stepper control B              enable, direction, step outputs
    Power supply current monitor   high-side current monitor
    Display                        OLED 0.96 mount intended
    Reverse Battery Protection     FET biased forward bias protection 
</pre>
