!pip install mip

from mip import *

# composição de cada ingrediente
a = {
    'l': {'c': 0.005, 's': 0.14},
    'g': {'c': 0.9,   's': 0.0},
    's': {'c': 0.09,  's': 0.27},
}

# custo
c = {'l': 90, 'g': 180, 's': 25}

# composições mínimas e máximas dos componentes
n = {'c': 0.0, 's': 0.19}  # min
m = {'c': 0.095, 's': 0.2} # max

# quantidade desejada da liga
Q = 10

# exercício 1

# criando modelo

model = Model(sense=MINIMIZE, solver_name=CBC)

# criação/adição da variável no modelo
x = {i: model.add_var(var_type=CONTINUOUS, name=f'x_{i}', lb=0.0) for i in  ['l', 'g', 's']}

# função objetivo
model.objective = c['l']*x['l'] + c['g']*x['g'] + c['s']*x['s']

# a soma dos ingredientes usados deve ser igual a Q
model += x['l'] + x['g'] + x['s'] == Q

# restrição na quantidade de Carbono na liga
carbono = a['l']['c']*x['l'] + a['g']['c']*x['g'] + a['s']['c']*x['s']
model += n['c']*Q <= carbono
model += carbono <= m['c']*Q

# restrição na quantidade de Silicio na liga
silicio = a['l']['s']*x['l'] + a['g']['s']*x['g'] + a['s']['s']*x['s']
model += n['s']*Q <= silicio
model += silicio <= m['s']*Q

model.write("model.lp") # salva modelo em arquivo

with open("model.lp") as f: # lê e exibe conteúdo do arquivo
    print(f.read())

# executa

def solve(model):
  status = model.optimize()

  print("Status = ", status)
  print(f"Solution value  = {model.objective_value:.2f}\n")
  
  print("Solution:")
  for v in model.vars:
      print(f"{v.name} = {v.x:.2f}")

solve(model)

# exercício 2

# estoque
e = {'l': 5, 'g': 5, 's': 12}

# criando modelo

model += x['l'] <= e['l']
model += x['g'] <= e['g']
model += x['s'] <= e['s']

model.write("modelo2.lp") # salva modelo em arquivo
with open("modelo2.lp") as f: # Lê e exibe conteúdo do arquivo
    print(f.read())

# executa

solve(model)

# exercício 3

# carregando dados

# composições mínimas e máximas dos componentes
n = [{'c': 0.0, 's': 0.19}, {'c': 0.0, 's': 0.12}]
m = [{'c': 0.095, 's': 0.2}, {'c': 0.4, 's': 0.19}]

# quantidade desejada da liga
Q = [10, 6]

# criando modelo

model = Model(sense=MINIMIZE, solver_name=CBC)

# criação/adição da variável no modelo
x = [{i: model.add_var(name=f'x_{l}_{i}') for i in ['l', 'g', 's']} for l in range(2)]

# função objetivo
model.objective = c['l']*x[0]['l'] + c['g']*x[0]['g'] + c['s']*x[0]['s'] + c['l']*x[1]['l'] + c['g']*x[1]['g'] + c['s']*x[1]['s']

# a soma dos ingredientes usados na liga 0 deve ser igual a Q0
model += x[0]['l'] + x[0]['g'] + x[0]['s'] == Q[0]

# a soma dos ingredientes usados na liga 1 deve ser igual a Q1
model += x[1]['l'] + x[1]['g'] + x[1]['s'] == Q[1]

# restrição na quantidade de Carbono na liga 0
carbono = a['l']['c']*x[0]['l'] + a['g']['c']*x[0]['g'] + a['s']['c']*x[0]['s']
model += n[0]['c']*Q[0] <= carbono
model += carbono <= m[0]['c']*Q[0]

# restrição na quantidade de Silicio na liga 0
silicio = a['l']['s']*x[0]['l'] + a['g']['s']*x[0]['g'] + a['s']['s']*x[0]['s']
model += n[0]['s']*Q[0] <= silicio
model += silicio <= m[0]['s']*Q[0]

# restrição na quantidade de Carbono na liga 1
carbono = a['l']['c']*x[1]['l'] + a['g']['c']*x[1]['g'] + a['s']['c']*x[1]['s']
model += n[1]['c']*Q[1] <= carbono
model += carbono <= m[1]['c']*Q[1]

# restrição na quantidade de Silicio na liga 1
silicio = a['l']['s']*x[1]['l'] + a['g']['s']*x[1]['g'] + a['s']['s']*x[1]['s']
model += n[1]['s']*Q[1] <= silicio
model += silicio <= m[1]['s']*Q[1]

# restrições de estoque
model += x[0]['l'] + x[1]['l'] <= e['l']
model += x[0]['g'] + x[1]['g'] <= e['g']
model += x[0]['s'] + x[1]['s'] <= e['s']

model.write("modelo3.lp") # salva modelo em arquivo
with open("modelo3.lp") as f: # lê e exibe conteúdo do arquivo
    print(f.read())

# executa

solve(model)
