def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    number = 0
    result = []
    for i in nums1:                     
        greaterelement = -1
        for i2 in range(len(nums2)):    
            if i == nums2[i2]:
                number = nums2[i2]      
                for i3 in range(i2+1,len(nums2)):
                    if nums2[i3] > number:      
                        greaterelement = nums2[i3]
                        break
        result.append(greaterelement)
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))         # Output: [-1,3,-1]