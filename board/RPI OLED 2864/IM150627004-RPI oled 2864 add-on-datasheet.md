# Raspberry PI OLED 2864 Add-on V2.0 #

## Introduction ##

There are seldom OLED add-ons customized for Raspberry Pi in the open source hardware market. In a lot of projects, we only need to display little information such as the state of system or IP. What’s more, when we have a high requirement for its portability, it’s unsuitable to connect a big screen to Raspberry Pi via HDMI interface. Thus, a tiny OLED add-on can satisfy this demand.

OLED add-on with built-in 0.96" 128*64 OLED and SSD1306 control chip is customized for Raspberry Pi. Every single pixel in OLED can be lighted up or off by this SSD1306 control chip.

We not only offer an easily-plugged add-on for Raspberry Pi, but also provide an SDK that help you transplant Arduino’s driver into Raspberry Pi. After installing the SDK, you can drive this add-on as easily as you do on Arduino.

## Feature ##



- Customized for Raspberry Pi, plug and play without wiring

- 0.96" OLED with 128*64 pixels


- Stackable


- Coming with 2.54 interface for Electronic bricks


## Specification ##

<table>
<tr>
  <th>PCB size</th>
  <td>65mm X 43mm X 1.6mm</td>
</tr>
<tr>
  <th>Operation Level</th>
  <td>Digital 3.3V DC</td>
</tr>
</table>

## Hardware ##

请看IM150627004-RPI oled 2864 add-on-dimension.pdf



## Pinmap ##

<table>
<tr>
  <th>Raspberry PI Pin N.O.</th>
  <th>Pin name</th>
  <th>Description</th>
</tr>
<tr>
  <td>1</td>
  <td>3.3V</td>
  <td></td>
</tr>
<tr>
  <td>2</td>
  <td>5V</td>
  <td></td>
</tr>
<tr>
  <td>3</td>
  <td>GPIO02</td>
  <td>OLED_SDA</td>
</tr>
<tr>
  <td>4</td>
  <td>5V</td>
  <td></td>
</tr>
<tr>
  <td>5</td>
  <td>GPIO03</td>
  <td>OLED_SCL</td>
</tr>
<tr>
  <td>6</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>7</td>
  <td>GPIO04</td>
  <td>OLED_RST</td>
</tr>
<tr>
  <td>8</td>
  <td>GPIO14</td>
  <td>TXD</td>
</tr>
<tr>
  <td>9</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>10</td>
  <td>GPIO15</td>
  <td>RXD</td>
</tr>
<tr>
  <td>11</td>
  <td>GPIO17</td>
  <td></td>
</tr>
<tr>
  <td>12</td>
  <td>GPIO18</td>
  <td></td>
</tr>
<tr>
  <td>13</td>
  <td>GPIO27</td>
  <td></td>
</tr>
<tr>
  <td>14</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>15</td>
  <td>GPIO22</td>
  <td></td>
</tr>
<tr>
  <td>16</td>
  <td>GPIO23</td>
  <td></td>
</tr>
<tr>
  <td>17</td>
  <td>3.3V</td>
  <td></td>
</tr>
<tr>
  <td>18</td>
  <td>GPIO24</td>
  <td></td>
</tr>
<tr>
  <td>19</td>
  <td>GPIO10</td>
  <td>SPI_MOSI</td>
</tr>
<tr>
  <td>20</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>21</td>
  <td>GPIO09</td>
  <td>SPI_MISO</td>
</tr>
<tr>
  <td>22</td>
  <td>GPIO25</td>
  <td></td>
</tr>
<tr>
  <td>23</td>
  <td>GPIO11</td>
  <td>SPI_SCK</td>
</tr>
<tr>
  <td>24</td>
  <td>GPIO08</td>
  <td>SPI_CE0</td>
</tr>
<tr>
  <td>25</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>26</td>
  <td>GPIO07</td>
  <td>SPI_CE1</td>
</tr>
<tr>
  <td>27</td>
  <td>ID_SD</td>
  <td></td>
</tr>
<tr>
  <td>28</td>
  <td>ID_SC</td>
  <td></td>
</tr>
<tr>
  <td>29</td>
  <td>GPIO05</td>
  <td></td>
</tr>
<tr>
  <td>30</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>31</td>
  <td>GPIO06</td>
  <td></td>
</tr>
<tr>
  <td>32</td>
  <td>GPIO12</td>
  <td></td>
</tr>
<tr>
  <td>33</td>
  <td>GPIO13</td>
  <td></td>
</tr>
<tr>
  <td>34</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>35</td>
  <td>GPIO19</td>
  <td></td>
</tr>
<tr>
  <td>36</td>
  <td>GPIO16</td>
  <td></td>
</tr>
<tr>
  <td>37</td>
  <td>GPIO26</td>
  <td></td>
</tr>
<tr>
  <td>38</td>
  <td>GPIO20</td>
  <td></td>
</tr>
<tr>
  <td>39</td>
  <td>GND</td>
  <td></td>
</tr>
<tr>
  <td>40</td>
  <td>GPIO21</td>
  <td></td>
</tr>
</table>

## Download ##

schematic: 请看IM150627004-RPI oled 2864 add-on-schematic.pdf


## Useful Link ##

https://github.com/itead/SDK

https://github.com/itead/SDK/tree/master/libraries/itead_SSD1306