# Inference Truth Values

## Measurements of uncertainty

### f/c to w+/w

w+=k*f*c / (1-c)
w =k*c / (1-c)

### w+/w to f/c

f=w+/w
c=w/(w+k)

## Revision

f = (f1 * c1 * (1 - c2) + f2 * c2 * (1 - c1)) / (c1 * (1 - c2) + c2 * (1 - c1))
c = (c1 * (1 - c2) + c2 * (1 - c1)) / (c1 * (1 - c2) + c2 * (1 - c1) + (1 - c1) * (1 - c2))

## Deduction

f = and(f1, f2) = f1f2
c = and(f1, f2, c1, c2) = f1f2c1c2

## Induction

f = f1
c = f2c1c2/(f2c1c2 + k)

## Abduction

f = f2
c = f1c1c2/(f1c1c2 + k)