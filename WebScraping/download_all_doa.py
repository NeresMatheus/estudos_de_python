import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from baixa_diario import download_diario

if __name__ == '__main__':

    dates = calendar.Calendar()
    today = datetime.today()
    list_of_results = []

    valor_ano = 2010
    while valor_ano < 2011:

        if valor_ano != 2010:
            valor_mes = 1
        else:
            valor_mes = 12

        while valor_mes <= 12:
            interavel = dates.itermonthdays4(valor_ano, valor_mes)
            for i in interavel:
                ano, mes, dia, numero = i
                if numero <= 4:
                    # print(ano, mes, dia, numero)
                    list_of_results.append(download_diario(ano, mes, dia))
            valor_mes += 1
            if ano == 2023 and mes == 7 and dia == 20:
                break
        valor_ano += 1

    print(list_of_results)
