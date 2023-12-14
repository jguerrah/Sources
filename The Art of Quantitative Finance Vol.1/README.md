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

#### Long European call

> The holder of a **long position in a European call option** on the underlying asset A with expiration date T and strike price K receives payment of a **payoff** at time T of **max (S (T) − K, 0)**. Since that holder initially purchased the option at the price C(t), the **profit (loss) from the option position is max (S (T) − K, 0) − C(t)**

![Payoff and profit function of a long call option](/Python/fig.2.1.png "Payoff and profit function of a long call option") {align=center}
