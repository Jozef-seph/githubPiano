# Piano Learning Program 🎹

def piano_layout():
    print("🎵 Welcome upcoming pianist!")
    print("This program will help you learn how to play the piano.")

# Chromatic notes repeated to avoid index wrapping
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] * 2

# Step patterns for each scale
scale_patterns = {
    "major": ["whole", "whole", "half", "whole", "whole", "whole", "half"],
    "minor": ["whole", "half", "whole", "whole", "half", "whole", "whole"],
    "diminished": ["whole", "half", "whole", "half", "whole", "half", "whole"]
}

# Chord qualities and Roman numerals
chord_qualities_map = {
    "major": ["major", "minor", "minor", "major", "major", "minor", "diminished"],
    "minor": ["minor", "diminished", "major", "minor", "minor", "major", "major"],
    "diminished": ["diminished"] * 7
}

roman_numerals_map = {
    "major": ["I", "ii", "iii", "IV", "V", "vi", "vii°"],
    "minor": ["i", "ii°", "III", "iv", "v", "VI", "VII"],
    "diminished": ["i°", "ii°", "iii°", "iv°", "v°", "vi°", "vii°"]
}

# Function to generate a scale
def generate_scale(start_note, scale_type):
    pattern = scale_patterns.get(scale_type)
    if not pattern or start_note not in notes:
        print("Invalid note or scale.")
        return []
    
    scale = [start_note]
    index = notes.index(start_note)

    for step in pattern:
        if step == "whole":
            index += 2
        elif step == "half":
            index += 1
        scale.append(notes[index])
    return scale

# Function to get triad notes
def get_chord_notes(scale, degree):
    root = scale[degree]
    third = scale[(degree + 2) % 7]
    fifth = scale[(degree + 4) % 7]
    return [root, third, fifth]
def passing_chords_for_scale(scale_type, scale, chord_qualities):
    print(f"\n🎶 Passing Chords for {scale_type.capitalize()} Scale")
    
    passing_chords_map = {
        "major": {
            1: ["Chromatic Passing: C - C# - D", "Diatonic Passing: C - Dm - G", "ii-V-I: Dm7 - G7 - Cmaj7", 
                "iii-VI-ii-V: Em - Am - Dm - G", "I-vi-IV-V: C - Am - F - G", "Circle of Fifths: C - F - Bb - Eb"],
            2: ["Chromatic Passing: D - D# - E", "Diatonic Passing: D - G - C", "ii-V-I: Dm7 - G7 - Cmaj7", 
                "iii-VI-ii-V: F - Dm - G7 - Cmaj7", "I-vi-IV-V: Dm - G - C", "Circle of Fifths: D - G - C - F"],
            3: ["Chromatic Passing: E - F - F#", "Diatonic Passing: Em - G - D", "ii-V-I: F#m7b5 - B7 - Emaj7", 
                "iii-VI-ii-V: Em - C - Dm - G7", "I-vi-IV-V: G - Em - C - D", "Circle of Fifths: E - A - D - G"],
            4: ["Chromatic Passing: F - F# - G", "Diatonic Passing: F - C - G", "ii-V-I: Gm7 - C7 - Fmaj7", 
                "iii-VI-ii-V: C - Em - Dm - G", "I-vi-IV-V: F - C - G - Am", "Circle of Fifths: F - Bb - Eb - Ab"],
            5: ["Chromatic Passing: G - G# - A", "Diatonic Passing: G - C - F", "ii-V-I: Am7 - D7 - Gmaj7", 
                "iii-VI-ii-V: C - G - Dm - G7", "I-vi-IV-V: G - Em - C - D", "Circle of Fifths: G - C - F - Bb"],
            6: ["Chromatic Passing: A - A# - B", "Diatonic Passing: Am - Dm - G", "ii-V-I: Bm7b5 - E7 - Am", 
                "iii-VI-ii-V: Em - Am - Dm - G", "I-vi-IV-V: A - D - G - C", "Circle of Fifths: A - D - G - C"],
            7: ["Chromatic Passing: B - C - C#", "Diatonic Passing: Bdim - E - A", "ii-V-I: Bdim - E7 - Am", 
                "iii-VI-ii-V: F#m - G - Am - D", "I-vi-IV-V: Bdim - Em - A - D", "Circle of Fifths: B - F# - D - A"]
        },
        "minor": {
            1: ["Chromatic Passing: Am - A# - B", "Diatonic Passing: Am - Dm - E", "ii-V-i: Bdim7 - E7 - Am", 
                "iii-VI-ii-V: Em - G - Am - Dm", "I-vi-IV-V: Am - F - G - E", "Circle of Fifths: Am - Dm - G - C"],
            2: ["Chromatic Passing: B - B# - C", "Diatonic Passing: Bdim - F - C", "ii°-V-i: Bdim7 - E7 - Am", 
                "iii-VI-ii-V: Em - Dm - G7 - C", "I-vi-IV-V: Bdim - Em - G - A", "Circle of Fifths: Bdim - F - Bb"],
            3: ["Chromatic Passing: C - C# - D", "Diatonic Passing: C - Em - G", "ii-V-i: C - G - Am", 
                "iii-VI-ii-V: Em - F - G - Am", "I-vi-IV-V: C - G - Am - F", "Circle of Fifths: C - F - Bb - Eb"],
            4: ["Chromatic Passing: D - D# - E", "Diatonic Passing: Dm - G - C", "ii-V-i: Dm7 - G7 - Am", 
                "iii-VI-ii-V: C - Em - Dm - G", "I-vi-IV-V: Dm - G - C - Am", "Passing to IV: Am - C#dim - Dm"],
            5: ["Chromatic Passing: E - F - F#", "Diatonic Passing: Em - B - F#", "ii-V-i: Em7 - B7 - Am", 
                "iii-VI-ii-V: G - Am - Dm - G", "I-vi-IV-V: Em - Am - Dm - G", "Circle of Fifths: E - A - D - G"],
            6: ["Chromatic Passing: F - F# - G", "Diatonic Passing: F - Dm - Am", "ii-V-i: F - C - Gm", 
                "iii-VI-ii-V: F - Dm - G7 - C", "I-vi-IV-V: F - C - G - Am", "Circle of Fifths: F - Bb - Eb - Ab"],
            7: ["Chromatic Passing: G - G# - A", "Diatonic Passing: G - C - F", "ii-V-i: G - C - Gm", 
                "iii-VI-ii-V: G - Am - Dm - C", "I-vi-IV-V: G - C - Dm - Em", "Circle of Fifths: G - D - A - E"]
        },
        "diminished": {
            1: ["Chromatic Passing: i° - i°# - ii°", "Diatonic Passing: i° - iii° - vi°", "ii°-V-i°: ii°7 - V7 - i°7", 
                "iii-VI-ii-V: vi° - Dm - F7 - Cmaj7", "Circle of Fifths: i° - iv - vi - vii°"],
            2: ["Chromatic Passing: ii° - ii°# - iii°", "Diatonic Passing: ii° - V - vi", "ii°-V-i: ii°7 - V7 - i°", 
                "iii-VI-ii-V: iv° - C - Dm7 - G"],
            3: ["Chromatic Passing: iii° - iii°# - iv°", "Diatonic Passing: iii° - ii° - V", "ii-V-i: iii° - V7 - i°", 
                "iii-VI-ii-V: iii° - vi° - Dm7 - G"],
            4: ["Chromatic Passing: iv° - iv°# - v°", "Diatonic Passing: iv° - V - i", "ii-V-i: iv° - V - i°", 
                "iii-VI-ii-V: iv° - Dm - G7 - Am"],
            5: ["Chromatic Passing: v° - v°# - vi°", "Diatonic Passing: v° - ii - vii°", "ii-V-i°: v° - ii°7 - i°", 
                "iii-VI-ii-V: vi° - G7 - C - Em"],
            6: ["Chromatic Passing: vi° - vi°# - vii°", "Diatonic Passing: vi° - ii - vi", "ii-V-i: vi° - ii°7 - V", 
                "iii-VI-ii-V: vii° - Em - A7 - Dm"],
            7: ["Chromatic Passing: vii° - vii°# - i°", "Diatonic Passing: vii° - ii - V", "ii-V-i°: vii° - V - i°", 
                "iii-VI-ii-V: vii° - G7 - Am - Dm"]
        }
    }

    # For each chord in the scale, show passing chords
    for i, chord in enumerate(scale):
        print(f"\nPassing Chords to {chord} ({chord_qualities[i]}):")
        for passing_chord in passing_chords_map[scale_type][i + 1]:
            print(f"- {passing_chord}")

# Function to teach passing chords
def passing_chords():
    print("\n🎶 Passing Chords in Music Theory")
    print("Passing chords connect chords smoothly, add tension, or create motion.")
    print("They can be chromatic (outside the key) or diatonic (inside the key).")
    
    print("\n🎵 Types of Passing Chords:")
    print("1. Chromatic Passing Chord: C - C# - D")
    print("2. Diatonic Passing Chord: C - Dm - G")
    print("3. ii–V–I Progression: Dm7 - G7 - Cmaj7 (classic jazz)")
    print("4. Circle of Fifths: Dm - G - C - F - Bb - etc.")
    print("5. Circle of Fourths: C - F - Bb - Eb - etc.")
    print("6. Passing to IV chord: C - Em - F (I - III - IV)")

    play = input("\nDo you want to explore a type of passing chord? (yes/no): ").lower()
    
    if play == "yes":
        print("\nChoose a passing technique:")
        print("1. Chromatic")
        print("2. Diatonic")
        print("3. ii–V–I")
        print("4. Circle of Fifths")
        print("5. Circle of Fourths")
        print("6. Passing to IV chord")
        
        choice = input("Enter 1-6: ")
        
        if choice == "1":
            print("\n🎵 Chromatic Passing Example: C - C# - D - G")
        elif choice == "2":
            print("\n🎵 Diatonic Passing Example: C - Dm - Em - F")
        elif choice == "3":
            print("\n🎵 ii–V–I Progression in C: Dm7 - G7 - Cmaj7")
        elif choice == "4":
            print("\n🎵 Circle of Fifths: Dm - G - C - F - Bb - Eb")
        elif choice == "5":
            print("\n🎵 Circle of Fourths: C - F - Bb - Eb - Ab")
        elif choice == "6":
            print("\n🎵 Passing to IV chord: C - Em - F (I - III - IV)")
        else:
            print("Invalid choice.")
    else:
        print("No worries! Come back when you’re ready to pass 🎶")

# Begin the program
piano_layout()

# Get root note from user
start_note = input("Enter a root note: ").upper()
while start_note not in notes:
    start_note = input("Invalid input. Please enter a valid note (C, C#, D, D#, E, F, F#, G, G#, A, A#, B): ").upper()

# Get scale type
scale_type = input("Choose a scale type (major, minor, diminished): ").lower()

# Generate scale
scale = generate_scale(start_note, scale_type)

if not scale:
    exit()

print(f"\n🎼 {start_note} {scale_type.capitalize()} Scale: {' - '.join(scale)}")

# Ask if user wants chords
ask_chords = input("\nWould you like to see the chords for this scale? (yes/no): ").lower()

if ask_chords == "yes":
    print(f"\n🎹 Chords in the {start_note} {scale_type} scale:\n")
    chord_qualities = chord_qualities_map[scale_type]
    roman_numerals = roman_numerals_map[scale_type]

    for i in range(7):
        chord_name = f"{scale[i]} {chord_qualities[i]}"
        chord_notes = get_chord_notes(scale, i)
        roman = roman_numerals[i]
        print(f"{roman} - {chord_name} ➤ Notes: {', '.join(chord_notes)}")

    # Ask about passing chords
    ask_passing = input("\nWould you like to learn about passing chords? (yes/no): ").lower()
    if ask_passing == "yes":
        passing_chords()
else:
    print("No problem! Just showing the scale.")

