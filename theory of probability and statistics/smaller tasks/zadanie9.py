import pandas as pd
from scipy.stats import ttest_1samp

data = pd.read_csv('rp10-09a.csv',delimiter=';')
data = pd.Series(data["Czas"])

from scipy.stats import t


sample_mean = data.mean()
sample_std = data.std()


n = len(data)

confidence_level = 0.95
df = n - 1
critical_value = t.ppf((1 + confidence_level) / 2, df)

margin_of_error = critical_value * (sample_std / (n**0.5))
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Wyświetl wynik
print("Przedział ufności dla średniej:")
print(" Dolna granica:", lower_bound)
print(" Górna granica:", upper_bound)
# Poziom istotności (alfa)
alpha = 0.05

# Przeprowadź test hipotezy dla H0: µ = 2840
null_mean = 2840
t_statistic, p_value = ttest_1samp(data, null_mean)

print("Test dla H0: µ =", null_mean)
print("Wartość t-statystyki:", t_statistic)
print("Wartość p:", p_value)
print("Hipoteza", "jest odrzucana" if p_value < alpha else "nie jest odrzucana")
print()

# Przeprowadź test hipotezy dla H0: µ = 2850
null_mean = 2850
t_statistic, p_value = ttest_1samp(data, null_mean)

print("Test dla H0: µ =", null_mean)
print("Wartość t-statystyki:", t_statistic)
print("Wartość p:", p_value)
print("Hipoteza", "jest odrzucana" if p_value < alpha else "nie jest odrzucana")
print()

# Przeprowadź test hipotezy dla H0: µ = 2875
null_mean = 2875
t_statistic, p_value = ttest_1samp(data, null_mean)

print("Test dla H0: µ =", null_mean)
print("Wartość t-statystyki:", t_statistic)
print("Wartość p:", p_value)
print("Hipoteza", "jest odrzucana" if p_value < alpha else "nie jest odrzucana")
