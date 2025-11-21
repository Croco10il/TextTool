#!/usr/bin/env python3



def process_line(line):
    """
    Analyse une ligne de commande et exécute l'opération demandée.
    L'utilisateur B a écrit cette docstring.
    """
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "count-words":
        return len(text.split())
    if cmd == "lenght":
	return str(len(text))
    if cmd == "prefix":
	return text[:10]


    return "Unknown command " + cmd



def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
