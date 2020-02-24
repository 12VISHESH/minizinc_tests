from minizinc import Instance, Model, Solver
gecode = Solver.lookup("gecode")

trivial = Model()
trivial.add_string(
    """
    var 1..10: x;
    constraint (x mod 2) = 1;
    solve ::int_search([x], input_order, indomain_min) maximize x;
    """
)
instance = Instance(gecode, trivial)

# Find and print all intermediate solutions
result = instance.solve(intermediate_solutions=True)
for i in range(len(result)):
    print(result[i, "x"])
