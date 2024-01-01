# Ez_linear

## Description

奇怪，怎么才240个方程组要解336个变量。

来看看你的线代吧。

hint1:注意利用flag头尾已知部分增加方程组

hint2:flag均为ASCII码,改如何利用

## Soluton

按照hint思路就很明显了

利用flag头尾6bytes可以得到6*8=48bits，即48个方程组

利用ASCII对余下的36bytes的flag，每个ASCII的第一位bit为0,可以得到36组方程

一共有240+48+36=322组，线代知识可以知道有336-322=14组解空间

即有2^14^这么多解，进行一个简单的ASCII码判断即可得到flag

