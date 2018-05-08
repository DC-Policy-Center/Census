


# Data needed
- Population by tract
- Centroid of tract in lat/lon



# Psudo-code

load in libraries

pop_read(t(#)) = local load of tract, as a tract number, Population

pop(v,x,y) = cent_correct(t(#),pop_read(t)) # gives population(value,lat,lon) outputs
