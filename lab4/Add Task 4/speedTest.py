import add1,add2,main
import time

time_start_main = time.time()
main.main()
time_elapsed_main = (time.time() - time_start_main)

time_start_add1 = time.time()
add1.main()
time_elapsed_add1 = (time.time() - time_start_add1)

time_start_add2 = time.time()
add2.main()
time_elapsed_add2 = (time.time() - time_start_add2)

print(time_elapsed_main * 100)
print(time_elapsed_add1 * 100)
print(time_elapsed_add2 * 100)
