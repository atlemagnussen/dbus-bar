import dbus

bus = dbus.SessionBus()

bus_name = 'org.mpris.MediaPlayer2.spotify'
path = '/org/mpris/MediaPlayer2'
interface_name = 'org.mpris.MediaPlayer2.Player'

bus_object = bus.get_object(bus_name, path)
interface = dbus.Interface(bus_object, dbus_interface='org.mpris.MediaPlayer2.Player')
interface.PlayPause()

props_iface = dbus.Interface(bus_object, dbus_interface='org.freedesktop.DBus.Properties')
props = props_iface.GetAll("org.mpris.MediaPlayer2.Player")
print("hemm")