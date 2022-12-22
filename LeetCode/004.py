

class Solution:
    def findMedianSortedArrays(self, nums1, nums2)-> float:

        nums1.extend(nums2)
        nums1.sort()
        len2 = len(nums1)
        mid = int(len2 / 2)
        if len2 % 2 == 0:
            return (nums1[mid] + nums1[mid - 1]) / 2
        else:
            return nums1[mid]

        len_n1 = len(nums1)
        len_n2 = len(nums2)
        mid_index = int((len(nums1) + len(nums2)) / 2)
        mid1 = 0
        mid2 = 0
        if mid_index % 2 == 0:
            while mid1 + mid2 != mid_index:
                if nums1[mid1] < nums2[mid2]:
                    mid1 += 1
                    if mid1 + mid2 == mid_index:
                        mid1 -= 1
                        break
                else:
                    mid2 += 1
                    if mid1 + mid2 == mid_index:
                        mid1 -= 1
                        break
            return (nums1[mid1] + nums2[mid2]) / 2
        else:
            while mid1 + mid2 != mid_index:
                if nums1[mid1] < nums2[mid2]:
                    mid1 += 1
                    if mid1 + mid2 == mid_index:
                        mid1 -=1
                        break
                else:
                    mid2 += 1
                    if mid1 + mid2 == mid_index:
                        mid1 -=1
                        break
            return nums1[mid1] if mid1 > mid2 else nums2[mid2]


if __name__ == '__main__':
    st = Solution()
    # lst = [1, 3]
    # lst2 = [2]
    # lst = [1, 2]
    # lst2 = [3, 4]

    lst = [1, 3,5]
    lst2 = [2,4]
    print(st.findMedianSortedArrays(lst, lst2))

    print(5/2)
