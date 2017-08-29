# Introduction to List Data Structure in Python
# A list is a collection of Data Items where each item
# holds a relative position with respect to the others

item_string = "Cars Bikes Fruits Vegetables Drinks"
print "\n[item_string] is:",item_string
print "[item_string] is a data structure of --", type(item_string)
print "Wait,' There are more items to be added to the Cart"


shop_list = item_string.split(' ')
print "\nConverting [item_string]  to a new data structure [shop_list] :of TYPE ", type(shop_list)

print "[SHOP_LIST_CART] : ", shop_list

add_new_items = ["Day", "Night", "Music", "Frisbee", "Games", "Sports"]
print "\n[add_new_items] is a data structure of --", type(add_new_items)

print "ADD NEW ITEMS : ", add_new_items

print "\n\n***List Operation BEGIN ***"

while len(shop_list) != 10:
    next_one = add_new_items.pop()
    print "Adding new item to the Cart:", next_one
    shop_list.append(next_one)
    print "There are %d items now:" % len(shop_list)

print "***List Operations END ***\n\n"


print "Printing SHOP_LIST",shop_list
si_index = shop_list.index("Music")
print "Music is found at Location",si_index

if "Music" in shop_list:
    print "ITEM FOUND in the LIST"
else:
    print "MUSIC is not found in the Present List"

new_shop_list = shop_list
print "There we go:", new_shop_list

print "Let's do some more things with the new_shop_list.\n\n"

print new_shop_list[1]
print new_shop_list[-1] # whoa ! Fancy

print "Whoa, Fancy\n"
print "Pop from the list", new_shop_list.pop()

print "\n[new_shop_list] Data Structure is--", type(new_shop_list)

print "Joining now"
print ' '.join(new_shop_list)

print "\nThe new [new_shop_list] Data Structure after join opeartion is--", type(new_shop_list)
print '#'.join(new_shop_list[3:5])

