import matplotlib.pyplot as plt
import numpy as np

class Particles :
    # -------------------------------------------------------------------------------------------------------
    # constructeur
    # -------------------------------------------------------------------------------------------------------
    def __init__(self, directory) :
        # coordonnées
        self.x    = np.loadtxt('../out-sph/' + directory + '/x.dat')
        self.y    = np.loadtxt('../out-sph/' + directory + '/y.dat')

        # quantité de mvt
        self.mvx  = np.loadtxt('../out-sph/' + directory + '/mvx.dat')
        self.mvy  = np.loadtxt('../out-sph/' + directory + '/mvy.dat')

        # pression
        self.P    = np.loadtxt('../out-sph/' + directory + '/P.dat')

        # vitesse
        self.vx   = np.loadtxt('../out-sph/' + directory + '/vx.dat')
        self.vy   = np.loadtxt('../out-sph/' + directory + '/vy.dat')

        # Tension de surface
        self.FTSx = np.loadtxt('../out-sph/' + directory + '/FTSx.dat')
        self.FTSy = np.loadtxt('../out-sph/' + directory + '/FTSy.dat')

        # volume
        self.w    = np.loadtxt('../out-sph/' + directory + '/w.dat')

        # gradient de pression
        self.GRPx = (self.w * self.FTSx - self.mvx) / self.w
        self.GRPy = (self.w * self.FTSy - self.mvy) / self.w
    #}

    # -------------------------------------------------------------------------------------------------------
    # plot champs de vecteur : quantité de mvt
    # -------------------------------------------------------------------------------------------------------
    def plot_mvt_quantity(self, title) :
        fig, ax = plt.subplots()
        im = ax.scatter(self.x, self.y, s=20, c=self.P, cmap='jet', label='Particules')
        cax = fig.colorbar(im, ax=ax)
        cax.set_label('Pressure [Pa]')

        ax.quiver(self.x, self.y, self.mvx, self.mvy, angles='xy', scale=0.05, label='Quantité mvt', color='black')

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

    # -------------------------------------------------------------------------------------------------------
    # plot 2 champs de vecteurs : le gradient de pression et la tension de surface
    # -------------------------------------------------------------------------------------------------------
    def plot_ts_forces(self) :
        sc = 0.01

        fig, ax = plt.subplots(ncols=2)

        ax[0].scatter(self.x, self.y, s=20, label='Particules')
        ax[0].quiver(self.x, self.y, self.GRPx, self.GRPy, angles='xy', scale=sc, label='GRP', color='black')
        ax[0].set_xlabel('$x$ [m]')
        ax[0].set_ylabel('$y$ [m]')
        ax[0].set_aspect('equal', 'datalim')
        ax[0].set_facecolor('lavender')
        ax[0].set_title('Gradient de pression')
        ax[0].set_xlim((-0.02, 0.02))
        ax[0].set_ylim((-0.02, 0.02))

        ax[0].legend(loc='best', fontsize='x-large', fancybox=True, framealpha=0.5)
        ax[0].grid(color='gray', linestyle='--')

        ax[1].scatter(self.x, self.y, s=20, label='Particules')
        ax[1].quiver(self.x, self.y, self.FTSx, self.FTSy, angles='xy', scale=sc, label='FTS', color='black')
        ax[1].set_xlabel('$x$ [m]')
        ax[1].set_ylabel('$y$ [m]')
        ax[1].set_aspect('equal', 'datalim')
        ax[1].set_facecolor('lavender')
        ax[1].set_title('Tension de surface')
        ax[1].set_xlim((-0.02, 0.02))
        ax[1].set_ylim((-0.02, 0.02))

        ax[1].legend(loc='best', fontsize='x-large', fancybox=True, framealpha=0.5)
        ax[1].grid(color='gray', linestyle='--')


        fig.tight_layout()

        return(fig, ax)
    #}
#}



def quarter(part) :
    n = len(part.x)
    somme_x = somme_y = 0.
    for i in range(0, n) :
        if part.x[i] >= 0 and part.y[i] >= 0 :
            somme_x += part.mvx[i]
            somme_y += part.mvy[i]
        #}
    #}
    return(somme_x, somme_y)
#}
