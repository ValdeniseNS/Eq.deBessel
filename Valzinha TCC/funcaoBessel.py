# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Dipole Field
"""
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
#parametros
n=0
n1=1
om0=1.0
xMin= 1.0*om0
xMax=12.0*om0
delta = (xMax-xMin)/120
x = np.arange(xMin, xMax, delta)
#funcao N_s indice espectral potencial K
J=np.sqrt(2/(np.pi*x))*np.cos(x-(n*np.pi/2)-np.pi/4)
J1=np.sqrt(2/(np.pi*x))*np.cos(x-(n1*np.pi/2)-np.pi/4)
matplotlib.rc('font', size= 14)
#matplotlib.rc('font', **{'sans-serif' : 'Arial',
#                               'family' : 'sans-serif'})
plt.plot (x, J, "g-", linewidth=1.5, label="$J_0$")
plt.plot (x, J1, "r--", linewidth=1.5, label="$J_1$")
#limites
plt.xlim (xMin, 13)
plt.ylim (-0.5, 1.0)
plt.xlabel ("$x$")
titulo=u"Funcion"  
#plt.title (titulo)
# Ajustar o tamanho relativo da figura
plt.subplots_adjust(left=0.12, right=0.94, top=0.81, bottom=0.13)
# Onde colocar as legendas
plt.legend(bbox_to_anchor=(0.8, 0.8), loc=2, borderaxespad=0.0, frameon=True)
#salvar figura
figura = 'FuncaoBessel1'
figura=figura.replace ('.', ',')
figura=figura+'.pdf'
plt.savefig(figura)
print(figura)
plt.show()
