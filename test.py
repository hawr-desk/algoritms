import algrtm as alg

arr = [4, 2, 8, 1, 5, 7, 6,9]
print(arr)
sort = alg.Sorting()
arr1 = sort.gnome(arr)
print(arr1)

search = alg.Search()
srch = search.linear(arr1, 4)
print('index = ', srch)