import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True,
                 input_vo_keyboard=True)


@player.property_observer('time-pos')
def time_observer(_name, value):
    print('Now playing at {:.2f}s'.format(value))


# player.fullscreen = True
# player.loop_playlist = 'inf'
player['vo'] = 'gpu'


@player.on_key_press('s')
def my_s_binding():
    pillow_img = player.screenshot_raw()
    pillow_img.save('hollywood.screenshot.png')


if __name__ == "__main__":
    player.play('https://youtu.be/DLzxrzFCyOs')
    player.wait_for_playback()
