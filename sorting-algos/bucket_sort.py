
# assume the input data is uniformly distributed
def bucket_sort(arr):
    num_buckets = len(arr)
    buckets = []

    for _ in range(num_buckets):
        buckets.append([])
    
    
    
    return buckets
    


nums = [42, 17, 93, 5, 28, 63, 11, 76, 31, 50]
print(bucket_sort(nums))
