# Mathrix_Segfault_Dataset
The folder Mathrix Segfault consists of the following scripts:
Pandemic_Model.py: Runs an isotropic diffusion model for population growth to simulate a 20x20 sq km city's population. After that, it runs a diffusion with random coefficients at each 
time step to simulate a pandemic over 240 days. The numpy arrays cases(22, 22, 240), tot_cases(22, 22, 240) (for these i,j,t where 1 <= i, j <= 20 matter) and tot_pop(20, 20, 240)
(only tot_pop[i][j][k] k > 230 actually matters) are used in the main script Data_Generation_Script.py. Most of the other functions (plot_tot_cases, net_cases, etc. ) are auxiliary, 
generating heatmaps, looking at aggregates and debugging. (Anand Balivada)

blood_pressure.py: Has the function bloodpressure(age). A function of age, this gives the probability of having blood pressure. It is NOT a probability distribution, but a collection of 
probabilities whose sum isn't significant. (Param Nayar)

DiabDSv2-DDS.csv: This gives the probability of diabetes. It is similar to bloodpressure(age), except for a different comorbidity (Diabetes),
but isn't a function; a list of values. (Pragadeeshwar Kannan)

ProbabilityWRTAge.py: The function probabilityByAge(mu) is a probability distribution over age of covid patients, returning a list indexed by age. At any age A  this gives the 
proportion of cases where the patients are of age A. It is a Gaussian; sums to 1. (Harsh Modani)

Data_Generation_Script.py: The function deathval(x) gives the probability that a covid patient of age x dies of the disease (Dhanush Srikanth). 

The list resp is a normalized histogram of respiratory illnesses in covid patients, by age. (Krishna Singh) On dividing a value of this list by the respective probabilityByAge(mu)[age], one gets a probability similar to what is returned in bloopressure(age). 

This script distributes the number of new cases (Pandemic_Model.cases[i][j][t]) in an area by age, and assigns comorbidities and outcomes. Each entry [Time of infection, Time of reporting, 
x location, y location, Age, Diabetes, Respiratory, Blood Pressure, Outcome] is added to the file COVID_Dataset.csv, which thus forms a dataset of all COVID cases over days 0-239.
The file Population.csv consists of the population at each x,y, where 1<=x, y<=20. Since Each (x,y) represents the center of a 1 square kilometer region, averaging the population values 
actually gives the average population density of the city (basically the population values are population/sq km). 

