import streamlit as st

st.title('Prognose der Weltbevökerung')
"Autor: Lukas Frei (https://github.com/lukfr)"

# Model mit SciPy
from scipy.stats import linregress
st.subheader("Vorhersage")

years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
population_per_year = [5327529078, 5414289382, 5498919891, 5581597596, 5663150426, 5744212929, 5824891927, 5905045647, 5984794072, 6064239030, 6143776621, 6222912459, 6302062210, 6381477292, 6461454653, 6542205330, 6623819401, 6706251239, 6789396380, 6873077808, 6957137521, 7041509491, 7126144677, 7210900157, 7295610265, 7380117870, 7464344232, 7548182589, 7631091110, 7713468203, 7794798725, 7874965730,]

regression_result = linregress(years, population_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept


def scipy_model(desired_year):
    scipy_model_result = scipy_slope * desired_year + scipy_intercept
    return scipy_model_result

#User-Input for dessired year
desired_year = st.number_input('Eingabe des gewünschtes Jahres:', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = int(round(prediction,0))

#delta population desired year vs. 2021
delta_desired_to_end2021 = int(round(prediction_rounded - population_per_year[31],0))

#output in streamlit
st.metric(label="Wieviele Menschen leben in "+str(desired_year)+" auf der Welt:", value='{:,}'.format(prediction_rounded), delta=str('{:,}'.format(delta_desired_to_end2021)+' Menschen leben mehr auf der Welt im Vergleich zu 2021' ))

st.subheader("Über das Modell und die Daten")

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 1990 bis 2021"
"Es steht ein Datenpunkt pro Jahr zur Verfügung"
"Datenquelle: https://ourworldindata.org/grapher/population?time=1975..latest"
#%%

#%%
