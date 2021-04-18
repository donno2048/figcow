def process(message: str, wrapping: int) -> tuple:
    lines, index = [""] * 6, 0
    for l in message:
        if l == "a":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "  __ _ "
            lines[2 + index * 6] += " / _` |"
            lines[3 + index * 6] += "| (_| |"
            lines[4 + index * 6] += " \\__,_|"
            lines[5 + index * 6] += "       "
        elif l == "b":
            lines[0 + index * 6] += " _     "
            lines[1 + index * 6] += "| |__  "
            lines[2 + index * 6] += "| '_ \\ "
            lines[3 + index * 6] += "| |_) |"
            lines[4 + index * 6] += "|_.__/ "
            lines[5 + index * 6] += "       "
        elif l == "c":
            lines[0 + index * 6] += "      "
            lines[1 + index * 6] += "  ___ "
            lines[2 + index * 6] += " / __|"
            lines[3 + index * 6] += "| (__ "
            lines[4 + index * 6] += " \\___|"
            lines[5 + index * 6] += "      "
        elif l == "d":
            lines[0 + index * 6] += "     _ "
            lines[1 + index * 6] += "  __| |"
            lines[2 + index * 6] += " / _` |"
            lines[3 + index * 6] += "| (_| |"
            lines[4 + index * 6] += " \\__,_|"
            lines[5 + index * 6] += "       "
        elif l == "e":
            lines[0 + index * 6] += "      "
            lines[1 + index * 6] += "  ___ "
            lines[2 + index * 6] += " / _ \\"
            lines[3 + index * 6] += "|  __/"
            lines[4 + index * 6] += " \\___|"
            lines[5 + index * 6] += "      "
        elif l == "f":
            lines[0 + index * 6] += "  __ "
            lines[1 + index * 6] += " / _|"
            lines[2 + index * 6] += "| |_ "
            lines[3 + index * 6] += "|  _|"
            lines[4 + index * 6] += "|_|  "
            lines[5 + index * 6] += "     "
        elif l == "g":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "  __ _ "
            lines[2 + index * 6] += " / _` |"
            lines[3 + index * 6] += "| (_| |"
            lines[4 + index * 6] += " \\__, |"
            lines[5 + index * 6] += " |___/ "
        elif l == "h":
            lines[0 + index * 6] += " _     "
            lines[1 + index * 6] += "| |__  "
            lines[2 + index * 6] += "| '_ \\ "
            lines[3 + index * 6] += "| | | |"
            lines[4 + index * 6] += "|_| |_|"
            lines[5 + index * 6] += "       "
        elif l == "i":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "(_)"
            lines[2 + index * 6] += "| |"
            lines[3 + index * 6] += "| |"
            lines[4 + index * 6] += "|_|"
            lines[5 + index * 6] += "   "
        elif l == "j":
            lines[0 + index * 6] += "   _ "
            lines[1 + index * 6] += "  (_)"
            lines[2 + index * 6] += "  | |"
            lines[3 + index * 6] += "  | |"
            lines[4 + index * 6] += " _/ |"
            lines[5 + index * 6] += "|__/ "
        elif l == "k":
            lines[0 + index * 6] += " _    "
            lines[1 + index * 6] += "| | __"
            lines[2 + index * 6] += "| |/ /"
            lines[3 + index * 6] += "|   < "
            lines[4 + index * 6] += "|_|\\_\\"
            lines[5 + index * 6] += "      "
        elif l == "l":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "| |"
            lines[2 + index * 6] += "| |"
            lines[3 + index * 6] += "| |"
            lines[4 + index * 6] += "|_|"
            lines[5 + index * 6] += "   "
        elif l == "m":
            lines[0 + index * 6] += "           "
            lines[1 + index * 6] += " _ __ ___  "
            lines[2 + index * 6] += "| '_ ` _ \\ "
            lines[3 + index * 6] += "| | | | | |"
            lines[4 + index * 6] += "|_| |_| |_|"
            lines[5 + index * 6] += "           "
        elif l == "n":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += " _ __  "
            lines[2 + index * 6] += "| '_ \\ "
            lines[3 + index * 6] += "| | | |"
            lines[4 + index * 6] += "|_| |_|"
            lines[5 + index * 6] += "       "
        elif l == "o":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "  ___  "
            lines[2 + index * 6] += " / _ \\ "
            lines[3 + index * 6] += "| (_) |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "p":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += " _ __  "
            lines[2 + index * 6] += "| '_ \\ "
            lines[3 + index * 6] += "| |_) |"
            lines[4 + index * 6] += "| .__/ "
            lines[5 + index * 6] += "|_|    "
        elif l == "q":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "  __ _ "
            lines[2 + index * 6] += " / _` |"
            lines[3 + index * 6] += "| (_| |"
            lines[4 + index * 6] += " \\__, |"
            lines[5 + index * 6] += "    |_|"
        elif l == "r":
            lines[0 + index * 6] += "      "
            lines[1 + index * 6] += " _ __ "
            lines[2 + index * 6] += "| '__|"
            lines[3 + index * 6] += "| |   "
            lines[4 + index * 6] += "|_|   "
            lines[5 + index * 6] += "      "
        elif l == "s":
            lines[0 + index * 6] += "     "
            lines[1 + index * 6] += " ___ "
            lines[2 + index * 6] += "/ __|"
            lines[3 + index * 6] += "\\__ \\"
            lines[4 + index * 6] += "|___/"
            lines[5 + index * 6] += "     "
        elif l == "t":
            lines[0 + index * 6] += " _   "
            lines[1 + index * 6] += "| |_ "
            lines[2 + index * 6] += "| __|"
            lines[3 + index * 6] += "| |_ "
            lines[4 + index * 6] += " \\__|"
            lines[5 + index * 6] += "     "
        elif l == "u":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += " _   _ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\__,_|"
            lines[5 + index * 6] += "       "
        elif l == "v":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "__   __"
            lines[2 + index * 6] += "\\ \\ / /"
            lines[3 + index * 6] += " \\ V / "
            lines[4 + index * 6] += "  \\_/  "
            lines[5 + index * 6] += "       "
        elif l == "w":
            lines[0 + index * 6] += "          "
            lines[1 + index * 6] += "__      __"
            lines[2 + index * 6] += "\\ \\ /\\ / /"
            lines[3 + index * 6] += " \\ V  V / "
            lines[4 + index * 6] += "  \\_/\\_/  "
            lines[5 + index * 6] += "          "
        elif l == "x":
            lines[0 + index * 6] += "      "
            lines[1 + index * 6] += "__  __"
            lines[2 + index * 6] += "\\ \\/ /"
            lines[3 + index * 6] += " >  < "
            lines[4 + index * 6] += "/_/\\_\\"
            lines[5 + index * 6] += "      "
        elif l == "y":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += " _   _ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\__, |"
            lines[5 + index * 6] += " |___/ "
        elif l == "z":
            lines[0 + index * 6] += "     "
            lines[1 + index * 6] += " ____"
            lines[2 + index * 6] += "|_  /"
            lines[3 + index * 6] += " / / "
            lines[4 + index * 6] += "/___|"
            lines[5 + index * 6] += "     "
        elif l == "A":
            lines[0 + index * 6] += "    _    "
            lines[1 + index * 6] += "   / \\   "
            lines[2 + index * 6] += "  / _ \\  "
            lines[3 + index * 6] += " / ___ \\ "
            lines[4 + index * 6] += "/_/   \\_\\"
            lines[5 + index * 6] += "         "
        elif l == "B":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "| __ ) "
            lines[2 + index * 6] += "|  _ \\ "
            lines[3 + index * 6] += "| |_) |"
            lines[4 + index * 6] += "|____/ "
            lines[5 + index * 6] += "       "
        elif l == "C":
            lines[0 + index * 6] += "  ____ "
            lines[1 + index * 6] += " / ___|"
            lines[2 + index * 6] += "| |    "
            lines[3 + index * 6] += "| |___ "
            lines[4 + index * 6] += " \\____|"
            lines[5 + index * 6] += "       "
        elif l == "D":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "|  _ \\ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += "|____/ "
            lines[5 + index * 6] += "       "
        elif l == "E":
            lines[0 + index * 6] += " _____ "
            lines[1 + index * 6] += "| ____|"
            lines[2 + index * 6] += "|  _|  "
            lines[3 + index * 6] += "| |___ "
            lines[4 + index * 6] += "|_____|"
            lines[5 + index * 6] += "       "
        elif l == "F":
            lines[0 + index * 6] += " _____ "
            lines[1 + index * 6] += "|  ___|"
            lines[2 + index * 6] += "| |_   "
            lines[3 + index * 6] += "|  _|  "
            lines[4 + index * 6] += "|_|    "
            lines[5 + index * 6] += "       "
        elif l == "G":
            lines[0 + index * 6] += "  ____ "
            lines[1 + index * 6] += " / ___|"
            lines[2 + index * 6] += "| |  _ "
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\____|"
            lines[5 + index * 6] += "       "
        elif l == "H":
            lines[0 + index * 6] += " _   _ "
            lines[1 + index * 6] += "| | | |"
            lines[2 + index * 6] += "| |_| |"
            lines[3 + index * 6] += "|  _  |"
            lines[4 + index * 6] += "|_| |_|"
            lines[5 + index * 6] += "       "
        elif l == "I":
            lines[0 + index * 6] += " ___ "
            lines[1 + index * 6] += "|_ _|"
            lines[2 + index * 6] += " | | "
            lines[3 + index * 6] += " | | "
            lines[4 + index * 6] += "|___|"
            lines[5 + index * 6] += "     "
        elif l == "J":
            lines[0 + index * 6] += "     _ "
            lines[1 + index * 6] += "    | |"
            lines[2 + index * 6] += " _  | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "K":
            lines[0 + index * 6] += " _  __"
            lines[1 + index * 6] += "| |/ /"
            lines[2 + index * 6] += "| ' / "
            lines[3 + index * 6] += "| . \\ "
            lines[4 + index * 6] += "|_|\\_\\"
            lines[5 + index * 6] += "      "
        elif l == "L":
            lines[0 + index * 6] += " _     "
            lines[1 + index * 6] += "| |    "
            lines[2 + index * 6] += "| |    "
            lines[3 + index * 6] += "| |___ "
            lines[4 + index * 6] += "|_____|"
            lines[5 + index * 6] += "       "
        elif l == "M":
            lines[0 + index * 6] += " __  __ "
            lines[1 + index * 6] += "|  \\/  |"
            lines[2 + index * 6] += "| |\\/| |"
            lines[3 + index * 6] += "| |  | |"
            lines[4 + index * 6] += "|_|  |_|"
            lines[5 + index * 6] += "        "
        elif l == "N":
            lines[0 + index * 6] += " _   _ "
            lines[1 + index * 6] += "| \\ | |"
            lines[2 + index * 6] += "|  \\| |"
            lines[3 + index * 6] += "| |\\  |"
            lines[4 + index * 6] += "|_| \\_|"
            lines[5 + index * 6] += "       "
        elif l == "O":
            lines[0 + index * 6] += "  ___  "
            lines[1 + index * 6] += " / _ \\ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "P":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "|  _ \\ "
            lines[2 + index * 6] += "| |_) |"
            lines[3 + index * 6] += "|  __/ "
            lines[4 + index * 6] += "|_|    "
            lines[5 + index * 6] += "       "
        elif l == "Q":
            lines[0 + index * 6] += "  ___  "
            lines[1 + index * 6] += " / _ \\ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\__\\_\\"
            lines[5 + index * 6] += "       "
        elif l == "R":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "|  _ \\ "
            lines[2 + index * 6] += "| |_) |"
            lines[3 + index * 6] += "|  _ < "
            lines[4 + index * 6] += "|_| \\_\\"
            lines[5 + index * 6] += "       "
        elif l == "S":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "/ ___| "
            lines[2 + index * 6] += "\\___ \\ "
            lines[3 + index * 6] += " ___) |"
            lines[4 + index * 6] += "|____/ "
            lines[5 + index * 6] += "       "
        elif l == "T":
            lines[0 + index * 6] += " _____ "
            lines[1 + index * 6] += "|_   _|"
            lines[2 + index * 6] += "  | |  "
            lines[3 + index * 6] += "  | |  "
            lines[4 + index * 6] += "  |_|  "
            lines[5 + index * 6] += "       "
        elif l == "U":
            lines[0 + index * 6] += " _   _ "
            lines[1 + index * 6] += "| | | |"
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "V":
            lines[0 + index * 6] += "__     __"
            lines[1 + index * 6] += "\\ \\   / /"
            lines[2 + index * 6] += " \\ \\ / / "
            lines[3 + index * 6] += "  \\ V /  "
            lines[4 + index * 6] += "   \\_/   "
            lines[5 + index * 6] += "         "
        elif l == "W":
            lines[0 + index * 6] += "__        __"
            lines[1 + index * 6] += "\\ \\      / /"
            lines[2 + index * 6] += " \\ \\ /\\ / / "
            lines[3 + index * 6] += "  \\ V  V /  "
            lines[4 + index * 6] += "   \\_/\\_/   "
            lines[5 + index * 6] += "            "
        elif l == "X":
            lines[0 + index * 6] += "__  __"
            lines[1 + index * 6] += "\\ \\/ /"
            lines[2 + index * 6] += " \\  / "
            lines[3 + index * 6] += " /  \\ "
            lines[4 + index * 6] += "/_/\\_\\"
            lines[5 + index * 6] += "      "
        elif l == "Y":
            lines[0 + index * 6] += "__   __"
            lines[1 + index * 6] += "\\ \\ / /"
            lines[2 + index * 6] += " \\ V / "
            lines[3 + index * 6] += "  | |  "
            lines[4 + index * 6] += "  |_|  "
            lines[5 + index * 6] += "       "
        elif l == "Z":
            lines[0 + index * 6] += " _____"
            lines[1 + index * 6] += "|__  /"
            lines[2 + index * 6] += "  / / "
            lines[3 + index * 6] += " / /_ "
            lines[4 + index * 6] += "/____|"
            lines[5 + index * 6] += "      "
        elif l == "`":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "( )"
            lines[2 + index * 6] += " \\|"
            lines[3 + index * 6] += "   "
            lines[4 + index * 6] += "   "
            lines[5 + index * 6] += "   "
        elif l == "1":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "/ |"
            lines[2 + index * 6] += "| |"
            lines[3 + index * 6] += "| |"
            lines[4 + index * 6] += "|_|"
            lines[5 + index * 6] += "   "
        elif l == "2":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "|___ \\ "
            lines[2 + index * 6] += "  __) |"
            lines[3 + index * 6] += " / __/ "
            lines[4 + index * 6] += "|_____|"
            lines[5 + index * 6] += "       "
        elif l == "3":
            lines[0 + index * 6] += " _____ "
            lines[1 + index * 6] += "|___ / "
            lines[2 + index * 6] += "  |_ \\ "
            lines[3 + index * 6] += " ___) |"
            lines[4 + index * 6] += "|____/ "
            lines[5 + index * 6] += "       "
        elif l == "4":
            lines[0 + index * 6] += " _  _   "
            lines[1 + index * 6] += "| || |  "
            lines[2 + index * 6] += "| || |_ "
            lines[3 + index * 6] += "|__   _|"
            lines[4 + index * 6] += "   |_|  "
            lines[5 + index * 6] += "        "
        elif l == "5":
            lines[0 + index * 6] += " ____  "
            lines[1 + index * 6] += "| ___| "
            lines[2 + index * 6] += "|___ \\ "
            lines[3 + index * 6] += " ___) |"
            lines[4 + index * 6] += "|____/ "
            lines[5 + index * 6] += "       "
        elif l == "6":
            lines[0 + index * 6] += "  __   "
            lines[1 + index * 6] += " / /_  "
            lines[2 + index * 6] += "| '_ \\ "
            lines[3 + index * 6] += "| (_) |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "7":
            lines[0 + index * 6] += " _____ "
            lines[1 + index * 6] += "|___  |"
            lines[2 + index * 6] += "   / / "
            lines[3 + index * 6] += "  / /  "
            lines[4 + index * 6] += " /_/   "
            lines[5 + index * 6] += "       "
        elif l == "8":
            lines[0 + index * 6] += "  ___  "
            lines[1 + index * 6] += " ( _ ) "
            lines[2 + index * 6] += " / _ \\ "
            lines[3 + index * 6] += "| (_) |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "9":
            lines[0 + index * 6] += "  ___  "
            lines[1 + index * 6] += " / _ \\ "
            lines[2 + index * 6] += "| (_) |"
            lines[3 + index * 6] += " \\__, |"
            lines[4 + index * 6] += "   /_/ "
            lines[5 + index * 6] += "       "
        elif l == "0":
            lines[0 + index * 6] += "  ___  "
            lines[1 + index * 6] += " / _ \\ "
            lines[2 + index * 6] += "| | | |"
            lines[3 + index * 6] += "| |_| |"
            lines[4 + index * 6] += " \\___/ "
            lines[5 + index * 6] += "       "
        elif l == "-":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "       "
            lines[2 + index * 6] += " _____ "
            lines[3 + index * 6] += "|_____|"
            lines[4 + index * 6] += "       "
            lines[5 + index * 6] += "       "
        elif l == "=":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += " _____ "
            lines[2 + index * 6] += "|_____|"
            lines[3 + index * 6] += "|_____|"
            lines[4 + index * 6] += "       "
            lines[5 + index * 6] += "       "
        elif l == "~":
            lines[0 + index * 6] += " /\\/|"
            lines[1 + index * 6] += "|/\\/ "
            lines[2 + index * 6] += "     "
            lines[3 + index * 6] += "     "
            lines[4 + index * 6] += "     "
            lines[5 + index * 6] += "     "
        elif l == "!":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "| |"
            lines[2 + index * 6] += "| |"
            lines[3 + index * 6] += "|_|"
            lines[4 + index * 6] += "(_)"
            lines[5 + index * 6] += "   "
        elif l == "@":
            lines[0 + index * 6] += "   ____  "
            lines[1 + index * 6] += "  / __ \\ "
            lines[2 + index * 6] += " / / _` |"
            lines[3 + index * 6] += "| | (_| |"
            lines[4 + index * 6] += " \\ \\__,_|"
            lines[5 + index * 6] += "  \\____/ "
        elif l == "#":
            lines[0 + index * 6] += "   _  _   "
            lines[1 + index * 6] += " _| || |_ "
            lines[2 + index * 6] += "|_  ..  _|"
            lines[3 + index * 6] += "|_      _|"
            lines[4 + index * 6] += "  |_||_|  "
            lines[5 + index * 6] += "          "
        elif l == "$":
            lines[0 + index * 6] += "  _  "
            lines[1 + index * 6] += " | | "
            lines[2 + index * 6] += "/ __)"
            lines[3 + index * 6] += "\\__ \\"
            lines[4 + index * 6] += "(   /"
            lines[5 + index * 6] += " |_| "
        elif l == "%":
            lines[0 + index * 6] += " _  __"
            lines[1 + index * 6] += "(_)/ /"
            lines[2 + index * 6] += "  / / "
            lines[3 + index * 6] += " / /_ "
            lines[4 + index * 6] += "/_/(_)"
            lines[5 + index * 6] += "      "
        elif l == "^":
            lines[0 + index * 6] += " /\\ "
            lines[1 + index * 6] += "|/\\|"
            lines[2 + index * 6] += "    "
            lines[3 + index * 6] += "    "
            lines[4 + index * 6] += "    "
            lines[5 + index * 6] += "    "
        elif l == "&":
            lines[0 + index * 6] += "  ___   "
            lines[1 + index * 6] += " ( _ )  "
            lines[2 + index * 6] += " / _ \\/\\"
            lines[3 + index * 6] += "| (_>  <"
            lines[4 + index * 6] += " \\___/\\/"
            lines[5 + index * 6] += "        "
        elif l == "*":
            lines[0 + index * 6] += "      "
            lines[1 + index * 6] += "__/\\__"
            lines[2 + index * 6] += "\\    /"
            lines[3 + index * 6] += "/_  _\\"
            lines[4 + index * 6] += "  \\/  "
            lines[5 + index * 6] += "      "
        elif l == "(":
            lines[0 + index * 6] += "  __"
            lines[1 + index * 6] += " / /"
            lines[2 + index * 6] += "| | "
            lines[3 + index * 6] += "| | "
            lines[4 + index * 6] += "| | "
            lines[5 + index * 6] += " \\_\\"
        elif l == ")":
            lines[0 + index * 6] += "__  "
            lines[1 + index * 6] += "\\ \\ "
            lines[2 + index * 6] += " | |"
            lines[3 + index * 6] += " | |"
            lines[4 + index * 6] += " | |"
            lines[5 + index * 6] += "/_/ "
        elif l == "_":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "       "
            lines[2 + index * 6] += "       "
            lines[3 + index * 6] += "       "
            lines[4 + index * 6] += " _____ "
            lines[5 + index * 6] += "|_____|"
        elif l == "+":
            lines[0 + index * 6] += "       "
            lines[1 + index * 6] += "   _   "
            lines[2 + index * 6] += " _| |_ "
            lines[3 + index * 6] += "|_   _|"
            lines[4 + index * 6] += "  |_|  "
            lines[5 + index * 6] += "       "
        elif l == "[":
            lines[0 + index * 6] += " __ "
            lines[1 + index * 6] += "| _|"
            lines[2 + index * 6] += "| | "
            lines[3 + index * 6] += "| | "
            lines[4 + index * 6] += "| | "
            lines[5 + index * 6] += "|__|"
        elif l == "]":
            lines[0 + index * 6] += " __ "
            lines[1 + index * 6] += "|_ |"
            lines[2 + index * 6] += " | |"
            lines[3 + index * 6] += " | |"
            lines[4 + index * 6] += " | |"
            lines[5 + index * 6] += "|__|"
        elif l == "\\":
            lines[0 + index * 6] += "__    "
            lines[1 + index * 6] += "\\ \\   "
            lines[2 + index * 6] += " \\ \\  "
            lines[3 + index * 6] += "  \\ \\ "
            lines[4 + index * 6] += "   \\_\\"
            lines[5 + index * 6] += "      "
        elif l == "{":
            lines[0 + index * 6] += "   __"
            lines[1 + index * 6] += "  / /"
            lines[2 + index * 6] += " | | "
            lines[3 + index * 6] += "< <  "
            lines[4 + index * 6] += " | | "
            lines[5 + index * 6] += "  \\_\\"
        elif l == "}":
            lines[0 + index * 6] += "__   "
            lines[1 + index * 6] += "\\ \\  "
            lines[2 + index * 6] += " | | "
            lines[3 + index * 6] += "  > >"
            lines[4 + index * 6] += " | | "
            lines[5 + index * 6] += "/_/  "
        elif l == "|":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "| |"
            lines[2 + index * 6] += "| |"
            lines[3 + index * 6] += "| |"
            lines[4 + index * 6] += "| |"
            lines[5 + index * 6] += "|_|"
        elif l == ";":
            lines[0 + index * 6] += "   "
            lines[1 + index * 6] += " _ "
            lines[2 + index * 6] += "(_)"
            lines[3 + index * 6] += " _ "
            lines[4 + index * 6] += "( )"
            lines[5 + index * 6] += "|/ "
        elif l == "'":
            lines[0 + index * 6] += " _ "
            lines[1 + index * 6] += "( )"
            lines[2 + index * 6] += "|/ "
            lines[3 + index * 6] += "   "
            lines[4 + index * 6] += "   "
            lines[5 + index * 6] += "   "
        elif l == ":":
            lines[0 + index * 6] += "   "
            lines[1 + index * 6] += " _ "
            lines[2 + index * 6] += "(_)"
            lines[3 + index * 6] += " _ "
            lines[4 + index * 6] += "(_)"
            lines[5 + index * 6] += "   "
        elif l == "\"":
            lines[0 + index * 6] += " _ _ "
            lines[1 + index * 6] += "( | )"
            lines[2 + index * 6] += " V V "
            lines[3 + index * 6] += "     "
            lines[4 + index * 6] += "     "
            lines[5 + index * 6] += "     "
        elif l == ",":
            lines[0 + index * 6] += "   "
            lines[1 + index * 6] += "   "
            lines[2 + index * 6] += "   "
            lines[3 + index * 6] += " _ "
            lines[4 + index * 6] += "( )"
            lines[5 + index * 6] += "|/ "
        elif l == ".":
            lines[0 + index * 6] += "   "
            lines[1 + index * 6] += "   "
            lines[2 + index * 6] += "   "
            lines[3 + index * 6] += " _ "
            lines[4 + index * 6] += "(_)"
            lines[5 + index * 6] += "   "
        elif l == "<":
            lines[0 + index * 6] += "  __"
            lines[1 + index * 6] += " / /"
            lines[2 + index * 6] += "/ / "
            lines[3 + index * 6] += "\\ \\ "
            lines[4 + index * 6] += " \\_\\"
            lines[5 + index * 6] += "    "
        elif l == ">":
            lines[0 + index * 6] += "__  "
            lines[1 + index * 6] += "\\ \\ "
            lines[2 + index * 6] += " \\ \\"
            lines[3 + index * 6] += " / /"
            lines[4 + index * 6] += "/_/ "
            lines[5 + index * 6] += "    "
        elif l == "/":
            lines[0 + index * 6] += "    __"
            lines[1 + index * 6] += "   / /"
            lines[2 + index * 6] += "  / / "
            lines[3 + index * 6] += " / /  "
            lines[4 + index * 6] += "/_/   "
            lines[5 + index * 6] += "      "
        elif l == "?":
            lines[0 + index * 6] += " ___ "
            lines[1 + index * 6] += "|__ \\"
            lines[2 + index * 6] += "  / /"
            lines[3 + index * 6] += " |_| "
            lines[4 + index * 6] += " (_) "
            lines[5 + index * 6] += "     "
        elif l == " ":
            lines[0 + index * 6] += "   "
            lines[1 + index * 6] += "   "
            lines[2 + index * 6] += "   "
            lines[3 + index * 6] += "   "
            lines[4 + index * 6] += "   "
            lines[5 + index * 6] += "   "
        if max(len(line) for line in lines[-6:]) + 10 > wrapping:
            lines.extend([""] * 6)
            index += 1
    return lines, max(len(line) for line in lines) + 1