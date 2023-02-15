def dupes(nums):
    hset = set()
    for item in nums:
        if item in hset:
            return True
        else:
            hset.add(item)
    return False
