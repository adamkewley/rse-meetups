import csvloader

def load_data():
    # TODO: write up where i got this from (https://data.rivm.nl/covid-19/)

    data = []
    f=open('C:\\Users\\adamk\\Desktop\\COVID-19_aantallen_gemeente_cumulatief.csv', 'rt')
    for l in f:
        data.append(l.split(';'))
    return data

# derived from group research !!!!!!DO NOT TOUCH!!!!!
correction_factor = 1.0
