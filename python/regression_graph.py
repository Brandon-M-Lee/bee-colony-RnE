import os
os.system('pip3 install -r requirements.txt')
import matplotlib.pyplot as plt

x = ['1st degree', '2nd degree', '3rd degree']

for state in os.listdir('data/states'):
    if state in ["NEW JERSEY", "NEW YORK", "WEST VIRGINIA", "COLORADO", "MINNESOTA", "MISSISSIPPI"]:
        continue
    with open(f'data/states/{state}/{state}_regression_1.txt', 'r') as f1:
        with open(f'data/states/{state}/{state}_regression_2.txt', 'r') as f2:
            with open(f'data/states/{state}/{state}_regression_3.txt', 'r') as f3:
                plt.plot(x, [float(f1.readlines()[2][:-1].split(':')[-1]), float(f2.readlines()[2][:-1].split(':')[-1]), float(f3.readlines()[2][:-1].split(':')[-1])], label=state)

plt.legend()
plt.title('ridge regression')
plt.savefig('data/regression/regression_ridge.png')
plt.clf()

for state in os.listdir('data/states'):
    if state in ["NEW JERSEY", "NEW YORK", "WEST VIRGINIA", "COLORADO", "MINNESOTA", "MISSISSIPPI"]:
        continue
    with open(f'data/states/{state}/{state}_regression_1.txt', 'r') as f1:
        with open(f'data/states/{state}/{state}_regression_2.txt', 'r') as f2:
            with open(f'data/states/{state}/{state}_regression_3.txt', 'r') as f3:
                plt.plot(x, [float(f1.readlines()[11][:-1].split(':')[-1]), float(f2.readlines()[11][:-1].split(':')[-1]), float(f3.readlines()[11][:-1].split(':')[-1])], label=state)

plt.legend()
plt.title('lasso regression')
plt.savefig('data/regression/regression_lasso.png')