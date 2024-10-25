# Homework Sheet 1, Gülle, Janik

## Exercise 2:
a)

Center of mass energy

$$ \sqrt{s} = m_{Higgs} = 125~GeV = 2E_e \iff E_e = 62.5~GeV$$

The electron and positron each need to have an energy of $~62.5~GeV$

b) The FIFA Goal has a size of $7.32~m$ by $2.44~m$ and thus an area of $7.32~m*2.44~m=17.86~m²$.
For the conversion from $m²$ to natural units we use $$\frac{\hbar c}{1eV}\approx197\cdot10^{-15}~fm=1.97\cdot10^{-7}m$$ with $\hbar c\approx197~MeV~fm$.

This means the area of the FIFA Goal is

$$A = \frac{17.86~m²}{(\hbar c)²}= \frac{17.86~m²}{(197~MeV~fm)²} = 4.6\cdot10^{14}~\frac{1}{eV²}$$

c) 

$$G = 6.7~\cdot~10^{-11}~m³~kg^{-1}~s^{-2}$$ 

The dimension of G is
$$[G]=L³M^{-1}T^{-2}$$

using the natural units relation
$$[L]=[T]=[M]^{-1}$$
we get
$$[G] = [M]^{-2}$$

now we convert from SI units to natural units:

$$\frac{\hbar ^3 c^3}{eV^3} \cdot \frac{c^2}{eV} \cdot \frac{eV^2}{\hbar ^2} \approx 9.96 \cdot 10^{45}~\frac{m^3}{kg s^2}.$$

With this we can calculate G in natural units:
$$ G=6.7~\cdot 10^{-11}~\frac{m^3}{kg s^2}\\
\approx 6.7\cdot 10^{-57}~\frac{1}{eV^2}$$

d)

Given a particle with electric charge $q$ and the momentum $\vec{p}$ and given a magnetic flux density $\vec{B}$ we want to introduce the konstant k so that the unit of the radius of the particles trajectory is has the dimension of $[m]$.

$$R=\frac{|\vec{p}|}{q |\vec{B}|}\cdot k$$

since $|\vec{p}|$ is in narural units we can use the relation

$$1~\frac{GeV}{c}=10^9~\frac{e kg}{c s}$$

we find that

$$k=\frac{c}{e}=1.87\cdot10^{27}~\frac{m}{c s}$$

## Exercise 3:

a) The constants have the following units:

$$G = [m]³[kg]^{-1}[s]^{-2},~\hbar=[kg][m]²[s]^{-1}, ~c=[m][s]^{-1},~t_p=[s]$$
with the equation $$t_p=G^\alpha \hbar^\beta c^\gamma$$ we get the equation

$$[s] = [m]^{3\alpha+2\beta+\gamma}[kg]^{\beta-\alpha}[s]^{\beta-2\alpha-\gamma}$$
from that we get the system of equations:

$$
3\alpha+2\beta+\gamma = 0 \\
\beta-\alpha = 0 \\
\beta -2 \alpha - \gamma = 1
$$

solving gives us the values
$$\alpha = \beta = \frac{1}{4},~\gamma = -\frac{5}{4}$$

b) similarly we write
$$m_p = G^\alpha \hbar^\beta c^\gamma$$

and get the system of equations
$$
3\alpha+2\beta+\gamma = 0 \\
\beta-\alpha = 1 \\
\beta -2 \alpha - \gamma = 0
$$

solving gives us

$$\alpha = -\frac{3}{4},~\beta=\frac{1}{4},~\gamma=\frac{7}{4}$$

## Exercise 4:

Defining the matrices $A$ and $B$ as follows:
``` Python
⎡1  2⎤
⎢    ⎥
⎣3  3⎦


⎡20  20⎤
⎢      ⎥
⎣10  10⎦

```

Then we can calculate the product of the matrices $A$ and $B$:

``` Python

⎡1  2⎤ ⎡20  20⎤
⎢    ⎥⋅⎢      ⎥
⎣3  3⎦ ⎣10  10⎦
=
⎡40  40⎤
⎢      ⎥
⎣90  90⎦
```

Printing element $A_{01}$ we get:
``` Python
2
```

Using `matrix_a.T` we can transpose the matrix $A$.

``` Python
      T
⎡1  2⎤ 
⎢    ⎥ 
⎣3  3⎦ 
=
⎡1  3⎤
⎢    ⎥
⎣2  3⎦
```

Finally we can calculate the inverse of the matrix $A$ using `matrix_a.inv()`.

``` Python
      -1
⎡1  2⎤  
⎢    ⎥  
⎣3  3⎦  
=
⎡-1  2/3 ⎤
⎢        ⎥
⎣1   -1/3⎦
```
proof:
``` Python
⎡-1  2/3 ⎤ ⎡1  2⎤
⎢        ⎥⋅⎢    ⎥
⎣1   -1/3⎦ ⎣3  3⎦
=
⎡1  0⎤
⎢    ⎥
⎣0  1⎦

```

## Exercise 5:

Using the `sympy.trace()` function we can calculate the trace of a matrix.

``` Python
trace_sigma_1= 0
trace_sigma_2= 0
trace_sigma_3= 0
```

Similarly we can calculate the determinant of a matrix using the `sympy.det()` function.

``` Python
det_sigma_1= -1
det_sigma_2= -1
det_sigma_3= -1
```

Finally using anticommutator of two matrices, `{A,B}=AB-BA`, we can verify the anticommutator relations.

``` Python
{sigma_1, sidma_1}=
⎡2  0⎤
⎢    ⎥
⎣0  2⎦
{sigma_1, sidma_2}=
⎡0  0⎤
⎢    ⎥
⎣0  0⎦
{sigma_1, sidma_3}=
⎡0  0⎤
⎢    ⎥
⎣0  0⎦
{sigma_2, sidma_2}=
⎡2  0⎤
⎢    ⎥
⎣0  2⎦
{sigma_2, sidma_3}=
⎡0  0⎤
⎢    ⎥
⎣0  0⎦
{sigma_3, sidma_3}=
⎡2  0⎤
⎢    ⎥
⎣0  2⎦
```