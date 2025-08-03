# Universidad del Valle de Guatemala
# Modelacion y Simulación
# Laboratorio 2 - Ejercicio 1 apartado (a) & (b) & (c)

# Tres refinerías con capacidades diarias de 6, 5 y 8 millones de galones, respectivamente, abastecen a tres áreas de distribución
# con demandas diarias de 4, 8 y 7 millones de galones, respectivamente. La gasolina se transporta a las tres áreas de distribución
# a través de una red de oleoductos. El costo de transporte es de $0.10 por 1000 galones por kilómetro de oleoducto. En la
# tabla 1 se presenta la distancia en kilómetros entre las refinerías y las áreas de distribución. La refinería 1 no está conectada
# al área de distribución 3.

# Refinería 1:  Área 1: 120, Área 2: 180, Área 3: null
# Refinería 2:  Área 1: 300, Área 2: 100, Área 3: 80
# Refinería 3:  Área 1: 200, Área 2: 250, Área 3: 120

# a) Formular el modelo de transporte asociado.
# vars: x_ij, i = {1, 2, 3} (refinerías) y j = {1, 2, 3} (áreas de distribución)
# Parámetros:
#   Capacidades de suministro: S = [6, 5, 8] (millones de galones)
#   Demandas diarias: D = [4, 8, 7] (millones de galones)
#   Distancias (km): d_ij = [120, 180, 0; 300, 100, 80; 200, 250, 120]
#   Costo de transporte: c_ij = d_ij * ((0.10 USD)/(1000 gal/km)) * ((10^6 gal)/(millón gal)) = 100 d_ij USD por millón de galones
#   Minimizar el costo total de transporte: Z = Σ c_ij * x_ij
# Restricciones:
#   Oferta: Σ x_ij = S_i para cada i
#   Demanda: Σ x_ij = D_j para cada j
#   Conectividad: x_ij = 0 si no hay conexión entre i y j
#   No negatividad: x_ij >= 0

# b) Usando JuMP o PuLP, determine el programa de envíos óptimo en la red de distribución &
# c) Suponga ahora que la demanda diaria en el área 3 disminuye a 4 millones de galones. La producción excedente en las
#    refinerías 1 y 2 se envía a otras áreas de distribución por medio de camiones. El costo de transporte por 100 galones
#    es de $1.50 desde la refinería 1 y de $2.20 desde la refinería 2. La refinería 3 puede enviar su producción excedente a
#    otros procesos químicos dentro de la planta.
#    Formule y resuelva de nuevo el programa óptimo de envíos.
using JuMP
using HiGHS

offer = [6.0, 5.0, 8.0]
distances = [120.0 180.0  NaN;
             300.0 100.0  80.0;
             200.0 250.0 120.0]


camio_costo_default = nothing

function solve_transport(o::Vector{Float64}, d::Vector{Float64}, dist::Array{Float64,2}, camio_costo)
    model = Model(HiGHS.Optimizer)
    @variable(model, x[1:3,1:3] >= 0)
    @constraint(model, x[1,3] == 0)

    if camio_costo !== nothing
        @variable(model, y[1:2] >= 0)
        for i in 1:2
            @constraint(model, sum(x[i,j] for j in 1:3) + y[i] == o[i])
        end

        @constraint(model, sum(x[3,j] for j in 1:3) <= o[3])
    else
        for i in 1:3
            @constraint(model, sum(x[i,j] for j in 1:3) == o[i])
        end
    end

    for j in 1:3
        @constraint(model, sum(x[i,j] for i in 1:3) == d[j])
    end

    expr_pipe = sum((!isnan(dist[i,j]) ? dist[i,j]*100*x[i,j] : 0) for i in 1:3, j in 1:3)
    if camio_costo !== nothing
        expr_truck = camio_costo[1]*y[1] + camio_costo[2]*y[2]
        @objective(model, Min, expr_pipe + expr_truck)
    else
        @objective(model, Min, expr_pipe)
    end

    optimize!(model)

    println("envios por oleoducto (mill de galones):")
    for i in 1:3
        println([value(x[i,j]) for j in 1:3])
    end
    if camio_costo !== nothing
        println("envios en camion desde ref1 y ref2 (mill de galones): ", [value(y[i]) for i in 1:2])
    end
    println("costo total optimo (USD): ", objective_value(model), "\n")
end

demand_ab = [4.0, 8.0, 7.0]
println("a & b")
solve_transport(offer, demand_ab, distances, camio_costo_default)

demand_c = [4.0, 8.0, 4.0]
camio_costo = [1.5e4, 2.2e4]
println("c")
solve_transport(offer, demand_c, distances, camio_costo)