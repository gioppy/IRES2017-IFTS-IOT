import glob

sensor_dir = "/sys/bus/w1/devices/"

def setSensors():
  sensors = []
  try:
    path = glob.glob(sensor_dir + "28*")
    for address in path:
      sensors.append(address)
  except:
    sensors.append("Bus 1Wire Error")
  return sensors

def getTemperature(address):
  sensors = {}
  for s in address:
    try:
      with open(s + "/w1_slave", "r") as f:
        sensors[s] = float(f.readlines()[1].split("t=")[1])/1000
        f.close()
    except:
      sensors[s] = "Error getting teperature"
  return sensors

if __name__ == '__main__':
  sensors = setSensors();
  print("Finding this sensors: {}".format(sensors))
  print("Temperature is: {}".format(getTemperature(sensors)))