class Star_Cinema:
    __hall_list = []

    def get_hall_list(self):
        return self.__hall_list

    def entry_hall(self,hall):
        self.__hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}

        Star_Cinema().entry_hall(self) # entry all the halls to the Star_Cinema class 

    def entry_show(self,id,movie_name,time):
        self.__show_list.append([id,movie_name,time]) # store show id, movie name and time as a tuple in a list
        self.__seats[id] = [] # Create an empty list for the current show's seats
        for i in range(self.__rows):
            row = [] # Create an empty list for the current row
            for j in range(self.__cols):
                row.append(None) # Add a None value for each seat in the current row
            self.__seats[id].append(row)  # Add the row to the list of seats for the current show


    def view_show_list(self):
        for show_info in self.__show_list:
            print(f"MOVIE NAME: {show_info[1]}, SHOW ID: {show_info[0]}, Time: {show_info[2]}")

    def view_available_seats(self):
        for id in self.__seats:
            for row in range(self.__rows):
                print('[ ',end="")
                for col in range(self.__cols):
                    if self.__seats[id][row][col] == None:
                        print("0",end=" ")
                    else:
                        print("1",end=" ")
                print(']')

    def book_seats(self,id,row,col):
        if row > self.__rows or col > self.__cols or row < 1 or col < 1:
            print("Invalid seat.")
            return
        if self.__seats[id][row-1][col-1] == None:
            self.__seats[id][row-1][col-1] = '1'
            print(f"Seat ({row},{col}) Booked for show {id}")
        else:
            print("Seat already booked.")

hall1 = Hall(5, 5, 101)
hall2 = Hall(5, 5, 102)
hall1.entry_show(502,'Avengers','07/10/23  12:00 pm')
hall2.entry_show(503,'Justice League','07/10/23  04:00 pm')

while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')

    option = int(input('ENTER OPTION: '))

    if option == 1:
        print('----------------------------------------- ')
        for hall in Star_Cinema().get_hall_list():
            hall.view_show_list()
        print('----------------------------------------- ')

    elif option == 2:
        id = int(input('Enter show ID: '))
        hall = None
        for h in Star_Cinema().get_hall_list():
            for show in h._Hall__show_list:
                if show[0] == id:
                    hall = h
                    break
        if hall == None:
            print("Invalid show ID.")
        else:
            print('Available Seats for the show: ')
            hall.view_available_seats()

    elif option == 3:
        id = int(input('Enter show ID: '))
        ticket = int(input('Number of Tickets?: '))
        row = int(input('Enter seat row: '))
        col = int(input('Enter seat col: '))
        hall = None
        for h in Star_Cinema().get_hall_list():
            for show in h._Hall__show_list:
                if show[0] == id:
                    hall = h
                    break
        if hall == None:
            print("Invalid show ID.")
        else:
            hall.book_seats(id,row,col)

    elif option == 4:
        break
    else:
        print('INVALID OPTION')
