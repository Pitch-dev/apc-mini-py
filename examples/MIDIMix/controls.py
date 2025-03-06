from akai_pro_py import controllers

# Define the MIDI Mix
# first argument: MIDI in
# second argument: MIDI out
midi_mix = controllers.MIDIMix('MIDI Mix MIDI 1', 'MIDI Mix MIDI 1')


@midi_mix.on_event
def on_event(event):  # Register event function
    if isinstance(event, controllers.MIDIMix.Knob):
        print(
            f"Knob {event.x},{event.y} was changed to {event.value} on "
            f"{event.controller.name}"
        )
    if isinstance(event, controllers.MIDIMix.Fader):
        print(
            f"Fader {event.fader_id} was changed to {event.value} on "
            f"{event.controller.name}"
        )
    if isinstance(event, controllers.MIDIMix.MuteButton):
        print(
            f"Mute Button {event.button_id} was changed to {event.state} on "
            f"{event.controller.name}"
        )
    if isinstance(event, controllers.MIDIMix.RecArmButton):
        print(
            f"Record Arm Button {event.button_id} was changed to {event.state}"
            f" on {event.controller.name}"
        )
    if isinstance(event, controllers.MIDIMix.SoloButton):
        print(
            f"Solo Button was changed to {event.state} on "
            f"{event.controller.name}"
        )
    if isinstance(event, controllers.MIDIMix.BankButton):
        print(
            f"Bank Button {event.button_id} was changed to {event.state} on "
            f"{event.controller.name}"
        )


midi_mix.start()  # Start event loop
