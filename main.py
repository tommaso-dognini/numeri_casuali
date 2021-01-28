import streamlit as st
import time
import matplotlib.pyplot as plt
from selenium import webdriver
import matplotlib as mpl
import numpy as np

st.title('Random Generator: Quanto è random?')
pagina = st.sidebar.radio(
    'Menù', ['HOME', 'RANDOM GENERATOR', 'CODICE SORGENTE'])


if pagina == 'HOME':
    st.write('''
        Come stabilire se un numero è stato generato casualmente? Quali caratteristiche devono avere dei numeri generati casualmente?
        Come stabilire quanto sono casuali?\n
        
        Questo programma vi permette di eseguire dei test per cercare di rispondere a tutte queste domande!

        \n
        ### Come funziona\n
        Questo programma vi permette di generare numeri casuali utilizzando il programma random generator di google in modo automatizzato, semplice e veloce.
        E' sufficiente inserire gli estremi dell'intervallo dei numeri che si vuole generare casualmente, il numero di estrazioni da eseguire e il gioco è fatto. 
        \n
        \n 
        ### Inserisci i valori per proseguire con le estrazioni:  \n
    ''')
    minimo = st.number_input('minimo', min_value=1)
    massimo = st.number_input('massimo', min_value=2)
    volte = st.number_input('volte', min_value=1)

    st.write('''\nSeleziona il tipo di grafico che vuoi visualizzare\n''')
    frequenze_assolute = st.checkbox('Grafico frequenze assolute')
    frequenze_percentuali = st.checkbox(
        'Grafico frequenze relative percentuali')

    st.write('''
        **Per proseguire clicca sul tasto start:**\n
        N.B. :\n
         - Il programma aprirà automaticamente una finestra di Chrome, **affinchè il programma funzioni devi cliccare su continua**. Hai 10 secondi ;)\n
         - Durante l'esecuzione del programma **non chiudere la finestra di Chrome!**  
    ''')
    start = False
    start = st.button('START')

    if start:
        browser = webdriver.Chrome()
        browser.get(
            'https://www.google.com/search?channel=fs&client=ubuntu&q=numeri+casuali')
        time.sleep(10)
        # do il tempo di cliccare continua

        # imposto i valori
        min = browser.find_element_by_id('UMy8j')
        min.clear()
        min.send_keys(minimo)
        max = browser.find_element_by_id('nU5Yvb')
        max.clear()
        max.send_keys(massimo)

        # con un ciclo faccio n volte l'estrazione
        genera = browser.find_element_by_id('ZdzlKb')
        ris = browser.find_element_by_class_name(
            'gws-csf-randomnumber__result')
        numeri = []
        for i in range(volte):
            genera.click()
            time.sleep(0.5)
            numeri.append(int(ris.text))

        # chiudo il browser
        time.sleep(5)
        browser.quit()

        if frequenze_assolute:
            # realizzo il grafico frequenze
            x = np.arange(minimo, massimo + 1)  # per distanziare colonne
            width = 0.8  # larghezza delle colonne

            frequenze = []  # array delle frequenze
            for i in range(minimo, massimo+1):
                frequenze.append(numeri.count(i))

            # stile del grafico
            mpl.style.use('seaborn')
            fig, ax = plt.subplots()
            rects = ax.bar(x, frequenze, width, label='frequenze')

            ax.set_title('\nRandom generator: quanto è random?\n',
                         c='maroon', size=20.0)
            ax.set_ylabel('Frequenze assolute')
            ax.set_xlabel('\nNumeri estratti')
            ax.set_xticks(x)

            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width()/2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

            st.write('''### Risultati dell'estrazione:FREQUENZE ASSOLUTE\n''')

            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            start = False

        if frequenze_percentuali:
            # realizzo il grafico percentuali
            x = np.arange(minimo, massimo + 1)  # per distanziare colonne
            width = 0.8  # larghezza delle colonne

            percentuali = []  # array delle frequenze relative percentuali approssimate a 1 decimale
            tot = len(numeri)
            for i in range(minimo, massimo+1):
                percentuali.append(round(numeri.count(i)/tot*100, 1))

            # stile del grafico
            mpl.style.use('seaborn')
            fig, ax = plt.subplots()
            rects = ax.bar(x, percentuali, width, label='frequenze')

            ax.set_title('\nRandom generator: quanto è random?\n',
                         c='maroon', size=20.0)
            ax.set_ylabel('Frequenze relativa percentuale')
            ax.set_xlabel('\nNumeri estratti')
            ax.set_xticks(x)

            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width()/2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

            plt.show()

            st.write(
                '''### Risultati dell'estrazione: FREQUENZE RELATIVE PERCENTUALI\n''')

            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            start = False


elif pagina == 'RANDOM GENERATOR':
    st.write('''
        ### Random generator
        \n
        Se vuoi sperimentare come funziona google random generator clicca RANDOM GENERATOR
        \n
    ''')
    button = st.button('RANDOM GENERATOR')
    if button:
        browser = webdriver.Chrome()
        browser.get(
            'https://www.google.com/search?channel=fs&client=ubuntu&q=numeri+casuali')
        time.sleep(5)
elif pagina == 'CODICE SORGENTE':
    st.write('''
        In questa pagina puoi consultare il codice sorgente di questo programma.\n
    
            \t
            browser = webdriver.Chrome()
            browser.get(
                'https://www.google.com/search?channel=fs&client=ubuntu&q=numeri+casuali')
            time.sleep(10)
            # do il tempo di cliccare continua

            # imposto i valori
            min = browser.find_element_by_id('UMy8j')
            min.clear()
            min.send_keys(minimo)
            max = browser.find_element_by_id('nU5Yvb')
            max.clear()
            max.send_keys(massimo)

            # con un ciclo faccio n volte l'estrazione
            genera = browser.find_element_by_id('ZdzlKb')
            ris = browser.find_element_by_class_name('gws-csf-randomnumber__result')
            numeri = []
            for i in range(volte):
                genera.click()
                time.sleep(0.5)
                numeri.append(int(ris.text))

            #print(numeri)

            # a questo punto ho un array con tutti i risultati
            numero_numeri = massimo-minimo
            plt.hist(numeri, numero_numeri+1, range=(minimo,massimo+1), width=0.8, align='left')

            plt.xticks([k for k in range(minimo, massimo+1)])

            plt.title('Random Generator: quanto è random? ')
            plt.xlabel('numeri estratti')
            plt.ylabel('frequenze')
            plt.plot()

            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    ''')
