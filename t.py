import sys
import time

print("PYTHON VERSION", sys.version)

import psutil

process = psutil.Process()

import tensorflow as tf

print("TF VERSION", tf.__version__)


def bench(fn):
    t = time.monotonic()
    r = []
    for i in range(100):
        for j in range(5000):
            fn()

        mem = process.memory_info().rss / 1024**2
        r.append(mem)
    return r[-1] - r[0], time.monotonic() - t


def fn():
    return tf.zeros(shape=(1,))


tf_fn = tf.function(fn)

if __name__ == "__main__":
    fn()  # warmup
    tf_fn()

    mem_usage, elapsed = bench(fn)
    print(f"EAGER memory growth {mem_usage:.1f} MB in {elapsed:.1f} s")

    mem_usage, elapsed = bench(tf_fn)
    print(f"TF FUNC memory growth {mem_usage:.1f} MB in {elapsed:.1f} s")
