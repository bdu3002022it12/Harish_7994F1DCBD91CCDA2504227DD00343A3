def LinearSearchProduct(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices

products = ["shoes","bant","loafer","shoes","sandal","shoes "]
Target = "shoes"
result= LinearSearchProduct(products, Target)
print(result)