#Week4
#Knowledge Representation
from sympy import symbols, Not, Implies, Xor, And

# Define propositional variables
rained = symbols('rained')
visited_hagrid = symbols('visited_hagrid')
visited_dumbledore = symbols('visited_dumbledore')

# Define the logical expressions based on the given statements
statement1 = Implies(Not(rained), visited_hagrid)  # If it didn't rain, then Harry visited Hagrid today
statement2 = Xor(visited_hagrid, visited_dumbledore)  # Harry visited either Hagrid or Dumbledore, but not both
statement3 = visited_dumbledore  # Harry visited Dumbledore today

# Combine the statements into a single formula
combined_formula = And(statement1, statement2, statement3)

# Function to check consistency of the combined formula and print evaluations
def check_combined_consistency():
    # Evaluate all possible scenarios for rained and visited_hagrid
    possible_values = [True, False]
    consistent_scenarios = []

    for rained_value in possible_values:#true,false
        for visited_hagrid_value in possible_values:#true,false
            # Substitute the variable values into the combined formula
            results = {
                rained: rained_value,#t
                visited_hagrid: visited_hagrid_value,#f
                visited_dumbledore: True  # We know that Harry visited Dumbledore today
            }

            # Evaluate the logical statements individually
            eval_statement1 = statement1.subs(results)#t
            eval_statement2 = statement2.subs(results)#t
            eval_statement3 = statement3.subs(results)#t

            # Evaluate the combined formula
            eval_combined_formula = combined_formula.subs(results)#t

            # Print the evaluation of each statement and the combined formula
            print(f"rained={rained_value}, visited_hagrid={visited_hagrid_value}, visited_dumbledore=True")
            print(f"  Statement 1 (¬R → H) evaluates to: {eval_statement1}")
            print(f"  Statement 2 (H ⊕ D) evaluates to: {eval_statement2}")
            print(f"  Statement 3 (D) evaluates to: {eval_statement3}")
            print(f"  Combined Formula evaluates to: {eval_combined_formula}\n")

            # Append to consistent scenarios if the combined formula is true
            if eval_combined_formula:
                consistent_scenarios.append((rained_value, visited_hagrid_value))#t,f

    return consistent_scenarios

# Find consistent scenarios
consistent_scenarios = check_combined_consistency()#t,f

# Output consistent scenarios
print("Consistent scenarios based on the combined formula:")
if consistent_scenarios:#t,f
    for scenario in consistent_scenarios:
        rained_value, visited_hagrid_value = scenario#t,f
        print(f"rained={rained_value}, visited_hagrid={visited_hagrid_value}, visited_dumbledore=True")
else:
    print("No consistent scenarios found.")

# Output the combined formula for reference
print("\nCombined logical formula:")
print(combined_formula)
