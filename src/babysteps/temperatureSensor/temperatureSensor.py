#!/usr/bin/env python

import time, smbus

LM75_ADDRESS            = 0x48
LM75_TEMP_REGISTER      = 0
LM75_CONF_REGISTER      = 1
LM75_THYST_REGISTER     = 2
LM75_TOS_REGISTER       = 3
LM75_CONF_SHUTDOWN      = 0
LM75_CONF_OS_COMP_INT   = 1
LM75_CONF_OS_POL        = 2
LM75_CONF_OS_F_QUE      = 3

class LM75():
    def __init__(self, mode=LM75_CONF_OS_COMP_INT, address=LM75_ADDRESS, busnum=1):
        self._mode = mode
        self._address = address
        self._bus = smbus.SMBus(busnum)

    def regdata2float (self, regdata):
        return (regdata / 32.0) / 8.0

    def toFah(self, temp):
        return (temp * (9.0/5.0)) + 32.0

    def getTemp(self):
        raw = self._bus.read_word_data(self._address, LM75_TEMP_REGISTER) & 0xFFFF
	print "0x%04X"%raw
	print "0b{0:b}".format(raw)
        # raw = ((raw << 8) & 0xFF00) + (raw >> 8)
        raw = ((raw >> 5) & 0xFF00)
	print "0b{0:b}".format(raw)
        return self.toFah(self.regdata2float(raw))


if __name__ == "__main__":
    print "this is not functional yet"
    sensor = LM75(address=0x4C)
    print sensor.getTemp()
