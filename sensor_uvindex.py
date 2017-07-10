# Simple example of reading the MCP3008 analog input channels and printing them all out.
#
# Requires Ahttps://github.com/adafruit/Adafruit_Python_MCP3008
#
# Author: Alan McNatty - based very very heavily on example script for the MCP3008 
#                        written by Tony DiCola
# License: Public Domain

import time
import psycopg2

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def mapfloat(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

#print('INFO: Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
conn = psycopg2.connect("dbname=sensor user=pi host=localhost")
cur = conn.cursor()

# Main program loop.
last = 0.0
while True:
    outputVoltage = 3.3 * float(mcp.read_adc(0)) / 1023
    uvIntensity = mapfloat(outputVoltage, 0.99, 2.9, 0.0, 15.0);
    if ( uvIntensity != last ):
        print "INFO: UV Index = {:f}".format(uvIntensity)
        cur.execute("INSERT INTO reading (name, value) VALUES (%s, %s)", ("UV Index", str(uvIntensity)))
        conn.commit()
        last = uvIntensity
    time.sleep(5)

cur.close()
conn.close()
