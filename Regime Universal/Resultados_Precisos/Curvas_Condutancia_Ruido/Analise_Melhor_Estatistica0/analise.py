import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
file_path = "Resultados_Fractal.xlsx"

# Leitura do arquivo Excel
df = pd.read_excel(file_path)

# Extração de cada coluna em uma lista
tipo_list = df['Tipo'].tolist()
ordem_list = df['Ordem'].tolist()
ensemble_list = df['Ensemble'].tolist()
alpha_list = df['alpha'].tolist()
beta_list = df['beta'].tolist()
gamma_list = df['gamma'].tolist()
lorentziana_list = df['Lorentziana'].tolist()
medicao_direta_list = df['Medição direta'].tolist()
erro_list = df['Erro %'].tolist()

'''
# Exibir as listas
print("Tipo:", tipo_list)
print("Ordem:", ordem_list)
print("Ensemble:", ensemble_list)
print("Alpha:", alpha_list)
print("Beta:", beta_list)
print("Gamma:", gamma_list)
print("Lorentziana:", lorentziana_list)
print("Medição Direta:", medicao_direta_list)
print("Erro %:", erro_list)
'''

newy1 = []
newx1 = []
newy2 = []
newx2 = []
newy3 = []
newx3 = []
for i in range(len(tipo_list)):
    if(ensemble_list[i] == 'beta1' and tipo_list[i] == 'Condutancia'):
        newx1.append(ordem_list[i])
        newy1.append(medicao_direta_list[i])
    if(ensemble_list[i] == 'beta2' and tipo_list[i] == 'Condutancia'):
        newx2.append(ordem_list[i])
        newy2.append(medicao_direta_list[i])
    if(ensemble_list[i] == 'beta4' and tipo_list[i] == 'Condutancia'):
        newx3.append(ordem_list[i])
        newy3.append(medicao_direta_list[i])

# Plot dos pontos
plt.scatter(newx1, newy1, label='Beta 1')
plt.scatter(newx2, newy2, label='Beta 2')
plt.scatter(newx3, newy3, label='Beta 4')

# Adicionando legendas e rótulos
plt.xlabel('Ordem', fontsize='15')
plt.ylabel('Densidade de máximos', fontsize='15')
plt.title('Condutancia', fontsize='20')
plt.legend(loc='best', fontsize='12')
plt.savefig('condutancia.png')
plt.show()



newy1 = []
newx1 = []
newy2 = []
newx2 = []
newy3 = []
newx3 = []
for i in range(len(tipo_list)):
    if(ensemble_list[i] == 'beta1' and tipo_list[i] == 'Ruído'):
        newx1.append(ordem_list[i])
        newy1.append(medicao_direta_list[i])
    if(ensemble_list[i] == 'beta2' and tipo_list[i] == 'Ruído'):
        newx2.append(ordem_list[i])
        newy2.append(medicao_direta_list[i])
    if(ensemble_list[i] == 'beta4' and tipo_list[i] == 'Ruído'):
        newx3.append(ordem_list[i])
        newy3.append(medicao_direta_list[i])

# Plot dos pontos
plt.scatter(newx1, newy1, label='Beta 1')
plt.scatter(newx2, newy2, label='Beta 2')
plt.scatter(newx3, newy3, label='Beta 4')

# Adicionando legendas e rótulos
plt.xlabel('Ordem', fontsize='15')
plt.ylabel('Densidade de máximos', fontsize='15')
plt.title('Ruido', fontsize='20')
plt.legend(loc='best', fontsize='12')
plt.savefig('Ruido.png')
plt.show()
