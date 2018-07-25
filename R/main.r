#!/usr/bin/Rscript

dir <- '../out-sph/avec-ts/'
file <- paste(dir, 'kappa.dat', sep='')

courbureSPH <- scan(file, quiet=TRUE)
courbureSPH <- courbureSPH[-row(matrix(courbureSPH))[courbureSPH == 0]]

cat('Summary of curvature kappa (for non zero values).\n\n')
print(summary(courbureSPH))
