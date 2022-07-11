import os

with open('data/regression/regression_ridge.csv', 'w') as f:
    f.write('State,1st degree,2nd degree,3rd degree\n')
with open('data/regression/regression_lasso.csv', 'w') as f:
    f.write('State,1st degree,2nd degree,3rd degree\n')

for state in os.listdir('data/states'):
    if state in ["NEW JERSEY", "NEW YORK", "WEST VIRGINIA", "COLORADO", "MINNESOTA", "MISSISSIPPI"]:
        continue
    with open(f'data/states/{state}/{state}_regression_1.txt', 'r') as f1:
        f1_lines = f1.readlines()
        with open(f'data/states/{state}/{state}_regression_2.txt', 'r') as f2:
            f2_lines = f2.readlines()
            with open(f'data/states/{state}/{state}_regression_3.txt', 'r') as f3:
                f3_lines = f3.readlines()
                with open('data/regression/regression_ridge.csv', 'a') as f_ridge:
                    f_ridge.write(f'{state},{f1_lines[2][:-1].split(":")[-1]},{f2_lines[2][:-1].split(":")[-1]},{f3_lines[2][:-1].split(":")[-1]}\n')
                with open('data/regression/regression_lasso.csv', 'a') as f_lasso:
                    f_lasso.write(f'{state},{f1_lines[11][:-1].split(":")[-1]},{f2_lines[11][:-1].split(":")[-1]},{f3_lines[11][:-1].split(":")[-1]}\n')