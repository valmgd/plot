import matplotlib.pyplot as plt
import numpy as np



def head_tail(vec) :
    chaine = '[ ' + str(vec[0]) + '   ' + str(vec[1]) + '   ' + str(vec[2])
    chaine += '   ...   '
    chaine += str(vec[-3]) + '   ' + str(vec[-2]) + '   ' + str(vec[-1]) + ' ]'

    return(chaine)
#}

def set_graph_style(fig, ax) :
    ax.set_aspect('equal', 'datalim')
    ax.set_facecolor('lavender')

    ax.legend(loc='best', fontsize='x-large', fancybox=True, framealpha=0.5)
    ax.grid(color='gray', linestyle='--')

    fig.tight_layout()
#}



class Particles :
    """Classe Particles.
    Coordonnées, variables du système de N-S, tension de surface."""
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

        # courbure
        self.kappa = np.loadtxt('../out-sph/' + directory + '/kappa.dat')

        # gradient de pression
        self.GRPx = (self.w * self.FTSx - self.mvx) / self.w
        self.GRPy = (self.w * self.FTSy - self.mvy) / self.w

        self.n = len(self.x)
    #}

    # -------------------------------------------------------------------------------------------------------
    # représentation
    # -------------------------------------------------------------------------------------------------------
    def __repr__(self) :
        chaine  =   'x    : ' + head_tail(self.x)
        chaine += '\ny    : ' + head_tail(self.y)
        chaine += '\nmvx  : ' + head_tail(self.mvx)
        chaine += '\nmvy  : ' + head_tail(self.mvy)
        chaine += '\nP    : ' + head_tail(self.P)
        chaine += '\nvx   : ' + head_tail(self.vx)
        chaine += '\nvy   : ' + head_tail(self.vy)
        chaine += '\nFTSx : ' + head_tail(self.FTSx)
        chaine += '\nFTSy : ' + head_tail(self.FTSy)
        chaine += '\nw    : ' + head_tail(self.w)
        chaine += '\nGRPx : ' + head_tail(self.GRPx)
        chaine += '\nGRPy : ' + head_tail(self.GRPy)

        return(chaine)
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
        ax.set_title(title)
        set_graph_style(fig, ax)

        return(fig, ax)
    #}

    # -------------------------------------------------------------------------------------------------------
    # plot champs de vecteur : quantité de mvt
    # -------------------------------------------------------------------------------------------------------
    def plot_curvature(self) :
        fig, ax = plt.subplots()
        im = ax.scatter(self.x, self.y, s=20, c=self.kappa, cmap='jet', label='Particules')
        cax = fig.colorbar(im, ax=ax)
        cax.set_label('$\kappa$ [$m^{-1}$]')

        ax.set_xlabel('$x$ [m]')
        ax.set_ylabel('$y$ [m]')
        ax.set_title('Courbure')
        set_graph_style(fig, ax)

        return(fig, ax)
    #}

    # -------------------------------------------------------------------------------------------------------
    # plot 2 champs de vecteurs : le gradient de pression et la tension de surface
    # -------------------------------------------------------------------------------------------------------
    def plot_ts_forces(self) :
        sc = 0.01
        r = 0.015

        fig, ax = plt.subplots(ncols=2)

        ax[0].scatter(self.x, self.y, s=20, label='Particules')
        ax[0].quiver(self.x, self.y, self.GRPx, self.GRPy, angles='xy', scale=sc, label='GRP', color='black')
        ax[0].set_xlabel('$x$ [m]')
        ax[0].set_ylabel('$y$ [m]')
        ax[0].set_title('Gradient de pression')
        ax[0].set_xlim((-r, r))
        ax[0].set_ylim((-r, r))
        set_graph_style(fig, ax[0])

        ax[1].scatter(self.x, self.y, s=20, label='Particules')
        ax[1].quiver(self.x, self.y, self.FTSx, self.FTSy, angles='xy', scale=sc, label='FTS', color='black')
        ax[1].set_xlabel('$x$ [m]')
        ax[1].set_ylabel('$y$ [m]')
        ax[1].set_title('Tension de surface')
        ax[1].set_xlim((-r, r))
        ax[1].set_ylim((-r, r))
        set_graph_style(fig, ax[1])

        return(fig, ax)
    #}

    # -------------------------------------------------------------------------------------------------------
    # somme de la quantité de mouvement sur un quartier de la bulle
    # -------------------------------------------------------------------------------------------------------
    def quarter(self) :
        n = len(self.x)
        somme_x = somme_y = 0.
        for i in range(0, n) :
            if self.x[i] >= 0 and self.y[i] >= 0 :
                somme_x += self.mvx[i]
                somme_y += self.mvy[i]
            #}
        #}
        return(somme_x, somme_y)
    #}
#}
