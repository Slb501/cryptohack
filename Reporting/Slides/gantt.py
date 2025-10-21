import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# 1. Définir les tâches et les dates
tasks = {
    "General": {
        "start": "2025-09-29",
        "end": "2025-10-06"
    },
    "Diffie-Hellman + RSA": {
        "start": "2025-10-06",
        "end": "2025-10-13"
    },
    "Rapport / Présentation": {
        "start": "2025-10-13",
        "end": "2025-10-21"
    }
}

# Conversion des chaînes de caractères en dates
for task in tasks.values():
    task['start_date'] = datetime.strptime(task['start'], '%Y-%m-%d')
    task['end_date'] = datetime.strptime(task['end'], '%Y-%m-%d')

# 2. Créer le diagramme
fig, ax = plt.subplots(figsize=(20, 8)) # Hauteur un peu réduite

# Tâches sur l'axe des y
task_names = list(tasks.keys())
y_pos = range(len(task_names))

# Durée de chaque tâche
start_dates = [tasks[name]['start_date'] for name in task_names]
durations = [(task['end_date'] - task['start_date']).days for task in tasks.values()]

# Ajouter les barres au graphique
bars = ax.barh(y_pos, durations, left=start_dates, height=0.6, align='center',
               color=['#3498db', '#e74c3c', '#2ecc71'])
ax.invert_yaxis()

# Écrire le texte dans les barres
for i, bar in enumerate(bars):
    text_x = start_dates[i] + timedelta(days=0.2)
    text_y = bar.get_y() + bar.get_height() / 2
    
    ax.text(text_x, text_y, 
            task_names[i], 
            va='center', ha='left',
            color='black', fontsize=15, fontweight='bold')

# 3. Mettre en forme le graphique
# --- MODIFICATION : LIGNES SUPPRIMÉES ---
# ax.set_yticks(y_pos)                 <-- SUPPRIMÉ
# ax.set_yticklabels(task_names)       <-- SUPPRIMÉ
ax.set_yticks([]) # On retire les "marques" sur l'axe Y

ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
ax.tick_params(axis='x', labelsize=14)

plt.xlabel('Date', fontsize=12)
# plt.ylabel('Tâches', fontsize=12)     <-- SUPPRIMÉ (le titre de l'axe n'est plus utile)
plt.title('Diagramme de Gantt du Projet', fontsize=16, fontweight = "bold")

plt.grid(True, which='major', axis='x', linestyle='')
fig.autofmt_xdate()

# On ajuste les marges pour que le graphique prenne toute la place
plt.tight_layout()
plt.show()