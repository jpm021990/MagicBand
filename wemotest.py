import pywemo

def get_device():
  devices = pywemo.discover_devices()
  print('Devices:', devices)

  return
  
  device = filter(lambda device: device.[SOME_PROPERTY] == [SOME_PROPERTY], devices)
  
  return device

def trigger_switch():
  return print('We can\'t run this function until we return the right device from get_device')

  device = get_device()

  if (device) device.toggle()

def main():
  trigger_switch()

if __name__ == '__main__':
  main()
