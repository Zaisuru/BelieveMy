age = int(input("Quel age avez-vous ? "))
bank = int(input("De combien disposez-vous sur votre banque ?"))
monthly_payment = int(input("Combien de mensualités souhaitez-vous ? "))
rising = int(input("Combien désirez-vous emprunter ? "))

#Si la personne a plus de 80ans, taux de 40%, sinon 10%
if age >=80:
    percentage = 40
else :
    percentage = 10

#Si la personne a moins de 100 euros en banque, on lui refuse le crédit

if bank > 100:
    percentage_total = rising + ((rising * percentage) /100)
    #resultat = print(f"Votre crédit d'un montant de {rising} euros vous engagera sur {monthly_payment} mois pour {monthly_payment_amount} euros par mois \n\t-> {total} euros en tout")

else:
    print("Nous sommes désolé mais nous ne pouvons pas donner suite à votre demande.")








