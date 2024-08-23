import statistics

def mean_median_mode(arr):
    length = len(arr)
    sum = 0
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    mode = statistics.mode(arr)
    return (mean,median,mode)
    # return [mean,median,mode]
    # return mean,median,mode

print(mean_median_mode([1,2,3,4,5,6]))
print(mean_median_mode([1,2,3,4,5,5]))


def add(a,b):
    if( a==0 and b==0 ):
        return "please enter a valid values"
    else:
        return a + b

print(add(0,0))
print(add(1,1))