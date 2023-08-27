def read_file(filePath):
	with open(filePath) as file:
		str_nums = file.read().split('\n')
		return [int(n) for n in str_nums]

nums1 = read_file('file1.txt')
nums2 = read_file('file2.txt')

overlap = [n1 for n1 in nums1 if n1 in nums2]
print(overlap)