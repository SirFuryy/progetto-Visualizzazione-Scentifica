# 🏎️ Analisi e Confronto GP COTA F1 (2023 vs 2024)  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)  
[![FastF1](https://img.shields.io/badge/FastF1-F1%20Data-red.svg)](https://theoehrly.github.io/Fast-F1/)  
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)  

## 📌 Descrizione del Progetto  

Questo progetto sviluppato come esame del corso di **visualizzazione scientifica** della laurea in Informatica dell'Università degli Studi di Milano analizza e confronta il **Gran Premio di Austin (COTA) di Formula 1** tra le stagioni **2023 e 2024**, con l’obiettivo di identificare i principali fattori che hanno contribuito al miglioramento della **pole position** di ben **2.7 secondi**.  

Attraverso l’utilizzo di **FastF1** per l’estrazione dei dati e **Pandas** per la loro elaborazione, il progetto genera un'analisi dettagliata rappresentata in un **PowerPoint**, che spiega il ruolo di vari fattori nelle prestazioni migliorate.  

---

## 🔍 Obiettivi dell'Analisi  

- 📊 **Confronto delle sessioni** per individuare differenze nelle prestazioni.  
- 🌦️ **Analisi meteo** per verificare l'influenza delle condizioni atmosferiche.  
- ⏱️ **SuperTimes 2023 vs 2024** per determinare quali settori hanno contribuito maggiormente al miglioramento del giro veloce.  
- 📉 **Generazione di grafici e tabelle** per una chiara visualizzazione dei dati.  

---

## 🏗️ Struttura del Progetto  

📂 **py_meteo/** → Confronto delle condizioni meteorologiche tra il 2023 e il 2024.  
📂 **confronto_sessioni/** → Analisi delle sessioni di qualifica e gara.  
📂 **confronto_anni/** → Confronto dei **SuperTimes** tra il 2023 e il 2024.  
📂 **grafici/** → PNG dei grafici generati dall’analisi.  

---

## 🚀 Installazione e Utilizzo  

1. **Clona il repository**

    ```sh
    git clone https://github.com/SirFuryy/progetto-Visualizzazione-Scentifica
    cd GP_COTA_Analysis
    ```

2. **Installa le dipendenze**

    ```sh
    pip install -r requirements.txt
    ```

3. **Esegui gli script di analisi**

    ```sh
    python script_analisi.py
    ```

4. **Esplora i risultati nella cartella grafici/ o nel PowerPoint generato.**

---

## 📊 Tecnologie Utilizzate

- Python 3.8+
- FastF1 → Per ottenere dati ufficiali sulle sessioni di F1.
- Pandas → Per elaborare e analizzare i dati.
- Matplotlib / Seaborn → Per la generazione dei grafici.
- PowerPoint Automation → Per la creazione di un report visivo.

---

## 📜 Licenza

Il progetto è distribuito sotto licenza GNU GPL v3.0. Per maggiori informazioni, consulta il file LICENSE.
