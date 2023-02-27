# Aula Prática 01: Mix de Produção

## Exercício 1

### Descrição do problema
Uma fundição tem de produzir 10 toneladas de um tipo de liga metálica e, para isso, tem disponível: lingotes de ferro, grafite e sucata. Dois componentes são relevantes para a liga: carbono e silício. As tabelas a seguir fornecem a fração, em termos percentuais, desses elementos nos ingredientes disponíveis, seus custos unitários, bem como a composição da liga (isto é, porcentagens mínimas e máximas de cada componente da liga).

Frações dos elementos (%) nos ingredientes e custo dos ingredientes (R$/ton):

| | Lingotes | Grafite | Sucata |
|:---|:---:|:---:|:---:|
| Carbono | 0.5 | 90 | 9 |
| Silício | 14 | - | 27 |
| Custo | 90 | 180 | 25 |

Frações (%) mínima e máxima dos componentes na liga:

| | min | max |
|:---|:---:|:---:|
|Carbono | 0.0 | 9.5 |
|Silício | 19 | 20 |


Escreva um modelo de otimização linear para determinar as quantidades dos ingredientes para compor a liga metálica, de modo que as especificações técnicas sejam satisfeitas e o custo seja mínimo.

### Resolução

**Cria** modelo

$x_i$: quantidade, em toneladas, do ingrediente $i$ usado na liga

$$\min c_l x_l + c_g x_g + c_s x_s$$

Sujeito a:

$$x_l + x_g + x_s = Q$$

$$n_c Q \leq a_{lc} x_l + a_{gc} x_g + a_{sc} x_s \leq m_c Q$$
$$n_s Q \leq a_{ls} x_l + a_{gs} x_g + a_{ss} x_s \leq m_s Q$$
$$x_l, x_g, x_s \geq 0$$

# Resultado esperado

\Problem name: 

Minimize
OBJROW: 90 x_l + 180 x_g + 25 x_s
Subject To
constr(0):  x_l + x_g + x_s = 10
constr(1):  0.00500 x_l + 0.90000 x_g + 0.09000 x_s >= -0
constr(2):  0.00500 x_l + 0.90000 x_g + 0.09000 x_s <= 0.95000
constr(3):  0.14000 x_l + 0.27000 x_s >= 1.90000
constr(4):  0.14000 x_l + 0.27000 x_s <= 2
Bounds
End

# Resultado esperado

Status =  OptimizationStatus.OPTIMAL
Solution value  = 600.00

Solution:
x_l = 5.38
x_g = 0.00
x_s = 4.62

## Exercício 2

Agora considere que os ingredientes tem o estoque limitado, de acordo com a tabela abaixo.

| | Lingotes | Grafite | Sucata |
|:---|:---:|:---:|:---:|
| Estoque (ton) | 5 | 5 | 12 |

Como o modelo pode ser modificado para atender a esse requisito?

**Cria** modelo

Adicionamos as seguintes restrições ao modelo anterior:

$$x_l \leq e_l$$
$$x_g \leq e_g$$
$$x_s \leq e_s$$

# Resultado esperado

\Problem name: 

Minimize
OBJROW: 90 x_l + 180 x_g + 25 x_s
Subject To
constr(0):  x_l + x_g + x_s = 10
constr(1):  0.00500 x_l + 0.90000 x_g + 0.09000 x_s >= -0
constr(2):  0.00500 x_l + 0.90000 x_g + 0.09000 x_s <= 0.95000
constr(3):  0.14000 x_l + 0.27000 x_s >= 1.90000
constr(4):  0.14000 x_l + 0.27000 x_s <= 2
constr(5):  x_l <= 5
constr(6):  x_g <= 5
constr(7):  x_s <= 12
Bounds
End

# Resultado esperado

Status =  OptimizationStatus.OPTIMAL
Solution value  = 603.70

Solution:
x_l = 5.00
x_g = 0.19
x_s = 4.81

## Exercício 3

Suponha agora que duas ligas metálicas devem ser preparadas e os mesmos ingredientes são utilizados em ambas. A liga especificada no Exercício 1 é referida como liga 1 e devem ser produzidas 10 toneladas desta liga. Da outra liga, referida como liga 2, devem ser produzidas 6 toneladas e suas composições mínima e máxima são dadas na tabela abaixo.

| | min | max |
|:---|:---:|:---:|
|Carbono | 0.00 | 40 |
|Silício | 12 | 19 |

**Cria** modelo

$x_{li}$: quantidade, em toneladas, do ingrediente $i$ usado na liga $l$

$$\min ((c_l x_{0l} + c_g x_{0g} + c_s x_{0s}) + (c_l x_{1l} + c_g x_{1g} + c_s x_{1s}))$$

Sujeito a:

$$x_{0l} + x_{0g} + x_{0s} = Q_0$$
$$x_{1l} + x_{1g} + x_{1s} = Q_1$$

$$n_{0c} Q_0 \leq a_{lc} x_{0l} + a_{gc} x_{0g} + a_{sc} x_{0s} \leq m_{0c} Q_0$$
$$n_{0s} Q_0 \leq a_{ls} x_{0l} + a_{gs} x_{0g} + a_{ss} x_{0s} \leq m_{0s} Q_0$$

$$n_{1c} Q_1 \leq a_{lc} x_{1l} + a_{gc} x_{1g} + a_{sc} x_{1s} \leq m_{1c} Q_1$$
$$n_{1s} Q_1 \leq a_{ls} x_{1l} + a_{gs} x_{1g} + a_{ss} x_{1s} \leq m_{1s} Q_1$$


$$x_{0l} + x_{1l} \leq e_l$$
$$x_{0g} + x_{1g} \leq e_g$$
$$x_{0s} + x_{1s} \leq e_s$$

$$x_{0l}, x_{0g}, x_{0s}, x_{1l}, x_{1g}, x_{1s} \geq 0$$

# Resultado esperado

\Problem name: 

Minimize
OBJROW: 90 x_0_l + 180 x_0_g + 25 x_0_s + 90 x_1_l + 180 x_1_g + 25 x_1_s
Subject To
constr(0):  x_0_l + x_0_g + x_0_s = 10
constr(1):  x_1_l + x_1_g + x_1_s = 6
constr(2):  0.00500 x_0_l + 0.90000 x_0_g + 0.09000 x_0_s >= -0
constr(3):  0.00500 x_0_l + 0.90000 x_0_g + 0.09000 x_0_s <= 0.95000
constr(4):  0.14000 x_0_l + 0.27000 x_0_s >= 1.90000
constr(5):  0.14000 x_0_l + 0.27000 x_0_s <= 2
constr(6):  0.00500 x_1_l + 0.90000 x_1_g + 0.09000 x_1_s >= -0
constr(7):  0.00500 x_1_l + 0.90000 x_1_g + 0.09000 x_1_s <= 2.40000
constr(8):  0.14000 x_1_l + 0.27000 x_1_s >= 0.72000
constr(9):  0.14000 x_1_l + 0.27000 x_1_s <= 1.14000
constr(10):  x_0_l + x_1_l <= 5
constr(11):  x_0_g + x_1_g <= 5
constr(12):  x_0_s + x_1_s <= 12
Bounds
End

# Resultado esperado

Status =  OptimizationStatus.OPTIMAL
Solution value  = 1029.26

Solution:
x_0_l = 4.32
x_0_g = 0.51
x_0_s = 5.17
x_1_l = 0.68
x_1_g = 1.45
x_1_s = 3.87
