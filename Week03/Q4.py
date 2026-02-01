monday_class={
    "Alice","Bob","harlie","Diana"
}
wednesday_class={"Bob","Diana","Eve","Frank"}
monday_class.add("Grace")
print("Monday Class", monday_class)
print("Wednesday Class", wednesday_class)

both_classes= monday_class & wednesday_class
print("Students in both classes", both_classes)

all_Students= monday_class | wednesday_class
print("Attended at least one class", all_Students)
only_monday= monday_class - wednesday_class
print("Attened only Monday  class", only_monday)

only_one=monday_class ^ wednesday_class
print("Attended only one class", only_one)
print("Is Monday subset of all students? ", monday_class<= all_Students)