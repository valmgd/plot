#!/home/vmagda/.anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np

from plot import *



# -----------------------------------------------------------------------------------------------------------
# données
# -----------------------------------------------------------------------------------------------------------
part = Particles('avec-ts')
print(part)



# -----------------------------------------------------------------------------------------------------------
# calculs somme sur quartiers
# -----------------------------------------------------------------------------------------------------------
somme_x, somme_y = part.quarter()
print('\nSomme Dmv/Dt sur un quartier :')
print(somme_x, somme_y)

# quantité de mouvement max
qmvMax = 'Dmv max en norme euclidienne : ' + str(max(np.sqrt(part.mvx**2 + part.mvy**2)))
print('\n', qmvMax)

# intervalle de pression
ip = 'Intervalle de pression : ' + '[' + str(min(part.P)) + ',' + str(max(part.P)) + ']'
print('\n', ip)

# vitesse max
vMax = 'Vitesse max en norme euclidienne : ' + str(max(np.sqrt(part.vx**2 + part.vy**2)))
print('\n', vMax)

# volume total
wTot = 'Volume total :' + str(sum(part.w))
print('\n', wTot)



# -----------------------------------------------------------------------------------------------------------
# Quantité de mouvement
# -----------------------------------------------------------------------------------------------------------
titre = 'Quantité de mvt avec TS\n initialisation bulle avec pression de Laplace\n$Dmv = -\omega GRP + \omega FTS$'
fig, ax = part.plot_mvt_quantity(titre)
ax.text(0.005, -0.011, s=qmvMax)
ax.text(0.005, -0.012, s=ip)
ax.text(0.005, -0.013, s=vMax)
ax.text(0.005, -0.014, s=wTot)

part.plot_ts_forces()

part.plot_curvature()



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
plt.show()
