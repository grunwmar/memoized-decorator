import time
from memoizer import memoized

def measure_computation_time(func, *args, **kwargs):
    start = time.perf_counter_ns()

    result = func(*args, **kwargs)

    finish = time.perf_counter_ns()

    duration = finish - start
    args_str = ", ".join([f"{v!r}" for v in args])
    kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
    print(f"""===== Measured computation time =====
    function:     {func.__name__}({args_str}, {kwargs_str})
    return value: {result!r}

    duration:     {duration} ns

    """)
    return duration



print("Without @memoized decorator")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

r1 = measure_computation_time(fib, 30)


print("With @memoized decorator")

@memoized
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

r2 = measure_computation_time(fib, 30)

print(f"Using @memoized was {r1/r2:.0f}x faster")

"""
Without @memoized decorator
===== Measured computation time =====
    function:     fib(30, )
    return value: 1346269

    duration:     350833033 ns


With @memoized decorator
===== Measured computation time =====
    function:     fib(30, )
    return value: 1346269

    duration:     87368 ns


Using @memoized was 4016x faster

"""
