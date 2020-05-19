import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

personagens = ('Chewbacca', 'Darth Vader', 'Jar Jar Binks', 'Obi-Wan Kenobi', 'Han Solo', 'Luke Skywalker', 'C-3PO', 'Leia Organa', 'R2-D2', 'Yoda')
indice = np.arange(len(personagens))
altura = [228,202,196,182,180,172,167,150,96,66]
plt.barh(indice, altura, color='#000000')
plt.yticks(indice, personagens)
plt.xlabel('Altura')
plt.ylabel('Nome dos Personagens')
plt.title('Altura dos Personagens de Star Wars - Amostragem de 10 itens')
plt.xticks(rotation=45)
plt.show()





