from mip import *

### Resolve o modelo e mostra os valores das variáveis
def solve(model):
    status = model.optimize()

    print("Status = ", status)
    print(f"Solution value = {model.objective_value:.2f}\n")

    print("Solution:")
    for v in model.vars:
        print(f"{v.name} = {v.x:.2f}")

### Salva modelo em arquivo lp, e mostra o conteúdo
def save(model, filename):
    model.write(filename) # Salva modelo em arquivo
    
    with open(filename, "r") as f: # Lê e exibe conteúdo do arquivo
        print(f.read())

### Dados de entrada
D = range(7)
e = [10, 6, 8, 5, 9, 4, 6]

def Dstar(d):
    p = d + 2 # Antes do primeiro dia

    for _ in range(5):
        p = (p + 1) % 7
        yield p

model = Model(sense=MINIMIZE, solver_name=CBC)

x = [model.add_var(var_type=INTEGER, name=f"x_{d + 1}", lb = 0) for d in D]

model.objective = xsum(x[d] for d in D)

for d in D:
    model += xsum(x[p] for p in Dstar(d)) >= e[d]

save(model, "model.lp")

solve(model)
