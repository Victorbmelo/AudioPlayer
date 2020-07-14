from audioplayer import AudioPlayer
import os

mp3 = os.path.join(os.path.dirname(__file__), 'audio', 'toquesuave.mp3') # ringtone by felipebbrusso'

p = AudioPlayer(mp3)

print('Playing {} in loop'.format(p.fullfilename))
p.play(block=False, loop=True)
print('Current state: {}'.format(p.state))
print('Duration: {:.2f} s'.format(p.duration))

input('Press Enter to pause ')
p.pause()
print('Current state: {}'.format(p.state))

input('Current position: {:.2f} s\nPress Enter to resume '.format(p.position))
p.resume()
print('Current state: {}'.format(p.state))

input('Press Enter to go to 00:02.2 ')
p.position = 2.2
print('Current state: {}'.format(p.state))

input('Press Enter to set volume to 1% ')
p.volume = 1

input('Press Enter to set volume to 10% ')
p.volume = 10

input('Press Enter to set volume to 50% ')
p.volume = 50

input('Press Enter to set volume to 100% ')
p.volume = 100

input('Press Enter to stop ')
p.stop()
print('Current state: {}'.format(p.state))

input('Press Enter to play once ')
p.play(block=True)