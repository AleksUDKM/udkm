# -*- coding: utf-8 -*-

import numpy as np
import udkm.tools.helpers as h

teststring = "Successfully loaded udkm.moke.functions"

# initialize some useful functions
t0 = 0    # Estimated value of t0
data_path = "data/"
export_path = "results/"


def load_data(date, time, voltage, col_to_plot):
    file = data_path + str(date) + "_" + h.timestring(time) 
	+ "/Fluence/-1.0/" + str(voltage) + "/overviewData.txt"
    data = np.genfromtxt(file, comments="#")
    return(data[:, 0], data[:, col_to_plot])


def load_data_A(date, time, angle, col_to_plot):
    file = data_path+str(date)+"_"+h.timestring(time)+"/Fluence/"+str(int(angle))+"/1.0"+"/overviewData.txt"
    data = np.genfromtxt(file, comments="#")
    return(data[:, 0], data[:, col_to_plot])


def load_data_B(date, time, angle, col_to_plot):
    file = data_path+str(date)+"_"+h.timestring(time)+"/Fluence/"+str(angle)+"/1.0"+"/overviewData.txt"
    data = np.genfromtxt(file, comments="#")
    return(data[:, 0], data[:, col_to_plot])


def load_data_reflectivity(date, time, voltage, col_to_plot):
    file = data_path+str(date)+"_"+h.timestring(time)+"/Fluence/-1.0/"+str(voltage)+"/dataBplus.txt"
    data = np.genfromtxt(file, comments="#")
    return(data[:, 0], data[:, col_to_plot])


def load_data_hysteresis(date, time, name):
    file = data_path+str(date)+"_"+h.timestring(time)+"/Fluence/Static/"+name+"_NoLaser.txt"
    data = np.genfromtxt(file, comments="#")
    return(data[:, 0], data[:, 1], data[:, 2])
