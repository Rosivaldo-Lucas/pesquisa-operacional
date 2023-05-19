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

model = Model(sense=MINIMIZE, solver_name=CBC)

x = [None] + [model.add_var(var_type=INTEGER, name=f"x_{i}", lb=0) for i in range(1, 5)]

model.objective = x[1] + x[2] + x[3] + x[4]

model += 3*x[1] + x[2] + x[3] >= 50
model += x[2] + 2*x[4] >= 60
model += x[3] >= 90

save(model, "model2.lp")

solve(model)
