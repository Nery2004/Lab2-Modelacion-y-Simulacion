using JuMP
using Ipopt
using HiGHS
using Optimization


#Define LP Model
model3 = Model()

#supuestos
costos = [50 50 20000 20;
          70 40 20 30;
          90 30 50 20000;
          70 20 60 70]

# Variables
@variable(model3, x[1:4, 1:4] >= 0, Bin)

#constraint
@constraint(model3, sum(x[1,j] for j in 1:4) == 1)
@constraint(model3, sum(x[2,j] for j in 1:4) == 1)
@constraint(model3, sum(x[3,j] for j in 1:4) == 1)
@constraint(model3, sum(x[4,j] for j in 1:4) == 1)


@constraint(model3, sum(x[i,1] for i in 1:4) == 1)
@constraint(model3, sum(x[i,2] for i in 1:4) == 1)
@constraint(model3, sum(x[i,3] for i in 1:4) == 1)
@constraint(model3, sum(x[i,4] for i in 1:4) == 1)


#objective function
@objective(model3, Min, sum(costos[i,j] * x[i,j] for i in 1:4, j in 1:4 ))

set_optimizer(model3, HiGHS.Optimizer)

optimize!(model3)


#print solution
print("x = ", value.(x), "\n")

print("objective value = ", objective_value(model3), "\n")