niccr151@ANG-KEMIB6Z56J3 MINGW64 ~/Documents/Python_Scripts/python-course/aspp2022-nac/day3-highperformance (master)
$ python -m memory_profiler matmult.py
Filename: matmult.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22   42.375 MiB   42.375 MiB           1   @profile
    23                                         def matmult(X,Y):
    24   43.812 MiB  -12.551 MiB         251       for i in range(len(X)):
    25                                                 # iterate through columns of Y
    26   43.812 MiB -3168.676 MiB       63000           for j in range(len(Y[0])):
    27                                                     # iterate through rows of Y
    28   43.812 MiB -792129.355 MiB    15750250               for k in range(len(Y)):
    29   43.812 MiB -788975.555 MiB    15687500                   result[i][j] += X[i][k] * Y[k][j]


(base)
niccr151@ANG-KEMIB6Z56J3 MINGW64 ~/Documents/Python_Scripts/python-course/aspp2022-nac/day3-highperformance (master)
$ python -m memory_profiler matmult_numpy.py
Filename: matmult_numpy.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19   52.906 MiB   52.906 MiB           1   @profile
    20                                         def matmult(X,Y):
    21   52.953 MiB    0.047 MiB           1       result = np.matmul(X,Y)
    22   52.953 MiB    0.000 MiB           1       return result
