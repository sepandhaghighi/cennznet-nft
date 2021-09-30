<div align="center">
<h1>CENNZnet NFT</h1>
</div>

----------

## Overview
<a href="https://gitcoin.co/issue/cennznet/grants/9/100026471">CENNZnet Generative Art Bounty</a>

<p align="justify">	
In this work I tried to generate unique complex geometric shapes based on random points, different formulas, different colors and also different projections!!
The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.
</p>

## Arts

### 1

- x : `random.uniform(-1,1) * x**2  - random.uniform(-1,1) * math.sin(y**2)`
- y : `random.uniform(-1,1) * y**3 - random.uniform(-1,1) * math.cos(x**2)`
- seed : 16081
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/1.png">	

### 2

- x : `random.uniform(-1,1) * x**2  - 2*x*math.sin(y**2)`
- y : `random.uniform(-1,1) * y**3 - math.cos(x**2)`
- seed : 19644
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/2.png">	

### 3

- x : `random.uniform(-1,1) * x**2  - math.sin(y**3) + abs(y-2*x)`
- y : `random.uniform(-1,1) * y**3 - math.cos(x**2)`
- seed : 43111
- projection : Rectilinear

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/3.png">	

### 4

- x : `random.uniform(-1,1) * x**2  - math.sin(y**3) + abs(y-2*x)`
- y : `random.uniform(-1,1) * y**3 + math.sin(x-y**2)`
- seed : 48614
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/4.png">	

### 5

- x : `random.uniform(-1,1) * y**3 + math.cos(2*y)`
- y : `random.uniform(-1,1) * math.cos(abs(y-x))**2`
- seed : 19974
- projection : Rectilinear

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/5.png">	

### 6

- x : `random.uniform(-1,1) * math.log10(abs(x))`
- y : `random.uniform(-1,1) * y**3 + math.sin(x**2)`
- seed : 823
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/6.png">


### 7

- x : `random.uniform(-1,1) * math.sin(y**2) + math.cos(x**2) + math.sin(2*x + y)`
- y : `random.uniform(-1,1) * y**3 + math.sin(x**2)`
- seed : 1125
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/7.png">	

### 8

- x : `random.uniform(-1,1) * math.sin(y**2) + math.cos(x**2) + math.sin(2*x + y)`
- y : `random.uniform(-1,1) * math.sin(x**3) + math.cos(2*y - x)`
- seed : 973
- projection : Hamer

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/8.png">

### 9

- x : `random.uniform(-1,1) * math.sqrt((x + y)**2) + math.floor(x - y)`
- y : `random.uniform(-1,1) * math.sqrt(abs(x-y)) ** 3  + math.ceil(x + y)`
- seed : 1083
- projection : Rectilinear

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/9.png">	

### 10

- x : `random.uniform(-1,1) * math.sqrt((x + y)**2) + math.floor(x - y)`
- y : `random.uniform(-1,1) * math.sqrt(abs(x-y)) ** 3  + math.ceil(x + y)`
- seed : 324
- projection : Polar

<img src="https://github.com/sepandhaghighi/cennznet-nft/raw/master/images/10.png">			


