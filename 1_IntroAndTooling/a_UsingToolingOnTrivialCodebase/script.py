from utils import lib
import matplotlib.pyplot as plt
from datetime import datetime

def apply_correction(yv):
    return yv*lib.correction_factor

def plot(data):
    t = [datetime.strptime(r[1], '%Y-%m-%d %H:%M:%S') for r in data[1:] if r[4] == 'Groningen' and r[5] == 'Groningen']
    dc = [apply_correction(float(f[6])) for f in data[1:] if f[4] == 'Groningen' and f[5] == 'Groningen']

    fig, ax = plt.subplots()
    ax.scatter(t, dc)
    ax.set_title("PROOF THAT IT'S ALL FAKE")
    ax.set_xlabel('TIME')
    ax.set_ylabel('PROOF')
    plt.show()
    plt.pause(10)

def do_investigation():
    datum = []
    data = lib.load_data()
    plot(datum)

do_investigaton()
