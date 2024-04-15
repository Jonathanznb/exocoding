""
reponse_fr = input("quelle note en fr?")
reponse_nl = input("quelle note en nl?")
reponse_ma = input("quelle note en math?")

int_note_fr = int(reponse_fr)
int_note_nl = int(reponse_nl)
int_note_ma = int(reponse_ma)
""

int_note_fr = int(input("quelle note en fr?"))
int_note_nl = int(input("quelle note en nl?"))
int_note_ma = int(input("quelle note en math?"))
moyenne = (int_note_fr + int_note_nl + int_note_ma)/3

print("La moyenne de l'élève est: " + str(moyenne))