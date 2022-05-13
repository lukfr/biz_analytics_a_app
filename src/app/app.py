import streamlit as st

st.title('Vorhersage der deutschen CO2-Emissionen')

"Autor: Lukas Frei (https://github.com/lukfr)"

# Model mit SciPy
from scipy.stats import linregress
st.subheader("Vorhersage")

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept


def scipy_model(desired_year):
    scipy_model_result = scipy_slope * desired_year + scipy_intercept
    return scipy_model_result

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction,2)

"Die Vorhersage der Emissionen für das ausgewählte jahr ist:"

st.write(prediction_rounded)

"Tonnen pro Kopf pro Jahr"
st.subheader("Über das Modell und die Daten")
"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 2010 bis 2020"
"Es steht ein Datenpunkt pro Jahr zur Verfügung"
#%%
