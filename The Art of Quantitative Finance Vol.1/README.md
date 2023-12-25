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
- Options can be (*for this book*): call & put, american & european, and have long & short positions.
- **Long position** or going long: *buy*, because we have to pay a premium.
- **Short position** or going short: *sell*, because we receive payment of a premium
- **OTM** (out of the money): no significant payoff (payoff = 0) when exercised immediately
- **ATM** (at the money): payoff ≈ 0 (St ≈ K)
- **ITM** (in the money): significant payoff (payoff >> 0) when exercised immediately

The holder of a long/short position in a **European** call/put option on the underlying asset A with expiration date T and strike price K receives/pays a **Payoff** at time T. Since that holder initially purchased/selled the option at the price $C(t_0)/P(t_0)$, the profit (loss) from the option position is **Profit**

| Position\Type | Call | Put |
| :------------ | ---- | --- |
| Long          | Payoff = $\max(S(T)−K, 0)$ <br/> Profit = $\max(S(T) − K, 0) − C(t_0)$ | Payoff = $\max(K-S(T), 0)$ <br/> Profit = $\max(K-S(T), 0) − P(t_0)$ |
| Short         | Payoff = $-\max(S(T)−K, 0)$ <br/> Profit = $-\max(S(T) − K, 0) + C(t_0)$ | Payoff = $-\max(K-S(T), 0)$ <br/> Profit = $-\max(K-S(T), 0) + P(t_0)$ |

![Payoff and profit function](Python/img/01_EuropeanOptions.png "Payoff and profit function")

### 2.3. American Options

- American option: option to exercise at any point (only once) until expiration T

The holder of a long/short position in a **American** call/put option on the underlying asset A with expiration date T and strike price K receives/pays a **Payoff** at any chosen time $t_1 \le T$. Since that holder initially purchased/selled the option at the price $C(t_0)/P(t_0)$, the profit (loss) from the option position is **Profit**

| Position\Type | Call | Put |
| :------------ | ---- | --- |
| Long          | Payoff = $\max(S(t_1)−K, 0)$ <br/> Profit = $\max(S(t_1) − K, 0) − C(t_0)$ | Payoff = $\max(K-S(t_1), 0)$ <br/> Profit = $\max(K-S(t_1), 0) − P(t_0)$ |
| Short         | Payoff = $-\max(S(t_1)−K, 0)$ <br/> Profit = $-\max(S(t_1) − K, 0) + C(t_0)$ | Payoff = $-\max(K-S(t_1), 0)$ <br/> Profit = $-\max(K-S(t_1), 0) + P(t_0)$ |

### 2.4. Any Strategy Is Better than No Strategy and “The Secretary Problem”
