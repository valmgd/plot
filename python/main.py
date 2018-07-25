#!/home/vmagda/.anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np

from plot import *



# -----------------------------------------------------------------------------------------------------------
# données
# -----------------------------------------------------------------------------------------------------------
x      = np.loadtxt('../out-sph/sans-ts/x.dat')
y      = np.loadtxt('../out-sph/sans-ts/y.dat')
mvx    = np.loadtxt('../out-sph/sans-ts/mvx.dat')
mvy    = np.loadtxt('../out-sph/sans-ts/mvy.dat')
P      = np.loadtxt('../out-sph/sans-ts/P.dat')
vx     = np.loadtxt('../out-sph/sans-ts/vx.dat')
vy     = np.loadtxt('../out-sph/sans-ts/vy.dat')

ts_x   = np.loadtxt('../out-sph/avec-ts/x.dat')
ts_y   = np.loadtxt('../out-sph/avec-ts/y.dat')
ts_mvx = np.loadtxt('../out-sph/avec-ts/mvx.dat')
ts_mvy = np.loadtxt('../out-sph/avec-ts/mvy.dat')
ts_P   = np.loadtxt('../out-sph/avec-ts/P.dat')
ts_vx  = np.loadtxt('../out-sph/avec-ts/vx.dat')
ts_vy  = np.loadtxt('../out-sph/avec-ts/vy.dat')
FTSx   = np.loadtxt('../out-sph/avec-ts/FTSx.dat')
FTSy   = np.loadtxt('../out-sph/avec-ts/FTSy.dat')
ts_w   = np.loadtxt('../out-sph/avec-ts/w.dat')

n = len(x)
ts_n = len(ts_x)



# -----------------------------------------------------------------------------------------------------------
# calculs somme sur quartiers
# -----------------------------------------------------------------------------------------------------------
print('nombre de particules : ', n, ts_n)

somme_x, somme_y = quarter(x, y, mvx, mvy)
print('\nSomme Dmv/Dt sur un quartier sans TS :')
print(somme_x, somme_y)

somme_x, somme_y = quarter(ts_x, ts_y, ts_mvx, ts_mvy)
print('\nSomme Dmv/Dt sur un quartier avec TS :')
print(somme_x, somme_y)

# print('\nDifférence entre Dmv/Dt avec TS et sans TS en norme infinie :')
# print(max(abs(mvx - ts_mvx)), max(abs(mvy - ts_mvy)))

# quantité de mouvement max
qmvMax = 'Dmv max en norme euclidienne : ' + str(max(np.sqrt(ts_mvx**2 + ts_mvy**2)))
print('\n', qmvMax)

# intervalle de pression
ip = 'Intervalle de pression : ' + '[' + str(min(ts_P)) + ',' + str(max(ts_P)) + ']'
print('\n', ip)

# vitesse max
vMax = 'Vitesse max en norme euclidienne : ' + str(max(np.sqrt(ts_vx**2 + ts_vy**2)))
print('\n', vMax)

# volume total
wTot = 'Volume total :' + str(sum(ts_w))
print('\n', wTot)



# -----------------------------------------------------------------------------------------------------------
# sans ts
# -----------------------------------------------------------------------------------------------------------
# fig1, ax1 = plot_bulle(x, y, mvx, mvy, P, 'Quantité de mvt sans TS')



# -----------------------------------------------------------------------------------------------------------
# avec ts
# -----------------------------------------------------------------------------------------------------------
titre1 = 'Quantité de mvt avec TS, t=1s\n initialisation bulle avec pression de Laplace'
titre2 = 'Quantité de mvt avec TS, t=240s\n initialisation carré avec pression quelconque'
fig2, ax2 = plot_bulle(ts_x, ts_y, ts_mvx, ts_mvy, ts_P, titre2)
ax2.text(0.005, -0.011, s=qmvMax)
ax2.text(0.005, -0.012, s=ip)
ax2.text(0.005, -0.013, s=vMax)
ax2.text(0.005, -0.014, s=wTot)



# -----------------------------------------------------------------------------------------------------------
# gradient de pression et tension de surface
# -----------------------------------------------------------------------------------------------------------
wGRPx = ts_w * FTSx - ts_mvx
wGRPy = ts_w * FTSy - ts_mvy

plt.show()
