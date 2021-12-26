"""
TCRE Climate Simulation

By: Mitchell Dickau
- Uses best estimate of the TCRE 1.65°C/1000 PgC
- Only simulates warming from CO2
"""
import matplotlib.pyplot as plt
import numpy as np

# Function to create list of range of values
def createList(n1, n2, int):
    return np.arange(n1, n2+1, int)

# Function creates CO2 pathway and ∆T pathway 
def CO2_pathway(timestep, interval):
    # CO2 pathway
    path_CO2 = []
    for x in timestep:
        if x == 2020:
            pre_val= 40 
            path_CO2.append(pre_val)
            continue 
        pre_val += interval
        if pre_val < 0:
            pre_val = 0
        path_CO2.append(pre_val)
    # ∆T pathway
    path_T = [1.2] 
    for n in range(1,len(path_CO2)):
        temp = sum(path_CO2[1:n+1])/3.664*1.65/1000+1.2
        path_T.append(temp)
    return (path_CO2, path_T)


if __name__ == '__main__':
    # Create year var
    year = createList(2020, 2100, 1)
    # Create CO2 pathways 
    CO2_up = CO2_pathway(year, 0.5)
    CO2_down = CO2_pathway(year, -0.5)
    CO2_fastdown = CO2_pathway(year, -1.3)
    CO2_stable = CO2_pathway(year, 0)

    pathways = {'year':year, 'up':CO2_up, 'down':CO2_down, 
                'fastdown':CO2_fastdown, 'stable':CO2_stable}

    ### Plot emissions and ∆T pathways 
    em = ['up','stable','down','fastdown']
    cols= ['red','orange','gold','blue']

    # Two plots
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Temperature response to CO2 pathways')

    # CO2 pathway
    for n in range(0,len(em)):
        ax1.plot(pathways['year'], pathways[em[n]][0], color= cols[n])
    # ∆T pathway
    for n in range(0,len(em)):
        ax2.plot(pathways['year'], pathways[em[n]][1], color= cols[n])

    ax1.set(xlabel='Year', ylabel='Gt CO2')
    ax2.set(xlabel='Year', ylabel='°C')

    ax1.grid(color = 'grey', linestyle = '--', linewidth = 0.25)
    ax2.grid(color = 'grey', linestyle = '--', linewidth = 0.25)

    fig.tight_layout()
    fig.savefig('TCRE_sim.png', dpi=300, facecolor='white',
                transparent=False, bbox_inches='tight')