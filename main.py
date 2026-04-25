import csv

# ============ ÉTAPE 1 : Générer ventes.csv ============
donnees = [
    [101, 15.0, 3, 10],
    [102, 25.0, 2, 5],
    [103, 10.0, 5, 0],
    [104, 50.0, 1, 15],
    [105, 8.0, 10, 0],
]
with open("ventes.csv", "w", newline="") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["ID", "Prix", "Quantite", "Remise"])
    writer.writerows(donnees)
print("✅ Fichier ventes.csv créé !")

# ============ ÉTAPES 2-6 : Calculs ============
ca_total = 0
meilleur_id = None
meilleur_ca = 0
resultats = []

with open("ventes.csv", "r") as fichier:
    reader = csv.DictReader(fichier)
    for ligne in reader:
        id_produit = int(ligne["ID"])
        prix = float(ligne["Prix"])
        quantite = int(ligne["Quantite"])
        remise = float(ligne["Remise"])

        ca_brut = prix * quantite
        ca_net = ca_brut * (1 - remise / 100)
        tva = round(ca_net * 0.20, 2)

        ca_total += ca_net

        if ca_net > meilleur_ca:
            meilleur_ca = ca_net
            meilleur_id = id_produit

        resultats.append({
            "ID": id_produit,
            "Prix": prix,
            "Quantite": quantite,
            "Remise": remise,
            "CA_Brut": ca_brut,
            "CA_Net": ca_net,
            "TVA": tva
        })

        print(f"Produit {id_produit} → CA Brut = {ca_brut} DT | CA Net = {ca_net} DT | TVA = {tva} DT")

# ============ ÉTAPE 5 : CA Total ============
print(f"\n💰 CA Total de l'entreprise = {ca_total} DT")

# ============ ÉTAPE 6 : Meilleur produit ============
print(f"🏆 Meilleur produit : ID {meilleur_id} avec {meilleur_ca} DT")

# ============ ÉTAPE 7 : Export resultats_final.csv ============
with open("resultats_final.csv", "w", newline="") as sortie:
    colonnes = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]
    writer = csv.DictWriter(sortie, fieldnames=colonnes)
    writer.writeheader()
    writer.writerows(resultats)

print("✅ Fichier resultats_final.csv exporté avec succès !")