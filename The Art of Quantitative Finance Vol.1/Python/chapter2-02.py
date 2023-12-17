import numpy as np
import matplotlib.pyplot as plt

K = 100
Ct = 10
ST = np.linspace(0, 250, 100)

payoff = - np.maximum(ST - K, 0)
profit = payoff + Ct

fig, ax = plt.subplots()
ax.set_title('Payoff (red) & Profit/Loss (green)')
ax.plot(ST, payoff, color='red')
ax.plot(ST, profit, color='green')
ax.set_xlim([np.min(ST), np.max(ST)])
ax.set_yticks([Ct, 0, np.min(payoff)], labels=['C(t)', 0.0, np.min(payoff)])
ax.axhline(0, color='gray', linewidth=0.5)
plt.savefig('fig.2.2.png')