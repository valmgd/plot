import matplotlib.pyplot as plt
import numpy as np

class Particles :
    def __init__(self) :
        self.x = 0
    #}
#}

def plot_bulle(x, y, mvx, mvy, P, title) :
    # -------------------------------------------------------------------------------------------------------
    # tracés
    # -------------------------------------------------------------------------------------------------------
    fig, ax = plt.subplots()
    im = ax.scatter(x, y, s=20, c=P, cmap='jet', label='Particules')
    cax = fig.colorbar(im, ax=ax)
    cax.set_label('Pressure [Pa]')

    ax.quiver(x, y, mvx, mvy, angles='xy', scale=0.05, label='Quantité mvt', color='black')

    # -------------------------------------------------------------------------------------------------------
    # affichage
    # -------------------------------------------------------------------------------------------------------
    ax.set_xlabel('$x$ [m]')
    ax.set_ylabel('$y$ [m]')
    ax.set_aspect('equal', 'datalim')
    ax.set_facecolor('lavender')
    ax.set_title(title)

    ax.legend(loc='best', fontsize='x-large', fancybox=True, framealpha=0.5)
    ax.grid(color='gray', linestyle='--')

    fig.tight_layout()

    return(fig, ax)
#}

def quarter(x, y, mvx, mvy) :
    n = len(x)
    somme_x = somme_y = 0.
    for i in range(0, n) :
        if x[i] >= 0 and y[i] >= 0 :
            somme_x += mvx[i]
            somme_y += mvy[i]
        #}
    #}
    return(somme_x, somme_y)
#}
