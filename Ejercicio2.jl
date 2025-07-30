using JuMP
using Ipopt
using HiGHS
using Optimization


#Define LP Model
model3 = Model()

#supuestos
costos = [3 8 2 10 3 3 9;
          2 2 7 6 5 2 7;
          5 6 4 5 6 6 6;
          4 2 7 5 9 4 7;
          10 3 8 4 2 3 5;
          3 5 4 2 3 7 8;
          0 0 0 0 0 0 0]

# Variables
@variable(model3, x[1:7, 1:7] >= 0, Bin)

#constraint
@constraint(model3, sum(x[1,j] for j in 1:7) == 1)
@constraint(model3, sum(x[2,j] for j in 1:7) == 1)
@constraint(model3, sum(x[3,j] for j in 1:7) == 1)
@constraint(model3, sum(x[4,j] for j in 1:7) == 1)
@constraint(model3, sum(x[5,j] for j in 1:7) == 1)
@constraint(model3, sum(x[6,j] for j in 1:7) == 1)
@constraint(model3, sum(x[7,j] for j in 1:7) == 1)


@constraint(model3, sum(x[i,1] for i in 1:7) == 1)
@constraint(model3, sum(x[i,2] for i in 1:7) == 1)
@constraint(model3, sum(x[i,3] for i in 1:7) == 1)
@constraint(model3, sum(x[i,4] for i in 1:7) == 1)
@constraint(model3, sum(x[i,5] for i in 1:7) == 1)
@constraint(model3, sum(x[i,6] for i in 1:7) == 1)
@constraint(model3, sum(x[i,7] for i in 1:7) == 1)

#objective function
@objective(model3, Min, sum(costos[i,j] * x[i,j] for i in 1:7, j in 1:7 ))

set_optimizer(model3, HiGHS.Optimizer)

optimize!(model3)


#print solution
print("x = ", value.(x), "\n")

print("objective value = ", objective_value(model3), "\n")