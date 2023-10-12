from . import lib

def plot(data):
    # data is Version;Date_of_report;Date_of_publication;Municipality_code;Municipality_name;Province;Total_reported;Hospital_admission;Deceased
    rows=data[1:]
    pass

def do_investigation():
    datum = []
    data = lib.load_data()
    plot(datum)

do_investigaton()
