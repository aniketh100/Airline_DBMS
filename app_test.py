import streamlit as st
import pandas as pd
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='YOUR USER',
    password= 'YOUR PASSWORD',
    database='AIRLINE_MANAGEMENT'
)

# Function to execute SQL queries
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Streamlit app
def main():
    if conn:
        print("connected")
    st.title("Database Management System Project")

    # Sidebar menu for CRUD operations
    crud_operation = st.selectbox("Select CRUD Operation", ["", "Create", "Read", "Update", "Delete"])

    

    if crud_operation == "Create":
        create_operation()
    elif crud_operation == "Read":
        read_operation()
    elif crud_operation == "Update":
        update_operation()
    elif crud_operation == "Delete":
        delete_operation()

# Function to perform CREATE operation for each table
def create_operation():
    table_name = st.selectbox("Select Table", ["Aircraft", "Airports", "Booking", "Crew", "Flight", "Gate", "Luggage", "Passenger", "Schedule", "Ticket"])
    st.subheader(f"Create Operation - {table_name}")

    if table_name == "Aircraft":
        print("Creating")
        with st.form("create_aircraft_form"):
            print("creating 2")
            aircraft_id = st.text_input("Aircraft ID")
            manufacturer = st.text_input("Manufacturer")
            model = st.text_input("Model")
            no_of_seats = st.text_input("Number of Seats")
            sub = st.form_submit_button("Add Aircraft")
            if sub:
                print("Creating in if")
                query = f"INSERT INTO Aircraft VALUES ('{aircraft_id}', '{manufacturer}', '{model}', {no_of_seats})"
                execute_query(query)
                st.success("Aircraft added successfully!")

    elif table_name == "Airports":
        with st.form("create_airport_form"):
            airport_code = st.text_input("Airport Code")
            city = st.text_input("City")
            country = st.text_input("Country")
            no_of_terminals = st.text_input("Number of Terminals")
            if st.form_submit_button("Add Airport"):
                query = f"INSERT INTO Airports VALUES ('{airport_code}', '{city}', '{country}', {no_of_terminals})"
                execute_query(query)
                st.success("Airport added successfully!")

    elif table_name == "Booking":
        with st.form("create_booking_form"):
            booking_id = st.text_input("Booking ID")
            passenger_id = st.text_input("Passenger ID")
            flight_id = st.text_input("Flight ID")
            date_of_booking = st.text_input("Date of Booking")
            if st.form_submit_button("Add Booking"):
                query = f"INSERT INTO Booking VALUES ('{booking_id}', '{passenger_id}', '{flight_id}', '{date_of_booking}')"
                execute_query(query)
                st.success("Booking added successfully!")

    elif table_name == "Crew":
        with st.form("create_crew_form"):
            crew_id = st.text_input("Crew ID")
            name = st.text_input("Name")
            position = st.text_input("Position")
            experience = st.text_input("Experience")
            airport_code = st.text_input("Airport Code")
            if st.form_submit_button("Add Crew"):
                query = f"INSERT INTO Crew VALUES ('{crew_id}', '{name}', '{position}', '{experience}', '{airport_code}')"
                execute_query(query)
                st.success("Crew added successfully!")

    elif table_name == "Flight":
        with st.form("create_flight_form"):
            flight_id = st.text_input("Flight ID")
            aircraft_id = st.text_input("Aircraft ID")
            aircraft_company = st.text_input("Aircraft Company")
            origin = st.text_input("Origin")
            arrival_time = st.text_input("Arrival Time")
            departure_time = st.text_input("Departure Time")
            destination = st.text_input("Destination")
            if st.form_submit_button("Add Flight"):
                query = f"INSERT INTO Flight VALUES ('{flight_id}', '{aircraft_id}', '{aircraft_company}', '{origin}', '{arrival_time}', '{departure_time}', '{destination}')"
                execute_query(query)
                st.success("Flight added successfully!")

    elif table_name == "Gate":
        with st.form("create_gate_form"):
            gate_id = st.text_input("Gate ID")
            airport_code = st.text_input("Airport Code")
            if st.form_submit_button("Add Gate"):
                query = f"INSERT INTO Gate VALUES ('{gate_id}', '{airport_code}')"
                execute_query(query)
                st.success("Gate added successfully!")

    elif table_name == "Luggage":
        with st.form("create_luggage_form"):
            luggage_id = st.text_input("Luggage ID")
            passenger_id = st.text_input("Passenger ID")
            weight = st.text_input("Weight")
            length = st.text_input("Length")
            width = st.text_input("Width")
            height = st.text_input("Height")
            status = st.text_input("Status")
            no_of_bags = st.text_input("Number of Bags")
            if st.form_submit_button("Add Luggage"):
                query = f"INSERT INTO Luggage VALUES ('{luggage_id}', '{passenger_id}', {weight}, {length}, {width}, {height}, '{status}', {no_of_bags})"
                execute_query(query)
                st.success("Luggage added successfully!")

    elif table_name == "Passenger":
        with st.form("create_passenger_form"):
            passenger_id = st.text_input("Passenger ID")
            name = st.text_input("Name")
            date_of_birth = st.text_input("Date of Birth")
            passport_no = st.text_input("Passport No")
            phone_no = st.text_input("Phone No")
            email_id = st.text_input("Email ID")
            if st.form_submit_button("Add Passenger"):
                query = f"INSERT INTO Passenger VALUES ('{passenger_id}', '{name}', '{date_of_birth}', '{passport_no}', {phone_no}, '{email_id}')"
                execute_query(query)
                st.success("Passenger added successfully!")

    elif table_name == "Schedule":
        with st.form("create_schedule_form"):
            schedule_id = st.text_input("Schedule ID")
            flight_id = st.text_input("Flight ID")
            gate_id = st.text_input("Gate ID")
            arrival_time = st.text_input("Arrival Time")
            departure_time = st.text_input("Departure Time")
            if st.form_submit_button("Add Schedule"):
                query = f"INSERT INTO Schedule VALUES ('{schedule_id}', '{flight_id}', '{gate_id}', '{arrival_time}', '{departure_time}')"
                execute_query(query)
                st.success("Schedule added successfully!")

    elif table_name == "Ticket":
        with st.form("create_ticket_form"):
            ticket_id = st.text_input("Ticket ID")
            flight_id = st.text_input("Flight ID")
            passenger_id = st.text_input("Passenger ID")
            seat_no = st.text_input("Seat No")
            price = st.text_input("Price")
            if st.form_submit_button("Add Ticket"):
                query = f"INSERT INTO Ticket VALUES ('{ticket_id}', '{flight_id}', '{passenger_id}', '{seat_no}', {price})"
                execute_query(query)
                st.success("Ticket added successfully!")

# Function to perform READ operation for each table
'''def read_operation():
    table_name = st.selectbox("Select Table", ["Aircraft", "Airports", "Booking", "Crew", "Flight", "Gate", "Luggage", "Passenger", "Schedule", "Ticket"])
    st.subheader(f"Read Operation - {table_name}")

    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    st.dataframe(df)'''
    
def read_operation():
    st.subheader("Read Operation")
    table_name = st.selectbox("Select Table to Read", ["Aircraft", "Airports", "Booking", "Crew", "Flight", "Gate", "Luggage", "Passenger", "Schedule", "Ticket"])

    query = f"SELECT * FROM {table_name}"
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    if data:
        st.write(f"Showing data from {table_name} table:")
        st.table(data)
    else:
        st.warning("No data found for the selected table.")
    
def update_operation():
    table_name = st.selectbox("Select Table", ["Aircraft", "Airports", "Booking", "Crew", "Flight", "Gate", "Luggage", "Passenger", "Schedule", "Ticket"])

    st.subheader(f"Update Operation - {table_name}")

    if table_name == "Aircraft":
        with st.form("update_aircraft_form"):
            aircraft_id = st.text_input("Aircraft ID to Update")
            manufacturer = st.text_input("New Manufacturer")
            model = st.text_input("New Model")
            no_of_seats = st.text_input("New Number of Seats")
            if st.form_submit_button("Update Aircraft"):
                query = f"UPDATE Aircraft SET MANUFACTURER = '{manufacturer}', MODEL = '{model}', NO_OF_SEATS = {no_of_seats} WHERE AIRCRAFT_ID = '{aircraft_id}'"
                execute_query(query)
                st.success("Aircraft updated successfully!")

    elif table_name == "Airports":
        with st.form("update_airport_form"):
            airport_code = st.text_input("Airport Code to Update")
            city = st.text_input("New City")
            country = st.text_input("New Country")
            no_of_terminals = st.text_input("New Number of Terminals")
            if st.form_submit_button("Update Airport"):
                query = f"UPDATE Airports SET CITY = '{city}', COUNTRY = '{country}', NO_OF_TERMINALS = {no_of_terminals} WHERE AIRPORT_CODE = '{airport_code}'"
                execute_query(query)
                st.success("Airport updated successfully!")

    elif table_name == "Booking":
        with st.form("up_book_form"):
            booking_id = st.text_input("Booking ID to Update")
            passenger_id = st.text_input("New Passenger ID")
            flight_id = st.text_input("New Flight ID")
            date_of_booking = st.text_input("New Date of Booking")
            if st.form_submit_button("Update Booking"):
                query = f"UPDATE Booking SET PASSENGER_ID = '{passenger_id}', FLIGHT_ID = '{flight_id}', DATE_OF_BOOKING = '{date_of_booking}' WHERE BOOKING_ID = '{booking_id}'"
                execute_query(query)
                st.success("Booking updated successfully!")

    elif table_name == "Crew":
        with st.form("up_crew_form"):
            crew_id = st.text_input("Crew ID to Update")
            name = st.text_input("New Name")
            position = st.text_input("New Position")
            experience = st.text_input("New Experience")
            airport_code = st.text_input("New Airport Code")
            if st.form_submit_button("Update Crew"):
                query = f"UPDATE Crew SET NAME = '{name}', POSITION = '{position}', EXPERIENCE = '{experience}', AIRPORT_CODE = '{airport_code}' WHERE CREW_ID = '{crew_id}'"
                execute_query(query)
                st.success("Crew updated successfully!")

    elif table_name == "Flight":
        with st.form("up_fl_form"):
            flight_id = st.text_input("Flight ID to Update")
            aircraft_id = st.text_input("New Aircraft ID")
            aircraft_company = st.text_input("New Aircraft Company")
            origin = st.text_input("New Origin")
            arrival_time = st.text_input("New Arrival Time")
            departure_time = st.text_input("New Departure Time")
            destination = st.text_input("New Destination")
            if st.form_submit_button("Update Flight"):
                query = f"UPDATE Flight SET AIRCRAFT_ID = '{aircraft_id}', AIRCRAFT_COMPANY = '{aircraft_company}', ORIGIN = '{origin}', ARRIVAL_TIME = '{arrival_time}', DEPARTURE_TIME = '{departure_time}', DESTINATION = '{destination}' WHERE FLIGHT_ID = '{flight_id}'"
                execute_query(query)
                st.success("Flight updated successfully!")

    elif table_name == "Gate":
        with st.form("up_ga_form"):
            gate_id = st.text_input("Gate ID to Update")
            airport_code = st.text_input("New Airport Code")
            if st.form_submit_button("Update Gate"):
                query = f"UPDATE Gate SET AIRPORT_CODE = '{airport_code}' WHERE GATE_ID = '{gate_id}'"
                execute_query(query)
                st.success("Gate updated successfully!")

    elif table_name == "Luggage":
        with st.form("up_lu_form"):
            luggage_id = st.text_input("Luggage ID to Update")
            passenger_id = st.text_input("New Passenger ID")
            weight = st.text_input("New Weight")
            length = st.text_input("New Length")
            width = st.text_input("New Width")
            height = st.text_input("New Height")
            status = st.text_input("New Status")
            no_of_bags = st.text_input("New Number of Bags")
            if st.form_submit_button("Update Luggage"):
                query = f"UPDATE Luggage SET PASSENGER_ID = '{passenger_id}', WEIGHT = {weight}, LENGTH = {length}, WIDTH = {width}, HEIGHT = {height}, STATUS = '{status}', NO_OF_BAGS = {no_of_bags} WHERE LUGGAGE_ID = '{luggage_id}'"
                execute_query(query)
                st.success("Luggage updated successfully!")

    elif table_name == "Passenger":
        with st.form("up_pa_form"):
            passenger_id = st.text_input("Passenger ID to Update")
            name = st.text_input("New Name")
            date_of_birth = st.text_input("New Date of Birth")
            passport_no = st.text_input("New Passport No")
            phone_no = st.text_input("New Phone No")
            email_id = st.text_input("New Email ID")
            if st.form_submit_button("Update Passenger"):
                query = f"UPDATE Passenger SET NAME = '{name}', DATE_OF_BIRTH = '{date_of_birth}', PASSPORT_NO = '{passport_no}', PHONE_NO = {phone_no}, EMAIL_ID = '{email_id}' WHERE PASSENGER_ID = '{passenger_id}'"
                execute_query(query)
                st.success("Passenger updated successfully!")

    elif table_name == "Schedule":
        with st.form("up_sched_form"):
            schedule_id = st.text_input("Schedule ID to Update")
            flight_id = st.text_input("New Flight ID")
            gate_id = st.text_input("New Gate ID")
            arrival_time = st.text_input("New Arrival Time")
            departure_time = st.text_input("New Departure Time")
            if st.form_submit_button("Update Schedule"):
                query = f"UPDATE Schedule SET FLIGHT_ID = '{flight_id}', GATE_ID = '{gate_id}', ARRIVAL_TIME = '{arrival_time}', DEPARTURE_TIME = '{departure_time}' WHERE SCHEDULE_ID = '{schedule_id}'"
                execute_query(query)
                st.success("Schedule updated successfully!")

    elif table_name == "Ticket":
        with st.form("up_tick_form"):
            ticket_id = st.text_input("Ticket ID to Update")
            flight_id = st.text_input("New Flight ID")
            passenger_id = st.text_input("New Passenger ID")
            seat_no = st.text_input("New Seat No")
            price = st.text_input("New Price")
            if st.form_submit_button("Update Ticket"):
                query = f"UPDATE Ticket SET FLIGHT_ID = '{flight_id}', PASSENGER_ID = '{passenger_id}', SEAT_NO = '{seat_no}', PRICE = {price} WHERE TICKET_ID = '{ticket_id}'"
                execute_query(query)
                st.success("Ticket updated successfully!")

# Function to perform DELETE operation for each table
def delete_operation():
    table_name = st.selectbox("Select Table", ["Aircraft", "Airports", "Booking", "Crew", "Flight", "Gate", "Luggage", "Passenger", "Schedule", "Ticket"])

    st.subheader(f"Delete Operation - {table_name}")

    if table_name == "Aircraft":
        with st.form("del_aircraft_form"):
            aircraft_id = st.text_input("Aircraft ID to Delete")
            if st.form_submit_button("Delete Aircraft"):
                query = f"DELETE FROM Aircraft WHERE AIRCRAFT_ID = '{aircraft_id}'"
                execute_query(query)
                st.success("Aircraft deleted successfully!")

    elif table_name == "Airports":
        with st.form("del_airport_form"):
            airport_code = st.text_input("Airport Code to Delete")
            if st.form_submit_button("Delete Airport"):
                query = f"DELETE FROM Airports WHERE AIRPORT_CODE = '{airport_code}'"
                execute_query(query)
                st.success("Airport deleted successfully!")

    elif table_name == "Booking":
        with st.form("del_book_form"):
            booking_id = st.text_input("Booking ID to Delete")
            if st.form_submit_button("Delete Booking"):
                query = f"DELETE FROM Booking WHERE BOOKING_ID = '{booking_id}'"
                execute_query(query)
                st.success("Booking deleted successfully!")

    elif table_name == "Crew":
        with st.form("del_crew_form"):
            crew_id = st.text_input("Crew ID to Delete")
            if st.form_submit_button("Delete Crew"):
                query = f"DELETE FROM Crew WHERE CREW_ID = '{crew_id}'"
                execute_query(query)
                st.success("Crew deleted successfully!")

    elif table_name == "Flight":
        with st.form("del_flight_form"):
            flight_id = st.text_input("Flight ID to Delete")
            if st.form_submit_button("Delete Flight"):
                query = f"DELETE FROM Flight WHERE FLIGHT_ID = '{flight_id}'"
                execute_query(query)
                st.success("Flight deleted successfully!")

    elif table_name == "Gate":
        with st.form("del_gate_form"):
            gate_id = st.text_input("Gate ID to Delete")
            if st.form_submit_button("Delete Gate"):
                query = f"DELETE FROM Gate WHERE GATE_ID = '{gate_id}'"
                execute_query(query)
                st.success("Gate deleted successfully!")

    elif table_name == "Luggage":
        with st.form("del_lug_form"):
            luggage_id = st.text_input("Luggage ID to Delete")
            if st.form_submit_button("Delete Luggage"):
                query = f"DELETE FROM Luggage WHERE LUGGAGE_ID = '{luggage_id}'"
                execute_query(query)
                st.success("Luggage deleted successfully!")

    elif table_name == "Passenger":
        with st.form("del_pass_form"):
            passenger_id = st.text_input("Passenger ID to Delete")
            if st.form_submit_button("Delete Passenger"):
                query = f"DELETE FROM Passenger WHERE PASSENGER_ID = '{passenger_id}'"
                execute_query(query)
                st.success("Passenger deleted successfully!")

    elif table_name == "Schedule":
        with st.form("del_sched_form"):
            schedule_id = st.text_input("Schedule ID to Delete")
            if st.form_submit_button("Delete Schedule"):
                query = f"DELETE FROM Schedule WHERE SCHEDULE_ID = '{schedule_id}'"
                execute_query(query)
                st.success("Schedule deleted successfully!")

    elif table_name == "Ticket":
        with st.form("del_tick_form"):
            ticket_id = st.text_input("Ticket ID to Delete")
            if st.form_submit_button("Delete Ticket"):
                query = f"DELETE FROM Ticket WHERE TICKET_ID = '{ticket_id}'"
                execute_query(query)
                st.success("Ticket deleted successfully!")

if __name__ == '__main__':
    main()