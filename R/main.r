#!/usr/bin/Rscript

dir <- '../out-sph/avec-ts/'
file <- paste(dir, 'kappa.dat', sep='')

courbureSPH <- scan(file, quiet=TRUE)
courbureSPH <- courbureSPH[-row(matrix(courbureSPH))[courbureSPH == 0]]

cat('Summary of curvature kappa (for non zero values).\n\n')
print(summary(courbureSPH))
x11()
hist(courbureSPH, col='yellowgreen')
locator(1)

# Extremum quantities
file <- paste(dir, 'ExtremumQuantities.csv', sep='')
extremum <- read.table(file, sep=',', skip=1)

# Fluid conservation
file <- paste(dir, 'FluidConservation.csv', sep='')
conservation <- read.table(file, sep=',', skip=1)

x11()
par(mfrow=c(2, 2))
plot(extremum$V1, extremum$V2, type='p', col='#1e4765', lwd=1, main='Vitesse max', xlab='time [s]', ylab='V')
grid()

plot(extremum$V1, extremum$V3, type='p', col='#1e4765', lwd=1, main='Mach max', xlab='time [s]', ylab='Mach')
grid()

plot(extremum$V1, extremum$V4, type='p', pch=3, col='#1e4765', lwd=1, main='Intervalle rho min - rho max', xlab='time [s]', ylab='rho')
lines(extremum$V1, extremum$V5, type='p', pch=4, col='#9a1d21', lwd=1)
grid()

plot(conservation$V1, conservation$V4, type='l', col='#9a1d21', lwd=3, main='Énergie cinétique', xlab='time [s]', ylab='EC')
grid()

dev.copy(pdf, '../graphs/quantities.pdf')
dev.off()

# attend que l'utilisateur clique sur la fenêtre
locator(1)
