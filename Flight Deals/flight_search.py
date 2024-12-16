import requests, os, dotenv
from datetime import datetime, timedelta

dotenv.load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        """
           Initialize an instance of the FlightSearch class.
           This constructor performs the following tasks:
           1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
           and 'AMADEUS_SECRET' respectively.
           Instance Variables:
           _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
           _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
           _token (str): The authentication token obtained by calling the _get_new_token method.
        """
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self.retrieve_token()

    def retrieve_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_iata_code(self, city_name):
        """
            Retrieves the IATA code for a specified city using the Amadeus Location API.
            Parameters:
            city_name (str): The name of the city for which to find the IATA code.
            Returns:
            str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
            or "Not Found" if no match is found due to a KeyError.

            The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
            name and other parameters to refine the search. It then attempts to extract the IATA code
            from the JSON response.
            - If the city is not found in the response data (i.e., the data array is empty, leading to
            an IndexError), it logs a message indicating that no airport code was found for the city and
            returns "N/A".
            - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading
            to a KeyError), it logs a message indicating that no airport code was found for the city
            and returns "Not Found".
        """
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        res = requests.get(url=url, params=params, headers=headers)
        res.raise_for_status()

        try:
            code = res.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Searches for flight options between two cities on specified departure and return dates
        using the Amadeus API.

        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.

        Returns:
            dict or None: A dictionary containing flight offer data if the query is successful; None
            if there is an error.

        The function constructs a query with the flight search parameters and sends a GET request to
        the API. It handles the response, checking the status code and parsing the JSON data if the
        request is successful. If the response status code is not 200, it logs an error message and
        provides a link to the API documentation for status code details.
        """
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "TWD",
            "max": "10",
        }

        res = requests.get(url=endpoint, headers=headers, params=params)

        if res.status_code != 200:
            print(f"check_flights() response code: {res.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", res.text)
            return None

        return res.json()

flight_search = FlightSearch()
tomorrow = datetime.today() + timedelta(days=1)
flight_search.check_flight("TPE", 'NRT', tomorrow, tomorrow + timedelta(days=6 * 30))