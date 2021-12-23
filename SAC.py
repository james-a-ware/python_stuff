
#SAC calculator

tank_vol = int(input('Your Cylinder Volume: '))
air_cons = int(input('Air you have consumed in L: '))
d_time = int(input('Your total dive time: '))
press = int(input('The max Atmospheric pressure experianced in BAR: '))

def sac_val(tank_vol,air_cons,d_time,press):
    return tank_vol*air_cons/d_time/press

sac_val()
