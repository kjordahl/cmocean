'''
Standardized colormaps for oceanography plots.

Colormaps are available for:
    salinity, salt
    temperature, temp
    oxygen, o2
    chlorophyll, chl, chloro
    cdom, CDOM
    turbidity, turb
    PAR, par
    density, rho
    # the following haven't been vetted well yet:
    bathymetry, bathy
    speed, s
    velocity, vel, u, v
    vorticity, vort
    seasurface, freesurface, zeta, eta

Used tool from http://bids.github.io/colormap/ to redo colormaps to be more perceptually correct.
'''

# from matplotlib import cm, colors
import tools
import matplotlib
# import plotting
# import data
import numpy as np
import os

# __all__ = ['salinity', 'salt', 'temperature', 'temp', 'oxygen', 
#             'o2', 'chl', 'chloro', 'chlorophyll', 'cdom', 'CDOM', 
#             'turbidity', 'turb', 'PAR', 'par', 'density', 'rho', 
#             'option_d', 'optiond', 'cmall', 'cmall_unique']
# __all__ = ['salinity', 'salt', 'temperature', 'temp', 'oxygen', 
#             'o2', 'chl', 'chloro', 'chlorophyll', 'cdom', 'CDOM', 
#             'turbidity', 'turb', 'PAR', 'par', 'density', 'rho', 
#             'bathymetry', 'bathy', 'speed', 's', 'velocity', 'vel', 
#             'u', 'v', 'vorticity', 'vort', 'seasurface', 'freesurface', 
#             'zeta', 'eta', 'option_d', 'optiond']

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')


def make_salinity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Salinity-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Salinity'
    cmap.units = 'g/kg'
    cmap.author = 'kmt'
    return cmap


def make_temperature_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Temperature-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Temperature'
    cmap.units = 'C'
    cmap.author = 'kmt'
    return cmap


def make_oxygen_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Oxygen-rgb.txt'))
    # convert middle .2 to .8 of colormap to grayscale
    l = rgb.shape[0]
    num = l/5.
    rgb[num:l-num,0] = 0.2989*rgb[num:l-num,0] + 0.5870*rgb[num:l-num,1] + 0.1140*rgb[num:l-num,2]
    rgb[num:l-num,1] = rgb[num:l-num,0]
    rgb[num:l-num,2] = rgb[num:l-num,0]
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Oxygen'
    cmap.units = 'm/l'
    cmap.author = 'kmt'
    return cmap


def make_chlorophyll_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Chlorophyll-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    # cmap = tools.cmap(rgb[::-1], N=256)
    cmap.name = 'Chlorophyll'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_CDOM_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'CDOM-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    # cmap = tools.cmap(rgb[::-1], N=256)
    cmap.name = 'CDOM'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_turbidity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Turbidity-rgb.txt'))
    cmap = tools.cmap(rgb[::-1], N=256)
    cmap.name = 'Turbidity'
    cmap.units = 'NTU'
    cmap.author = 'kmt'
    return cmap


def make_PAR_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'PAR-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'PAR'
    cmap.units = 'W/m^2'
    cmap.author = 'kmt'
    return cmap


def make_density_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Density-rgb.txt'))
    cmap = tools.cmap(rgb[::-1], N=256)
    cmap.name = 'Density'
    cmap.units = 'kg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_bathymetry_cmap():  
    rgb = np.load(os.path.join(datadir, 'Bathymetry.npy'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Bathymetry' 
    cmap.units = 'm'
    cmap.author = 'kmt'
    return cmap

def make_speed_cmap():
    rgb = np.load(os.path.join(datadir, 'Speed.npy'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Speed'
    cmap.units = 'm/s'
    cmap.author = 'kmt'
    return cmap

# def make_velocity_cmap():
#     cmap = cm.BrBG #cm.PuOr
#     cmap.name = 'Velocity'
#     cmap.units = 'm/s'
#     cmap.author = 'kmt'
#     return cmap

# def make_vorticity_cmap():
#     cmap = cm.PiYG  # BrBG
#     cmap.name = 'Vorticity'
#     cmap.units = '1/s'
#     cmap.author = 'kmt'
#     return cmap

def make_freesurface_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Freesurface-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Free surface'
    cmap.units = 'm'
    cmap.author = 'kmt'
    return cmap

# def make_option_d_cmap():
#     rgb = np.load(os.path.join(datadir, 'option_d.npy'))
#     cmap = tools.cmap(rgb, N=256)
#     cmap.name = 'matplotlib option_d'
#     cmap.units = '[]'
#     cmap.author = 'eric firing'
#     return cmap    


salinity = make_salinity_cmap()
salt = make_salinity_cmap()
temperature = make_temperature_cmap()
temp = make_temperature_cmap()
oxygen = make_oxygen_cmap()
o2 = make_oxygen_cmap()
chl = make_chlorophyll_cmap()
chloro = make_chlorophyll_cmap()
chlorophyll = make_chlorophyll_cmap()
cdom = make_CDOM_cmap()
CDOM = make_CDOM_cmap()
turbidity = make_turbidity_cmap()
turb = make_turbidity_cmap()
PAR = make_PAR_cmap()
par = make_PAR_cmap()
density = make_density_cmap()
rho = make_density_cmap()
# bathymetry = make_bathymetry_cmap()
# bathy = make_bathymetry_cmap()
# speed = make_speed_cmap()
# s = make_speed_cmap()
# velocity = make_velocity_cmap()
# vel = make_velocity_cmap()
# u = make_velocity_cmap()
# v = make_velocity_cmap()
# vorticity = make_vorticity_cmap()
# vort = make_vorticity_cmap()
seasurface = make_freesurface_cmap()
freesurface = make_freesurface_cmap()
zeta = make_freesurface_cmap()
eta = make_freesurface_cmap()
# option_d = make_option_d_cmap()
# optiond = make_option_d_cmap()


def all_colormap_names(methods):
    '''Return all names available to refer to colormaps. 
    This includes duplicates.

    '''

    cmall = []
    cmnames = []

    # loop through all the methods
    for method in methods:

        # see if method is a colormap
        if type(eval(method)) == matplotlib.colors.LinearSegmentedColormap:
            # import pdb; pdb.set_trace()
            cmnames.append(method)  # add on colormap nickname

    return cmnames

cmnames = all_colormap_names(dir())


def all_colormaps(cmnames):
    '''All available colormaps with names

    '''

    cmallname = []
    cmall = []
    for cmname in cmnames:
        thisname = eval(cmname).name
        if thisname not in cmallname:
            cmall.append(eval(cmname))
            cmallname.append(thisname)

    return cmall


cmall = all_colormaps(cmnames)


if __name__ == '__main__':

    make_salinity_cmap()
    # pass