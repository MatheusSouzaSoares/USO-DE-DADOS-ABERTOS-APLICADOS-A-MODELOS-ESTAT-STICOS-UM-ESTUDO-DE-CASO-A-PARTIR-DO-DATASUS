from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import ETL

# Obtendo as variáveis x e y da função ETL.get_variables()
x, y = ETL.get_variables()

# Calculando a linha de regressão linear
reg = LinearRegression().fit(x.reshape(-1, 1), y)
r = reg.coef_[0]

# Plotando o gráfico de dispersão com a linha de regressão linear
plt.scatter(x, y)
plt.plot(x, reg.predict(x.reshape(-1, 1)), color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Gráfico de dispersão com linha de regressão linear (r={r:.2f})")
plt.show()