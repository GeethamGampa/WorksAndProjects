# #==================================== MULTIPROCESSING ====================================#

# #=========================== Square of a number ===========================#

from multiprocessing import Process

def print_square(n):
    square = n * n
    print(f"The square of {n} is {square}")

if __name__ == "__main__":
    p = Process(target=print_square, args=(9,))
    p.start()
    p.join()


# #===========================  Square of 100 numbers ===========================#

# This part finds squares of numbers from 1 to 100.
# We use a loop to start() and join() them

def print_square(n):
    print(f"The square of {n} is {n * n}")

if __name__ == "__main__":
    process = []

    for i in range(1, 101):
        p = Process(target=print_square, args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

# #=========================== Using Pool ===========================#

# This part also finds squares from 1 to 100, but in a simpler and cleaner way.
# We use Pool.map() to send all numbers to the function.
# It gives back results in order

from multiprocessing import Pool

def print_square(n):
    return f"The square of {n} is {n * n}"

if __name__ == "__main__":
    with Pool() as p:
        r = p.map(print_square, range(1, 101))
        
    for result in r:
         print (result)
        

#==================================================================================================#
#==================================================================================================#


#===========================  Cube of a number =========================== #


def print_cube(n):
    cube = n * n * n
    print(f"The cube of {n} is {cube}")

if __name__ == "__main__":
    p = Process(target=print_cube, args=(2,))
    p.start()
    p.join()

#===========================  Cube of 100 numbers =========================== #

# This part finds cubes from 1 to 100 using 100 small processes.
# We create, start, and join each process in a loop.

def print_cube(n):
    print(f"The square of {n} is {n * n * n}")

if __name__ == "__main__":
    process = []

    for i in range(1, 101):
        p = Process(target=print_cube, args=(i,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

# #=========================== USING POOL =========================== #

# This part uses Pool.map() to find cubes of 1 to 100 in a simple way.
# It returns the results in the right order, and we print each cube.

def print_cube(n):
    return f"The cube of {n} is {n * n * n}"

if __name__ == "__main__":
    with Pool() as p:
        r = p.map(print_cube, range(1, 101))
        
    for result in r:
        print (result)

# # ============================================ Memory Profiler ============================================ #

# The memory_profiler is a tool in Python that helps you measure
# how much memory your program is using, especially line by line.

from memory_profiler import profile

# #===========================  Square of 100 numbers =========================== #

@profile
def print_square():
    for n in range(1, 101):
        square = n * n
        print(f"The square of {n} is {square}")

if __name__ == "__main__":
    print_square()
    
# #===========================  CUbe of 100 numbers =========================== #

@profile
def print_cube():
    for n in range(1, 101):
        cube = n * n * n
        print(f"The cube of {n} is {cube}")
        
if __name__ == "__main__":
    print_cube()



