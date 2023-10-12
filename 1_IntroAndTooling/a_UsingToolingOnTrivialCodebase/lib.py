import csvloader

def load_data():
    # TODO: write up where i got this from (https://data.rivm.nl/covid-19/) then
    # i manually changed semicolon to comma lol
    f=open('C:\\Users\\adamk\\Desktop\\COVID-19_aantallen_gemeente_cumulatief.csv')
    parsed=  csvloader.loads(f)
    f.close()
