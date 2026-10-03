import app_funcs

my_recipe = app_funcs.Recipe("Przepis na chrupiące frytki z air fryera w 10min",
                             "Frytki z air fryera", "Rozpakuj opakowanie i wsyp frytki do airfryera, wstaw na 10min 180 st.",
                             "Frytki do airfryera", "Airfryer"
                            )
print(my_recipe.__str__())