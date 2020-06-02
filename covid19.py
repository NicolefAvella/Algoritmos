"""
Calcular el porcentaje de probabilidad que existe de tener Covid19 con sintomas graves en Colombia

Las cifras arrojadas por el ministerio de salud en Colombia al 01 de junio de 2020 son las siguientes:
* Pruebas realizadas= 34114
* Casos negativos = 310649
* Casos positivos = 30493
* Casos positivos con sintomas severos que requieren hospitalizacion = 2756

* Poblacion en colombia = 48258494

"""

def theorem_bayes(prior_A, prob_B_if_A, prob_B):
    return (prior_A*prob_B_if_A)/prob_B

if __name__ == '__main__':
    prob_covid = 30493 / 48258494
    prob_severe_symptom_if_covid = 2756 / 341142
    prob_severe_symptom_if_not_covid = 310649 / 48228001
    prob_not_covid = 1 - prob_covid

    prob_symptom = (prob_severe_symptom_if_covid * prob_covid) + (prob_severe_symptom_if_not_covid * prob_not_covid)

    prob_covid_if_severe_symptom = theorem_bayes(prob_covid, prob_severe_symptom_if_covid, prob_symptom)

    print("Tienes una probabilidad del {} de tener covid19 con sintomas graves".format(round(prob_covid_if_severe_symptom*100, 4)))
