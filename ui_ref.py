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
            return "QRadioButton::indicator::unchecked{image: url(assets/rbUnselected.png);}QRadioButton::indicator::checked{image: url(assets/rbSelected.png);}"
        if s_type == "shadow":
            return "color: rgb(26, 26, 26);"
        if s_type == "grayText":
            return "font: 75 12pt \"Orbitron\"; color: rgb(123, 135, 148);"
        if s_type == "smallgrayText":
            return "font: 10pt \"Orbitron\"; color: rgb(123, 135, 148);"
        if s_type == "whiteText":
            return "font: 50 16pt \"Orbitron\"; color: rgb(245, 247, 250);"