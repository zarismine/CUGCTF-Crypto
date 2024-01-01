# BabyRSA

## Description

p,q高位一样的简单RSA

## Solution

$$
p = k+a\\q=k+b\\a,b:200bits\\p,q:512bits
$$

所以对n简单的开方即可得到p，q高位

进一步套用p高位攻击脚本就ok