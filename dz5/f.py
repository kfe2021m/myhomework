# def binary_search(sequence, start_element, key):
#     end_element = len(sequence) - 1
#     while start_element <= end_element:
#         middle_element = start_element + (end_element - start_element) // 2
#         if sequence[middle_element] == key:
#             return middle_element
#         elif sequence[middle_element] < key:
#             start_element = middle_element + 1
#         else:
#             end_element = middle_element - 1
#     return None
# sequence = [int(x)for x in input().split()]
# find_element = int(input())
# result = binary_search(sequence=sequence, start_element=0, key=find_element)
# print(result)