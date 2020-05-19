import matplotlib.pyplot as plt
import squarify   
 
squarify.plot(sizes=[19,1,62,5], label=["Female", "Hermaphrodite", "Male", "NA / None"], color=['#008000', '#6495ED', '#F4A460', '#D8BFD8'], alpha=.5)
plt.title('Sexo dos Personagens de Star Wars - Dataset completo')
plt.axis('off')
plt.show()


