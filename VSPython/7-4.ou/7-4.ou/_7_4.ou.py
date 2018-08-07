
def print_design(unprinted_designs,print_designs):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("printing model:"+current_design)
        print_designs.append(current_design)

def show_completed_designs(print_designs):
    print("\nThis following models have been printed:")
    for completed_design in print_designs:
        print(completed_design)

unprinted_designs=["iphone case","robot pendant","katherine"]
print_designs=[]

print_design(unprinted_designs[:],print_designs)
show_completed_designs(print_designs)

print(unprinted_designs)
print(print_designs)