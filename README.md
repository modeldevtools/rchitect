# Minimal R API for Python

[![CircleCI](https://circleci.com/gh/randy3k/rapi/tree/master.svg?style=shield)](https://circleci.com/gh/randy3k/rapi/tree/master)
[![Build status](https://ci.appveyor.com/api/projects/status/4o9m8q61m755xc2a/branch/master?svg=true)](https://ci.appveyor.com/project/randy3k/rapi/branch/master)
[![pypi](https://img.shields.io/pypi/v/rapi.svg)](https://pypi.org/project/rapi/)

```py
import rapi
from rapi import rcopy, reval
rapi.start()
rcopy(reval("R.version"))
```

## Why?

Why another R interface when there is [`rpy2`](https://rpy2.readthedocs.io/)?

1. `rapi` is 100% python

`rapi` is primarily used by [`rtichoke`](https://github.com/randy3k/rtichoke) which is an alternate R console. `rpy2` was not an option because it requires compilations and who wants to compile!?

2. `rapi` is portable

At stated above, `rpy2` requires tool chains to install which makes it not portable. `rapi` on the other hand is lightweight and portable.

3. `rapi` is lightweight

`rpy2` supports a large number of python and R packages, such as numpy, scipy, ggplot2 etc. But there are situations a user may just want to compute a simple thing from R. Additionally, I found that the interface of `rpy2` is not very discoverable.

4. `rapi` is a brother of `RCall.jl`

I am the same developer behind the Julia package [`RCall.jl`](https://github.com/JuliaInterop/RCall.jl) which allows Julia to communicate with R. `rapi` and `RCall.jl` share a very similar design. For example, `rcopy(reval("1"))` works for both `rapi` and `RCall.jl`.
 

## R Eventloop in IPython

When running interactively in IPython, R events such as showing graphical 
devices could be handled by the `r` eventloop. Simply enter in IPython
```
%gui r
```
