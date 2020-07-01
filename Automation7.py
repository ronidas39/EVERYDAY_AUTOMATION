import glob
import os
import io
import time
import concurrent.futures

start=time.perf_counter()
cd=os.getcwd()
dirs=glob.glob(cd+"/*/*/")

def read_file(dir):
    files=glob.glob(dir+"*.csv")
    for file in files:
        with io.open(file,"r",encoding="utf-8")as f1:
            data=f1.read()
            data=data.split("\n")[1:]
            data1="\n".join(row for row in data)
            with io.open("output_multiprocessing.csv","a",encoding="utf-8") as f2:
                f2.write(data1)
                f2.close()
            f1.close()

#===============================================================================
# #use only when multithreading is required            
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     output=executor.map(read_file,dirs)
#===============================================================================

#use only when multi processing is required   
with concurrent.futures.ProcessPoolExecutor() as executor:
    output=executor.map(read_file,dirs)
              
            
#only used when threading or multiprocessing is not required      
#===============================================================================
# for i in range (len(dirs)):
#     read_file(dirs[i])
#===============================================================================
    
end=time.perf_counter()
print(f"time taken {round(end-start,2)} seconds")