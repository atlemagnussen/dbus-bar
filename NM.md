# Network Manager dbus commands
## Get All
```sh
dbus-send --system --print-reply --dest=org.freedesktop.NetworkManager \
    /org/freedesktop/NetworkManager \
    org.freedesktop.DBus.Properties.GetAll \
    string:"org.freedesktop.NetworkManager"
```
## Get active
```sh
dbus-send --system --print-reply --dest=org.freedesktop.NetworkManager \
    /org/freedesktop/NetworkManager \
    org.freedesktop.DBus.Properties.Get \
    string:"org.freedesktop.NetworkManager" \
    string:"ActiveConnections"
```