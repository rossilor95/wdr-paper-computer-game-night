# Challenges

## 1. Countdown
- Start with a number N in register $R_0 = N$ (i.e., $N$ tokens in $R_0$).
- Write a program to "empty" $R_0$ of all tokens (erase its value and bring it to zero)
- Remember that you cannot subtract $1$ from an empty register and that the program must end with Stop... So it must also work if $N = 0$.


## 2. Addition
- Start with a number $N$ in register $R_0$ and a number $M$ in register $R_1$.
- Add $M$ to $N$ so that the program ends with $R_0 = M + N$ and $R_1 = 0$.


## 3. Subtraction
- Start with a number $N$ in register $R_0$ and a number $M$ in register $R_1$.
- Subtract $M$ from $N$ so that the program ends with $R_0 = N - M$ and $R_1 = 0$.
*WARNING*: negative numbers are not allowed, so the program must stop with $R_0$ if $M > N$.

## 4. Even or Odd
- Start with a number $N$ in register $R_0$.
- Decrement $R_0$ until it reaches $0$.
- Use $R_1$ as an indicator (flag): set it to $1$ when the current value of $R_0$ is NOT a multiple of $2$, set it to $0$ when the current value of $R_0$ is a multiple of $2$.
- Consider starting with $R_1 = 0$. At the end of the program, we must have $R_1 = 0$ if $N$ is even, $R_1 = 1$ if $N$ is odd.