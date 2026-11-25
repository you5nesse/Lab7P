from datetime import datetime

class ValidationMixin:
    def valider(self):
        if not getattr(self, "titre", None) or not self.titre.strip():
            raise ValueError("Titre obligatoire et non vide !")
        print("[Validation] Titre OK")

class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def enregistrer_historique(self, ancienne_description):
        self.historique.append({
            "date": datetime.now(),
            "ancienne_description": ancienne_description
        })

    def afficher_historique(self):
        if not self.historique:
            print("Aucun historique pour cette tâche.")
            return
        print(f"--- Historique de '{self.titre}' ---")
        for i, entree in enumerate(self.historique, 1):
            print(f"{i}. Le {entree['date']} : {entree['ancienne_description']}")

# 3. Mixin Journalisation
class JournalisationMixin:
    def journaliser(self, action):
        print(f"[Journal] {datetime.now()} - {action} : '{self.titre}'")

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description):
        HistoriqueMixin.__init__(self)
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()

        self.valider()
        self.journaliser("Création")

    def mettre_a_jour(self, nouvelle_description):
        self.valider()
        # 1. Sauvegarder l'ancienne version AVANT de modifier
        self.enregistrer_historique(self.description)
        # 2. Modifier
        self.description = nouvelle_description
        # 3. Journaliser
        self.journaliser("Modification")

    def __str__(self):
        return f"Tâche '{self.titre}' - {self.description}"
t1 = Tache("Rapport de stage", "Version 1 du rapport")
print(t1)

t1.mettre_a_jour("Version 2 - Ajout introduction")