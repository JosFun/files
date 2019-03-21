import datetime

def month_to_str(month_num):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(month_num, "Invalid month number specified" )

name = ""
abort_seq = "abort"
filename = "guestbook.txt"
while name != abort_seq:
    name = input("Please give your name!\n")
    try:
        with open(filename, "a") as guest_book:
            now = datetime.datetime.now()
            guest_book.write("{} has visited us on the {} of {} {} at {}.\n".format(name, str(now.day) + ".", month_to_str(now.month), str(now.year), str(now.hour) + ":" + str(now.minute)))
        guest_book.close()
    except FileNotFoundError:
        print("The guestbook, stored as " + filename + ", could not be found on your computer.")
