from audioplayer import *
import os
import time


def on_finish():
    global done
    done += 1


file1 = os.path.join(os.path.dirname(__file__), 'audio',
                     'toquesuave.mp3')  # ringtone by felipebbrusso'
p1 = AudioPlayer(file1, on_finish)

file2 = os.path.join(os.path.dirname(__file__), 'audio',
                     'WarpDrive_01.mp3')  # www.littlerobotsoundfactory.com
p2 = AudioPlayer(file2, on_finish)

repeat = ''
while repeat != 'N':
    p1.volume = 50
    p1.play(PlayMode.ONCE_ASYNC)
    p2.play(PlayMode.ONCE_ASYNC)
    done = 0
    while True:
        print('\rtoquesuave.mp3: {:3.1f}/{:3.1f} [{}]\t WarpDrive_01.mp3: {:3.1f}/{:3.1f} [{}] '.format(
            p1.position, p1.duration, p1.state, p2.position, p2.duration, p2.state), flush=True, end='')
        if done == 2:
            break
        time.sleep(0.1)

    repeat = input('\n\nRepeat [Y/N]: ').upper()
    done = False

file3 = os.path.join(os.path.dirname(__file__), 'audio',
                     'snd_descend.mp3')  # GPLv3 Watabou https://github.com/watabou/pixel-dungeon

print('Now playing "{}"'.format(file3))
AudioPlayer(file3, lambda: print('The end')).play(PlayMode.ONCE_BLOCKING)
