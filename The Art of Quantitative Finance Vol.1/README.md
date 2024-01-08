# The Art of Quantitative Finance Vol.1

Volume 1 is the first of a 3 volumne series including:

1. Trading, Derivatives and Basic Concepts
2. Volatilities, Stochastic Analysis and Valuation Tools
3. Risk, Optimal Portfolios and Case Studies

Volume 1 contains 3 chapters. The first one is more like an introduction. So we start directly from chapter 2

The book is kind of informal, so notes will be just listed as bullets

## Chapter 2. Derivatives and Trading in Derivatives, Basic Concepts and Strategies

### 2.1. What Is a Derivative?

- A derivative (financial product) is a financial product that derives its value from another financial product.
- The financial product A from which a particular derivative D is derived is referred to as the “underlying asset” of D.

### 2.2. European Plain-Vanilla Options, Definition and Basic Characteristics

- “Plain-vanilla” options are standard options with no special features.
- Options can be [for this book]: call & put, american & european, and have long & short positions.
- **Long position** or going long: *buy*, because we have to pay a premium.
- **Short position** or going short: *sell*, because we receive payment of a premium

> The holder of a long/short position in a **European** call/put option on the underlying asset A with expiration date T and strike price K receives/pays a **Payoff** at time T. Since that holder initially purchased/selled the option at the price $C(t_0)/P(t_0)$, the profit (loss) from the option position is **Profit**

| Position\Type | European Call | European Put |
| :------------ | ---- | --- |
| Long          | Payoff = $\max(S(T)−K, 0)$ <br/> Profit = $\max(S(T) − K, 0) − C(t_0)$ | Payoff = $\max(K-S(T), 0)$ <br/> Profit = $\max(K-S(T), 0) − P(t_0)$ |
| Short         | Payoff = $-\max(S(T)−K, 0)$ <br/> Profit = $-\max(S(T) − K, 0) + C(t_0)$ | Payoff = $-\max(K-S(T), 0)$ <br/> Profit = $-\max(K-S(T), 0) + P(t_0)$ |

![Payoff and profit function](Python/img/01_EuropeanOptions.png "Payoff and profit function")

- **OTM** (out of the money): no significant payoff (payoff = 0) when exercised immediately
- **ATM** (at the money): payoff ≈ 0 (St ≈ K)
- **ITM** (in the money): significant payoff (payoff >> 0) when exercised immediately

### 2.3. American Options

- American option: option to exercise at any point (only once) until expiration T

> The holder of a long/short position in a **American** call/put option on the underlying asset A with expiration date T and strike price K receives/pays a **Payoff** at any chosen time $t_1 \le T$. Since that holder initially purchased/selled the option at the price $C(t_0)/P(t_0)$, the profit (loss) from the option position is **Profit**

| Position\Type | American Call | American Put |
| :------------ | ---- | --- |
| Long          | Payoff = $\max(S(t_1)−K, 0)$ <br/> Profit = $\max(S(t_1) − K, 0) − C(t_0)$ | Payoff = $\max(K-S(t_1), 0)$ <br/> Profit = $\max(K-S(t_1), 0) − P(t_0)$ |
| Short         | Payoff = $-\max(S(t_1)−K, 0)$ <br/> Profit = $-\max(S(t_1) − K, 0) + C(t_0)$ | Payoff = $-\max(K-S(t_1), 0)$ <br/> Profit = $-\max(K-S(t_1), 0) + P(t_0)$ |

### 2.4. Any Strategy Is Better than No Strategy and “The Secretary Problem”

- The idea of this section is to *show* that having a strategy is better than not having one. The games presentend are not usefull later

#### Simple game with 2 players and $n$ options (professional version, aka 'The Secretary Problem'):
- Player A writes $n$ different numbers ($Z_1, ..., Z_n$) in $n$ notes. The notes are shuffled
- Note 1 is uncovered and Player B decides whether or not to take Note 1
- If not, Note 2 is uncovered and Player B decides whether or not to take Note 2, etc
- If not, Note $n-1$ is uncovered and Player B decides whether or not to take Note $n-1$
- If not, Player B gets Note $n$
- Player A gets remaining notes
- **Winner** is the player who has the note with the largest number
- This game is usually illustrated as: An office manager is urgently looking for **one** new secretary. There are **n candidates** outside, waiting to be interviewed for this job. The office manager is in such a hurry that she does not actually intend to interview all *n* applicants. Hence, she starts briefly interviwing one candidate after another (in random order) and decides immediatly after each interview for or against that candidate.
- The best strategy is to discard $m \in [0,n[$ notes and then pick the note with greater number than the previous ones, where $m = \arg\max{\sum_{k=m+1}^{n} \frac{1}{n} \frac{m}{k-1}}$, $\frac{1}{n}$ is the probability that the *k-th* note has the largest value, and $\frac{m}{k-1}$ the probability that the first *m* (discarded) notes have greater values than the first *k-1* notes.
- [Adapted proof:] Note that $\sum_{k=m+1}^{n} \frac{1}{n} \frac{m}{k-1} = \frac{m}{n} \sum_{k=m+1}^{n} \frac{1}{k-1} = \frac{m}{n} \sum_{k=m+1}^{n} \frac{n}{k-1} \frac{1}{n} = \frac{m}{n} \sum_{k=m+1}^{n} \frac{1}{(k-1)/n} (\frac{k+1}{n} - \frac{k}{n})$. For $n \to \infty$, and writing $x$ as the limit of $\frac{m}{n}$ then $m \to \arg\max{ x \int_{x}^{1} \frac{1}{t} dt} = \arg\max{(- x \ln(x))}$ (by Riemann approximation). Taking the first derivative, $x = 1/e$ and $m = n/e \approx 0.3679 n$
- Meaning that, for $n \to \infty$, we discard the first $m = n/e$ notes and then choose the first note with greater number. Chance of winning = $1/e$

####  Same game as before but $n = 3$ (advanced version):
- Strategy "always choose the first note" or "last note" then chance of winning = 1/3
- Strategy $m=1$ maximizes chance of winning: "Discard $Z_1$. If $Z_2 > Z_1$ then choose $Z_2$, else choose $Z_3$" then chance of winning = 1/2
  * If $Z_1$ largest, lose (1/3)
  * If $Z_2$ largest, win (1/3)
  * If $Z_3$ largest and $Z_1 > Z_2$, win (1/6)
  * If $Z_3$ largest and $Z_2 > Z_1$, lose (1/6)

#### Same game as before but $n = 2$ (simple version):
- Strategy "always choose the first note" then chance of winning = 50%
- Strategy "choose alternately the first and then the second note" then chance of winning = 50%
- Strategy "If the $Z_1 > X$ then pick Note 1, otherwise choose Note 2" then chance of winning > 50%
  * Case 1: $Z_1 < Z_2 \le X$, pick Note 2 & win
  * Case 2: $Z_2 < Z_1 \le X$, pick Note 2 & lose
  * Case 3: $X < Z_1 < Z_2$, pick Note 1 & lose
  * Case 4: $X < Z_2 < Z_1$, pick Note 1 & win
  * Case 5: $Z_1 \le X < Z_2$, pick Note 2 & win
  * Case 6: $Z_2 \le X < Z_1$, pick Note 1 & win
  * Chance of winning: Case 1 & 2, 50%; Case 3 & 4, 50%; Case 5 & 6, 100%; Overall > 50% (for any $X$)

### 2.5. How Do You Trade Options? Trading Through a Bank
