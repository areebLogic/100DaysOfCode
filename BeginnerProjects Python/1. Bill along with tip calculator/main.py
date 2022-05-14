#This is going to be a script to to calculate bill along with tip.
#This is focused towards scenarios where bills are being split between two or more people


totalBill = float(input("How much is the total bill? "))
billSplits = float(input("How many people are going to split the bill among each other? "))
preferredTip= float(input("How much tip is each person going to give? "))

billForEach = (totalBill/billSplits) + preferredTip

print(f"Each person is going to pay {billForEach} \nThis will account for their tip along with their bill after split.")
