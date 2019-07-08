userName = input("Enter USER NAME : ")
delCount = int(input("Enter the number of characters to be deleted : "))
print("ORIGINAL USER NAME : " + userName)
# to delete first few characters
userName = userName[delCount:]
print("USER NAME AFTER DELETING CHARACTERS : " + userName)
# to reverse the string
userName = userName[::-1]
print("USER NAME AFTER REVERSING : " + userName)
