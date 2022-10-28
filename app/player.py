import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True,
                 input_vo_keyboard=True)


# player.fullscreen = True
# player.loop_playlist = 'inf'
player['vo'] = 'gpu'


@player.property_observer('time-pos')
def time_observer(_name, value):
    if value is not None:
        print('Now playing at {:.2f}s'.format(value))


@player.on_key_press('q')
def my_q_binding():
    print('THERE IS NO ESCAPE')


@player.on_key_press('s')
def my_s_binding():
    pillow_img = player.screenshot_raw()
    pillow_img.save('hollywood.screenshot.png')
