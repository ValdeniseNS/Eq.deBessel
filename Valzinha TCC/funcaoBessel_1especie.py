import numpy as np #importa a biblioteca numpy
import scipy.special as sp # importa a bibliotexa das funcoes especiais de BESSEL
import matplotlib.pyplot as plt 
x = np.linspace(0, 15, 500000)
for v in range(0, 2):
    #plt.plot(x, sp.jv(v, x)) # com esse comando pode plotar para a quantidade de v que especificou acima
    plt.plot (x, sp.jv(0,x), "b-", linewidth=1.5) # plota para o v que vc definir aqui
    plt.plot (x, sp.jv(1,x), "r--", linewidth=2.5) # plota para o v que vc definir aqui
plt.xlim((0, 13)) #eixo x varia de 0 a 13
plt.ylim((-0.5, 1.1)) # eixo y varia de -5 a 1.1
plt.legend(('$\mathcal{J}_0(x)$', '$\mathcal{J}_1(x)$'),
           loc = 0)
plt.xlabel('$x$')
plt.subplots_adjust(left=0.12, right=0.94, top=0.72, bottom=0.13)
#plt.ylabel('$\mathcal{J}_n(x)$')
#py.title('funcao de Bessel')                                
plt.grid(False)
#Salvar Figura
figura = 'FuncoesdeBesselPrimeiraEspecie'
figura=figura.replace ('.', ',')
figura=figura+'.pdf'
plt.savefig(figura)
print(figura)
plt.show()
