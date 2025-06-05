# fichier : simulateur_web/strategies.py

import random
import pandas as pd
import math

def strategie_uniforme(n):
    traitements = ['A', 'B', 'C', 'D', 'E']
    resultats = []
    for i in range(n):
        t = random.choice(traitements)
        success = random.random() < 0.6
        resultats.append({"Patient": i+1, "Traitement": t, "Succes": int(success)})
    df = pd.DataFrame(resultats)
    df.to_csv("static/resultats_uniforme.csv", index=False)
    return df

def strategie_greedy(n):
    traitements = ['A', 'B', 'C', 'D', 'E']
    compte = {t: 0 for t in traitements}
    succes = {t: 0 for t in traitements}
    resultats = []
    for i, t in enumerate(traitements):
        outcome = random.random() < 0.6
        compte[t] += 1
        succes[t] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": t, "Succes": int(outcome)})
    for i in range(len(traitements), n):
        estimations = {t: succes[t] / compte[t] for t in traitements}
        best = max(estimations, key=estimations.get)
        outcome = random.random() < 0.6
        compte[best] += 1
        succes[best] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": best, "Succes": int(outcome)})
    df = pd.DataFrame(resultats)
    df.to_csv("static/resultats_greedy.csv", index=False)
    return df

def strategie_epsilon(n, epsilon=0.1):
    traitements = ['A', 'B', 'C', 'D', 'E']
    compte = {t: 0 for t in traitements}
    succes = {t: 0 for t in traitements}
    resultats = []
    for i, t in enumerate(traitements):
        outcome = random.random() < 0.6
        compte[t] += 1
        succes[t] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": t, "Succes": int(outcome)})
    for i in range(len(traitements), n):
        if random.random() < epsilon:
            t = random.choice(traitements)
        else:
            estimations = {t: succes[t] / compte[t] for t in traitements}
            t = max(estimations, key=estimations.get)
        outcome = random.random() < 0.6
        compte[t] += 1
        succes[t] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": t, "Succes": int(outcome)})
    df = pd.DataFrame(resultats)
    df.to_csv("static/resultats_epsilon_greedy.csv", index=False)
    return df

def strategie_hoeffding(n):
    traitements = ['A', 'B', 'C', 'D', 'E']
    compte = {t: 0 for t in traitements}
    succes = {t: 0 for t in traitements}
    resultats = []
    for i, t in enumerate(traitements):
        outcome = random.random() < 0.6
        compte[t] += 1
        succes[t] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": t, "Succes": int(outcome)})
    for i in range(len(traitements), n):
        ucb = {
            t: (succes[t] / compte[t]) + math.sqrt(math.log(i+1) / (2 * compte[t]))
            for t in traitements
        }
        best = max(ucb, key=ucb.get)
        outcome = random.random() < 0.6
        compte[best] += 1
        succes[best] += int(outcome)
        resultats.append({"Patient": i+1, "Traitement": best, "Succes": int(outcome)})
    df = pd.DataFrame(resultats)
    df.to_csv("static/resultats_hoeffding.csv", index=False)
    return df
