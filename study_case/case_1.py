def check_memory():
    """
    This function is used to check the memory usage of the hello world program.
    """
    import subprocess
    import os
    import sys
    import time
    import psutil
    import signal
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator

    # Get the current process id
    pid = os.getpid()

    # Get the current process
    p = psutil.Process(pid)

    # Get the current process memory usage
    memory_usage_start = p.memory_info().rss 

    # Run the hello world program
    subprocess.run(["python3", "../main.py"])

    # Get the current process memory usage
    memory_usage_end = p.memory_info().rss

    # Calculate the memory usage difference
    memory_usage_diff = memory_usage_end - memory_usage_start

    # Print the memory usage difference
    print("Memory usage difference: {} kb".format(memory_usage_diff/ (1024 ** 2)))


check_memory_usage()