from pulsectl import Pulse, PulseVolumeInfo

pulse = Pulse()
sinks = pulse.sink_list()
sink = sinks[0]

print(sink.mute)
print(sink.volume.value_flat)