import numpy as np
import matplotlib.pyplot as plt

K = 100
Ct = Pt = 10
ST = np.linspace(0, 200, 100)
positions = ['long', 'short']
types = ['call', 'put']
payoffs = [np.maximum(ST - K, 0), np.maximum(K - ST, 0)] # long call/put
maxpayoffs = [np.max(ST - K), np.max(K - ST)] # long call/put

fig, ax = plt.subplots(2,2, figsize=(8, 8), sharex=True)
fig.suptitle('Payoff (red) & Profit/Loss (green)')
for i in range(2): # long/short
	for j in range(2): # call/put
		payoff = [1,-1][i] * payoffs[j]
		profit = payoff + [-1,1][i] * [Ct, Pt][j]
		ax[i,j].set_title("European " + positions[i] + " " + types[j])
		ax[i,j].plot(ST, payoff, color='red')
		ax[i,j].plot(ST, profit, color='green')
		ax[i,j].axhline(0, color='gray', linewidth=0.5)
		ax[i,j].set_yticks(
        	[[-1,1][i] * [Ct, Pt][j], 0, [1,-1][i] * maxpayoffs[j]], 
        	labels = [['-',''][i] + ['C(t)','P(t)'][j], 0.0, [1,-1][i] * maxpayoffs[j]]
        	)
ax[0,0].set_xlim([np.min(ST), np.max(ST)])
plt.savefig('img/01_EuropeanOptions.png')