#This file/class contains references for the ease of use/rewriting#

class references():
    def styleSheet(self, s_type): #Used to replace the huge parts of styleSheets setting
        if s_type == "mainButton":
            return "QPushButton{font: 18pt \"Orbitron\"; font-weight: bold; background-color:rgb(54, 75, 182); border: none; border-bottom: 2px solid rgb(34, 48, 116); border-radius: 8px; color: rgb(18,18,18);} QPushButton:hover{font: 18pt \"Orbitron\"; font-weight: bold; background-color: rgb(62, 87, 212); border: none; border-bottom: 2px solid rgb(34, 48, 116); color: rgb(18, 18, 18);} QPushButton:pressed{font: 18pt \"Orbitron\"; font-weight: bold; background-color: rgb(38, 55, 131); border: none; border-top: 2px solid rgb(34, 48, 116); color: rgb(18, 18, 18);}"
        if s_type == "smallPlayButton":
            return "QPushButton{background-color:rgb(54, 75, 182); border: none; border-bottom: 1px solid rgb(34, 48, 116); border-radius: 4px; color: rgb(18,18,18);} QPushButton:hover{background-color: rgb(62, 87, 212); border: none; border-bottom: 1px solid rgb(34, 48, 116); color: rgb(18, 18, 18);} QPushButton:pressed{background-color: rgb(38, 55, 131); border: none; border-top: 1px solid rgb(34, 48, 116); color: rgb(18, 18, 18);}"
        if s_type == "secondaryButton":
            return "QPushButton{font: 18pt \"Orbitron\"; font-weight: bold; background-color: rgb(230, 168, 106); border: none; border-bottom: 2px solid rgb(208, 122, 36); border-radius: 8px; color: rgb(18, 18, 18);} QPushButton:hover{font: 18pt \"Orbitron\"; font-weight: bold; background-color: rgb(234, 182, 130); border: none; border-bottom: 2px solid rgb(208, 122, 36); color: rgb(18, 18, 18);} QPushButton:pressed{font: 18pt \"Orbitron\"; font-weight: bold; background-color: rgb(220, 139, 58); border: none; border-top: 2px solid rgb(208, 122, 36); color: rgb(18, 18, 18);}"
        if s_type == "sysButton":
            return "QPushButton{background-color: rgb(18, 18, 18); border: none;} QPushButton:hover{background-color: rgb(34, 34, 34); border: none;} QPushButton:pressed{background-color: rgb(39, 39, 39); border: none;}"
        if s_type == "sysBlack":
            return "background-color: rgb(18, 18, 18);"
        if s_type == "darkGray":
            return "background-color: rgb(34, 34, 34);"
        if s_type == "darkBlueGray":
            return "background-color: rgb(31, 41, 51);"
        if s_type == "midBlueGray":
            return "background-color: rgb(50, 63, 75);"
        if s_type == "radioButton":
            return "QRadioButton::indicator{image: url(assets/rbUnselected.png);}QRadioButton::indicator::unchecked{image: url(assets/rbUnselected.png);}QRadioButton::indicator::checked{image: url(assets/rbSelected.png);}"
        if s_type == "shadow":
            return "color: rgb(26, 26, 26);"
        if s_type == "grayText":
            return "font: 75 12pt \"Orbitron\"; color: rgb(123, 135, 148);"
        if s_type == "smallgrayText":
            return "font: 10pt \"Orbitron\"; color: rgb(123, 135, 148);"
        if s_type == "whiteText":
            return "font: 50 16pt \"Orbitron\"; color: rgb(245, 247, 250);"
    def previewSounds(self,i_type,t_num,prog = 0):
        #i_type = instrument type, prog = song mood/chord progression, t_num = track number
        drumlist = ["assets/audio/drums/preview/p_drum_4floor.wav","assets/audio/drums/preview/p_drum_heavier.wav",
                    "assets/audio/drums/preview/p_drum_clapupbeat.wav","assets/audio/drums/preview/p_drum_complex.wav"]
        #[prog][t_num] => happy, dark, hopeful
        bassList = [["assets/audio/chordBased/happy/bass/preview/p_hap_bass_long.wav","assets/audio/chordBased/happy/bass/preview/p_hap_bass_rolling.wav",
                     "assets/audio/chordBased/happy/bass/preview/p_hap_bass_316.wav","assets/audio/chordBased/happy/bass/preview/p_hap_bass_offbeat.wav"],
                    ["assets/audio/chordBased/dark/bass/preview/p_dark_bass_long.wav","assets/audio/chordBased/dark/bass/preview/p_dark_bass_rolling.wav",
                     "assets/audio/chordBased/dark/bass/preview/p_dark_bass_316.wav","assets/audio/chordBased/dark/bass/preview/p_dark_bass_offbeat.wav"],
                    ["assets/audio/chordBased/hopeful/bass/preview/p_hope_bass_long.wav","assets/audio/chordBased/hopeful/bass/preview/p_hope_bass_rolling.wav",
                     "assets/audio/chordBased/hopeful/bass/preview/p_hope_bass_316.wav","assets/audio/chordBased/hopeful/bass/preview/p_hope_bass_offbeat.wav"]]
        padList = [["assets/audio/chordBased/happy/pad/preview/p_hap_pad_strings.wav",
                    "assets/audio/chordBased/happy/pad/preview/p_hap_pad_smooth.wav",
                     "assets/audio/chordBased/happy/pad/preview/p_hap_pad_fuzzy.wav",
                    "assets/audio/chordBased/happy/pad/preview/p_hap_pad_breathy.wav"],
                    ["assets/audio/chordBased/dark/pad/preview/p_dark_pad_strings.wav",
                     "assets/audio/chordBased/dark/pad/preview/p_dark_pad_smooth.wav",
                     "assets/audio/chordBased/dark/pad/preview/p_dark_pad_fuzzy.wav",
                     "assets/audio/chordBased/dark/pad/preview/p_dark_pad_breathy.wav"],
                    ["assets/audio/chordBased/hopeful/pad/preview/p_hope_pad_strings.wav",
                     "assets/audio/chordBased/hopeful/pad/preview/p_hope_pad_smooth.wav",
                     "assets/audio/chordBased/hopeful/pad/preview/p_hope_pad_fuzzy.wav",
                     "assets/audio/chordBased/hopeful/pad/preview/p_hope_pad_breathy.wav"]]
        chordList = [["assets/audio/chordBased/happy/chords/preview/p_hap_chord_synco.wav",
                    "assets/audio/chordBased/happy/chords/preview/p_hap_chord_bouncy.wav",
                    "assets/audio/chordBased/happy/chords/preview/p_hap_chord_longer.wav",
                    "assets/audio/chordBased/happy/chords/preview/p_hap_chord_16tension.wav"],
                   ["assets/audio/chordBased/dark/chords/preview/p_dark_chord_synco.wav",
                    "assets/audio/chordBased/dark/chords/preview/p_dark_chord_bouncy.wav",
                    "assets/audio/chordBased/dark/chords/preview/p_dark_chord_longer.wav",
                    "assets/audio/chordBased/dark/chords/preview/p_dark_chord_16tension.wav"],
                   ["assets/audio/chordBased/hopeful/chords/preview/p_hope_chord_synco.wav",
                    "assets/audio/chordBased/hopeful/chords/preview/p_hope_chord_bouncy.wav",
                    "assets/audio/chordBased/hopeful/chords/preview/p_hope_chord_longer.wav",
                    "assets/audio/chordBased/hopeful/chords/preview/p_hope_chord_16tension.wav"]]
        if i_type == 0: #Drums
            return drumlist[t_num]
        if i_type == 1: #Bass
            return bassList[prog][t_num]
        if i_type == 2: #Pad
            return padList[prog][t_num]
        if i_type == 3: #Chords
            return chordList[prog][t_num]
    def finalSounds(self,i_type,t_num,prog = 0):
        # i_type = instrument type, prog = song mood/chord progression, t_num = track number
        drumlist = ["assets/audio/drums/final/drum_4floor.wav", "assets/audio/drums/final/drum_heavier.wav",
                    "assets/audio/drums/final/drum_clapupbeat.wav", "assets/audio/drums/final/drum_complex.wav"]
        # [prog][t_num] => happy, dark, hopeful
        bassList = [["assets/audio/chordBased/happy/bass/final/hap_bass_long.wav",
                     "assets/audio/chordBased/happy/bass/final/hap_bass_rolling.wav",
                     "assets/audio/chordBased/happy/bass/final/hap_bass_316.wav",
                     "assets/audio/chordBased/happy/bass/final/hap_bass_offbeat.wav"],
                    ["assets/audio/chordBased/dark/bass/final/dark_bass_long.wav",
                     "assets/audio/chordBased/dark/bass/final/dark_bass_rolling.wav",
                     "assets/audio/chordBased/dark/bass/final/dark_bass_316.wav",
                     "assets/audio/chordBased/dark/bass/final/dark_bass_offbeat.wav"],
                    ["assets/audio/chordBased/hopeful/bass/final/hope_bass_long.wav",
                     "assets/audio/chordBased/hopeful/bass/final/hope_bass_rolling.wav",
                     "assets/audio/chordBased/hopeful/bass/final/hope_bass_316.wav",
                     "assets/audio/chordBased/hopeful/bass/final/hope_bass_offbeat.wav"]]
        padList = [["assets/audio/chordBased/happy/pad/final/hap_pad_strings.wav",
                    "assets/audio/chordBased/happy/pad/final/hap_pad_smooth.wav",
                    "assets/audio/chordBased/happy/pad/final/hap_pad_fuzzy.wav",
                    "assets/audio/chordBased/happy/pad/final/hap_pad_breathy.wav"],
                   ["assets/audio/chordBased/dark/pad/final/dark_pad_strings.wav",
                    "assets/audio/chordBased/dark/pad/final/dark_pad_smooth.wav",
                    "assets/audio/chordBased/dark/pad/final/dark_pad_fuzzy.wav",
                    "assets/audio/chordBased/dark/pad/final/dark_pad_breathy.wav"],
                   ["assets/audio/chordBased/hopeful/pad/final/hope_pad_strings.wav",
                    "assets/audio/chordBased/hopeful/pad/final/hope_pad_smooth.wav",
                    "assets/audio/chordBased/hopeful/pad/final/hope_pad_fuzzy.wav",
                    "assets/audio/chordBased/hopeful/pad/final/hope_pad_breathy.wav"]]
        chordList = [["assets/audio/chordBased/happy/chords/final/hap_chord_synco.wav",
                      "assets/audio/chordBased/happy/chords/final/hap_chord_bouncy.wav",
                      "assets/audio/chordBased/happy/chords/final/hap_chord_longer.wav",
                      "assets/audio/chordBased/happy/chords/final/hap_chord_16tension.wav"],
                     ["assets/audio/chordBased/dark/chords/final/dark_chord_synco.wav",
                      "assets/audio/chordBased/dark/chords/final/dark_chord_bouncy.wav",
                      "assets/audio/chordBased/dark/chords/final/dark_chord_longer.wav",
                      "assets/audio/chordBased/dark/chords/final/dark_chord_16tension.wav"],
                     ["assets/audio/chordBased/hopeful/chords/final/hope_chord_synco.wav",
                      "assets/audio/chordBased/hopeful/chords/final/hope_chord_bouncy.wav",
                      "assets/audio/chordBased/hopeful/chords/final/hope_chord_longer.wav",
                      "assets/audio/chordBased/hopeful/chords/final/hope_chord_16tension.wav"]]
        if i_type == 0: #Drums
            return drumlist[t_num]
        if i_type == 1: #Bass
            return bassList[prog][t_num]
        if i_type == 2: #Pad
            return padList[prog][t_num]
        if i_type == 3: #Chords
            return chordList[prog][t_num]