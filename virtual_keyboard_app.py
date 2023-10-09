import streamlit as st

# Define the virtual keyboard layout
keyboard_layout = [
    ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    ['C#', 'D#', 'F#', 'G#', 'A#'],
]

# Define a dictionary to map notes to Plaine and easie code
note_to_code = {
    'C': 'C',
    'C#': '^C',
    'D': 'D',
    'D#': '^D',
    'E': 'E',
    'F': 'F',
    'F#': '^F',
    'G': 'G',
    'G#': '^G',
    'A': 'A',
    'A#': '^A',
    'B': 'B',
}

st.title("Virtual Keyboard")

# Create a layout for the virtual keyboard
for row in keyboard_layout:
    for note in row:
        note_code = note_to_code.get(note, '')
        if note_code:
            button = st.button(note)
            if button:
                st.write(f"Plaine and easie code: `{note_code}`")

# Display a reset button
if st.button("Reset"):
    st.clear_cache()

