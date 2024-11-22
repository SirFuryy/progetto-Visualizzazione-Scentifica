import fastf1 as ff1

Q = ff1.get_session(2024, 'Austin', 4)
Q.load()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import fastf1.plotting as f1plt
import fastf1.utils as f1u
import pandas as pd
from timple.timedelta import strftimedelta
from timple.timedelta import num2timedelta
from fastf1.core import Laps

plt.rc('figure', figsize=(15.0, 10.0))
mpl.rcParams['figure.facecolor'] = 'None' # Il colore di sfondo del grafico seguirà quello del PowerPoint
mpl.rcParams['axes.facecolor'] = 'None'
f1plt.setup_mpl(color_scheme=None, misc_mpl_mods=False)


### Colori
colors_palette = {
    # Teams
    'Red Bull': '#CCA9DD',
    'Ferrari': '#CB3234',
    'Mercedes': '#A3E7D6',
    'Alpine': '#99D6EA',
    'Alfa Romeo': '#641C34',
    'McLaren': '#EFA94A',
    'Haas': '#987654',
    'AlphaTauri': '#1E213D',
    'Williams': '#4592CE',
    'Aston Martin': '#216477',
    # Teams Storici
    'Lotus': '#CDA434',
    'Renault': '#FFFF66',
    'Benetton': '#177245',
    'Brabham': '#77DD77',
    'Tyrrell': '#ABCDEF'
}

### Associazione Pilota --> Squadra
driver_team = {
    'VER': 'Red Bull',
    'HAM': 'Mercedes',
    'LEC': 'Ferrari',
    'NOR': 'McLaren',
    'PER': 'Red Bull',
    'SAI': 'Ferrari',
    'GAS': 'Alpine',
    'RUS': 'Mercedes',
    'ALB': 'Williams',
    'PIA': 'McLaren',
    'OCO': 'Alpine',
    'RIC': 'AlphaTauri',
    'ALO': 'Aston Martin',
    'TSU': 'AlphaTauri',
    'HUL': 'Haas',
    'BOT': 'Alfa Romeo',
    'ZHO': 'Alfa Romeo',
    'MAG': 'Haas',
    'SAR': 'Williams',
    'STR': 'Aston Martin'
}

drivers = pd.unique(Q.laps['Driver'])
Q1, Q2, Q3 = Q.laps.split_qualifying_sessions()

list_fastest_laps = list()
for drv in drivers[15:]:
    #
    #   Provare a vedere se si possono prendere tutti i driver in una volta sola (pick_drivers)
    #
    drvs_fastest_lap = Q1.pick_driver(drv).pick_fastest()
    list_fastest_laps.append(drvs_fastest_lap)
for drv in drivers[10:15]:
    drvs_fastest_lap = Q2.pick_driver(drv).pick_fastest()
    list_fastest_laps.append(drvs_fastest_lap)
for drv in drivers[:10]:
    drvs_fastest_lap = Q3.pick_driver(drv).pick_fastest()
    list_fastest_laps.append(drvs_fastest_lap)
fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)

pole_lap = fastest_laps.pick_fastest()
fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']
fastest_laps['Complete_Name'] = [
    'Charles Leclerc',
    'Lando Norris',
    'Lewis Hamilton',
    'Carlos Sainz',
    'George Russell',
    'Max Verstappen',
    'Pierre Gasly',
    'Esteban Ocon',
    'Sergio Perez',
    'Oscar Piastri',
    'Yuki Tsunoda',
    'Guanyu Zhou',
    'Valtteri Bottas',
    'Kevin Magnussen',
    'Daniel Ricciardo',
    'Nico Hulkenberg',
    'Fernando Alonso',
    'Alexander Albon',
    'Lance Stroll',
    'Logan Sargeant'
]
team_colors = list()
for index, lap in fastest_laps.iterlaps():
    color = colors_palette[driver_team[lap['Driver']]]
    team_colors.append(color)

fig, ax = plt.subplots()
ax.barh(fastest_laps['Driver'], fastest_laps['LapTimeDelta'],
        color=team_colors, alpha=.75)
ax.set_yticks(fastest_laps['Driver'])
ax.set_yticklabels(fastest_laps['Complete_Name'])

# show fastest at the top
ax.invert_yaxis()

lap_time_string = [strftimedelta(i, '%m:%s.%ms') for i in fastest_laps['LapTime']]

plt.suptitle(f"{Q.event['EventName']} {Q.event.year} Qualifica\n"
             f"Giro Veloce: {lap_time_string[0]} (Charles Leclerc)")

for i in range(len(fastest_laps)):
    plt.text(fastest_laps.LapTimeDelta[i]+num2timedelta((1/24/60/60)*0.01), i+0.15, lap_time_string[i], ha = 'left')

plt.xlim(0, num2timedelta(2.3/24/60/60))
plt.grid(visible=None, which='both')
plt.ylabel('Piloti')
plt.xlabel('Distacco dal Giro Veloce')
plt.tight_layout()
plt.savefig('Grafici/Q - Distacco dalla Pole.png', dpi=700, bbox_inches='tight')
plt.show()