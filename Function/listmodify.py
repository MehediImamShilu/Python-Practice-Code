# modify the list using loop within the function

def print_model(unprinted_models, completed_models):
    while unprinted_models:
        # simulate printing each model, until none are left
        # append every model to the completed model
        copy_model = unprinted_models.pop()     # pop-up each element
        print("Printing model: " + copy_model.title())
        completed_models.append(copy_model)     # append the pop-up element


def show_completed_model(completed_models):     # show each append element
    print("\nThe completed models are given below: ")
    for models in completed_models:     # loop for pick each element
        print(models.title())


unprinted_models = ["car", "toy", "lego"]
completed_models = []

print_model(unprinted_models, completed_models)
show_completed_model(completed_models)
