import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (6, 4)

K = 100
[Ct, Pt] = [10]*2
ST = np.linspace(0, 250, 100)

# Fig. 2.1 Payoff and profit function of a long call option
payoff = np.maximum(ST - K, 0)
profit = payoff - Ct

fig, ax = plt.subplots()
ax.set_title('Payoff (red) & Profit/Loss (green)')
ax.plot(ST, payoff, color='red')
ax.plot(ST, profit, color='green')
ax.set_xlim([np.min(ST), np.max(ST)])
ax.set_yticks([-Ct, 0, np.max(payoff)], labels=['-C(t)', 0.0, np.max(payoff)])
ax.axhline(0, color='gray', linewidth=0.5)
plt.savefig('img/fig.2.1.png')


# Fig. 2.2 Payoff and profit graph of a short call option
#payoff = - np.maximum(ST - K, 0)
#profit = payoff + Ct

fig, ax = plt.subplots()
ax.set_title('Payoff (red) & Profit/Loss (green)')
ax.plot(ST, -payoff, color='red')
ax.plot(ST, -profit, color='green')
ax.set_xlim([np.min(ST), np.max(ST)])
ax.set_yticks([Ct, 0, np.min(-payoff)], labels=['C(t)', 0.0, np.min(-payoff)])
ax.axhline(0, color='gray', linewidth=0.5)
plt.savefig('img/fig.2.2.png')


# Fig. 2.3 Payoff and profit graph of a long put option
payoff = np.maximum(K - ST, 0)
profit = payoff - Pt

fig, ax = plt.subplots()
ax.set_title('Payoff (red) & Profit/Loss (green)')
ax.plot(ST, payoff, color='red')
ax.plot(ST, profit, color='green')
ax.set_xlim([np.min(ST), np.max(ST)])
ax.set_yticks([-Pt, 0, np.max(payoff)], labels=['-P(t)', 0.0, np.max(payoff)])
ax.axhline(0, color='gray', linewidth=0.5)
plt.savefig('img/fig.2.3.png')


# Fig. 2.4 Payoff and profit function of a short put option
#payoff = - np.maximum(K - ST, 0)
#profit = payoff + Pt

fig, ax = plt.subplots()
ax.set_title('Payoff (red) & Profit/Loss (green)')
ax.plot(ST, -payoff, color='red')
ax.plot(ST, -profit, color='green')
ax.set_xlim([np.min(ST), np.max(ST)])
ax.set_yticks([Pt, 0, np.min(-payoff)], labels=['P(t)', 0.0, np.min(-payoff)])
ax.axhline(0, color='gray', linewidth=0.5)
plt.savefig('img/fig.2.4.png')

