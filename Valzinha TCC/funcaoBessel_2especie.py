import numpy as np #importa a biblioteca numpy
import pylab as py # importa o pylab para plotar
import scipy.special as sp # importa a bibliotexa das funcoes especiais de BESSEL
import matplotlib.pyplot as plt 
x = np.linspace(0, 10, 500000)
for v in range(0, 2):
    #plt.plot(x, sp.yv(v, x)) # com esse comando pode plotar para a quantidade de v que especificou acima
    plt.plot (x, sp.yv(0,x), "b-", linewidth=1.5, label="$J_0$") # plota para o v que vc definir aqui
    plt.plot (x, sp.yv(1,x), "r--", linewidth=2.5, label="$J_0$") # plota para o v que vc definir aqui
plt.xlim((0, 11)) #eixo x varia de 0 a 13
plt.ylim((-0.6, 0.6)) # eixo y varia de -5 a 1.1
plt.legend(('${Y}_0(x)$', '${Y}_1(x)$'),
           loc = 0)
plt.xlabel('$x$')
plt.subplots_adjust(left=0.12, right=0.94, top=0.72, bottom=0.13)
#plt.ylabel('$\mathcal{J}_n(x)$')
#py.title('funcao de Bessel')                                
plt.grid(False)
#Salvar Figura
figura = 'FuncoesdeBesselSegundaEspecie'
figura=figura.replace ('.', ',')
figura=figura+'.pdf'
plt.savefig(figura)
print(figura)
plt.show()
