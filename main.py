def main():
    filu = input("Anna filu: ") # C:\Users\kauha\Desktop\ttyyh18.json

    vikaRivi = False
    käyttäjät = dict()

    id = 0
    actor = ""
    date = ""
    text = ""

    for line in open(filu, 'r', encoding="utf8"):
        if vikaRivi and '"' not in line and id > 0:
            if actor in käyttäjät.keys():
                if type == "message":
                    käyttäjät[actor][0].append(text)
                    käyttäjät[actor][1].append(date)
            else:
                if type == "message":
                    käyttäjät[actor] = [[text],[date]]

            vikaRivi = False

        else:
            if '"' not in line:
                vikaRivi = True

            else:
                if line == '{':
                    continue

                else:
                    if '"id":' in line:
                        id = int(line[12:len(line)-2])
                        #print()
                        #print()
                        #print(id)
                    elif '"type":' in line:
                        type = line[15:len(line)-3]
                        #print(type)
                    elif '"date":' in line:
                        date = line[15:len(line) - 3]
                        #print(date)
                    elif '"from":' in line:
                        actor = line[15:len(line) - 3]
                        #print(actor)
                    elif '"actor":' in line:
                        actor = line[16:len(line) - 3]
                        #print(actor)
                    elif '"text":' in line:
                        text = line[15:len(line) - 2]
                        #print(text)

    while True:
        komento = input("> ")

        if komento == "nimi":
            nimi = input("Syötä henkilön nimi: ")

            if nimi in käyttäjät.keys():
                print("Henkilöllä on ", len(käyttäjät[nimi][0]), " viestiä.")

            else:
                print("Nimeä ei löydy tietokannasta.")

        elif komento == "lopeta":
            print("I'll be back.")
            break

        elif komento == "nimet":
            print(käyttäjät.keys())

        else:
            print("Come again?")
main()