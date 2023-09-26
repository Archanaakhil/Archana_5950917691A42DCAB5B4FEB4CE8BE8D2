def linearSearchproduct(productList, targetproduct):
 indices = [ ]

 for index, product in enumerate(productList):
   if product == targetproduct: 
     indices.append (index)

 return indices

#Example Usage:
Products = ["Shoes", "boot", "Looper", "Shoes", "Sandal","Shoes"]
target = "Shoes"
result = linearSearchproduct(Products, target) 
print(result)