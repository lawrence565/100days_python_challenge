#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight

from data_manager import DataManager
from datetime import datetime, timedelta
import time

BASE_AIRPORT = "TPE"

dataManager = DataManager()
sheet_data = dataManager.get_destination_data()
flightSearch = FlightSearch()
notification_manager = NotificationManager()

# ----------------- Initiate Sheet Data ------------------ #
# Check the sheet and refine it
for row in sheet_data:
    if not row.get("iataCode") or len(row["iataCode"]) != 3:
        row["iataCode"] = flightSearch.get_iata_code(row.get("city", ""))
        time.sleep(2)
dataManager.destination_data = sheet_data
dataManager.update_iata_code()

# -------------------- Main mechanism -------------------- #
# Search the lowest price
tomorrow = datetime.today() + timedelta(days=1)
six_month_later = tomorrow + timedelta(days=6 * 30)
for destination in sheet_data:
    flight_data = flightSearch.check_flight(
        BASE_AIRPORT,
        destination['iataCode'],
        is_direct="true",
        from_time=tomorrow,
        to_time=six_month_later
    )

    cheapest_flight = find_cheapest_flight(flight_data)

    if cheapest_flight.price == "N/A":
        flight_data = flightSearch.check_flight(
            BASE_AIRPORT,
            destination['iataCode'],
            is_direct="false",
            from_time=tomorrow,
            to_time=six_month_later
        )

    cheapest_flight = find_cheapest_flight(flight_data)
    print(f"{destination['city']}: NT${cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and (cheapest_flight.price < destination.get("lowestPrice") or int(destination.get("lowestPrice")) == 0):
        print(f"Lower price flight found to {destination['city']}!")
        for user in dataManager.user_data:
            notification_manager.send_email(
                email=user['emailAddress'],
                message_body=f"Hi {user.get('firstName')}, Low price alert! Only NT${cheapest_flight.price} to fly "
                             f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                             f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        destination["lowestPrice"] = cheapest_flight.price
    time.sleep(2)
dataManager.destination_data = sheet_data
dataManager.update_lowest_price()