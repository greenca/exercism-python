from constraint import *

def solution():
    
    # New constraint problem
    problem = Problem()
    
    # Groups of properties
    colours = ['red', 'green', 'ivory', 'yellow', 'blue']
    nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian']
    pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
    beverages = ['coffee', 'tea', 'milk', 'orange juice', 'water']
    cigarettes = ['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments']
    
    properties = [colours, nationalities, pets, beverages, cigarettes]
    
    
    # Add all properties as variables to constraint problem, 
    # with values corresponding to house number (all different in a property group)
    for group in properties:
        problem.addVariables(group, range(5))
        problem.addConstraint(AllDifferentConstraint(), group)
    
    
    # Known values
    value_constraints = [['milk', 2],       # 9. Milk is drunk in the middle house.
                         ['Norwegian', 0]]  # 10. The Norwegian lives in the first house.
    
    for name, val in value_constraints:
        problem.addConstraint(InSetConstraint([val]), [name])
    
    
    # Pairs of properties that occur at the same house
    pair_constraints = [['Englishman', 'red'],            # 2. The Englishman lives in the red house.
                        ['Spaniard', 'dog'],              # 3. The Spaniard owns the dog.
                        ['coffee', 'green'],              # 4. Coffee is drunk in the green house.
                        ['Ukrainian', 'tea'],             # 5. The Ukrainian drinks tea.
                        ['Old Gold', 'snails'],           # 7. The Old Gold smoker owns snails.
                        ['Kools', 'yellow'],              # 8. Kools are smoked in the yellow house.
                        ['Lucky Strike', 'orange juice'], # 13. The Lucky Strike smoker drinks orange juice.
                        ['Japanese', 'Parliaments']]      # 14. The Japanese smokes Parliaments.
    
    for pair in pair_constraints:
        problem.addConstraint(AllEqualConstraint(), pair)
    
    
    # Relative position constraints
    
    # 6. The green house is immediately to the right of the ivory house.
    problem.addConstraint(lambda g, i: g == i + 1, 
                          ('green', 'ivory'))
    
    # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
    problem.addConstraint(lambda C, f: C == f + 1 or C == f - 1, 
                          ('Chesterfields', 'fox'))
    
    # 12. Kools are smoked in the house next to the house where the horse is kept.
    problem.addConstraint(lambda K, h: K == h + 1 or K == h - 1,
                          ('Kools', 'horse'))
    
    # 15. The Norwegian lives next to the blue house.
    problem.addConstraint(lambda N, b: N == b + 1 or N == b - 1,
                          ('Norwegian', 'blue'))
    
    solution_dict =  problem.getSolutions()[0]
    
    for nat in nationalities:
        if solution_dict[nat] == solution_dict['water']:
            water_drinker = nat
        if solution_dict[nat] == solution_dict['zebra']:
            zebra_owner = nat
    
    return 'It is the %s who drinks the water.\nThe %s keeps the zebra.' % (water_drinker, zebra_owner)
