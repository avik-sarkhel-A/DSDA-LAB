import time
string1 = "Hello" * 100000  
string2 = "Hello" * 100000 
start_time = time.time()
result = (string1 == string2)
end_time = time.time()
print(f"Strings are equal: {result}. Time taken: {end_time - start_time:.10f} seconds.")
