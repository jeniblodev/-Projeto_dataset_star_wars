import matplotlib.pyplot as plt

labels = ('Human','Droid','Wookiee','Yodas species','Gungan')
sizes = [5, 2, 1, 1, 1]
colors = ['#48D1CC', '#90EE90', '#F4A460', '#FA8072', '#D8BFD8']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.0f%%', startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.title('Espécie dos Personagens de Star Wars - Amostragem de 10 itens')
plt.axis('equal')
plt.show()
