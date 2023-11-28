class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, variable, color):
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  

        unassigned_variables = [var for var in self.variables if var not in assignment]

        first_unassigned = unassigned_variables[0]
        for value in self.domains[first_unassigned]:
            if self.is_consistent(assignment, first_unassigned, value):
                assignment[first_unassigned] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[first_unassigned]  

        return None  

def main():
    
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    colors = ['Red', 'Green', 'Blue']

    map_csp = MapColoringCSP(variables=regions, domains={r: colors for r in regions}, constraints=neighbors)

    solution = map_csp.backtracking_search()

    if solution:
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
