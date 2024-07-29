tira1 = 0
tira2 = 0
tira3 = 0

def on_forever():
    global tira1, tira2, tira3
    tira1 = pins.digital_read_pin(DigitalPin.P1)
    tira2 = pins.digital_read_pin(DigitalPin.P8)
    tira3 = pins.digital_read_pin(DigitalPin.P2)
    if tira1 or (tira2 or tira3):
        basic.pause(30)
        tira1 = pins.digital_read_pin(DigitalPin.P1)
        tira2 = pins.digital_read_pin(DigitalPin.P8)
        tira3 = pins.digital_read_pin(DigitalPin.P2)
        if tira1 == 0 and (tira2 == 0 and tira3 == 1):
            music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 0 and (tira2 == 1 and tira3 == 0):
            music.play(music.tone_playable(294, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 0 and (tira2 == 1 and tira3 == 1):
            music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 1 and (tira2 == 0 and tira3 == 0):
            music.play(music.tone_playable(349, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 1 and (tira2 == 0 and tira3 == 1):
            music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 1 and (tira2 == 1 and tira3 == 0):
            music.play(music.tone_playable(440, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
        if tira1 == 1 and (tira2 == 1 and tira3 == 1):
            music.play(music.tone_playable(494, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
