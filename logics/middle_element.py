def middle_element(lst):
  length = len(lst)
  modifier = int(length/2)
  if length%2 != 0:
    return lst[(modifier)]
  else:
    lower_mid = lst[(modifier)-1]
    upper_mid = lst[modifier]
    return (lower_mid+upper_mid)/2