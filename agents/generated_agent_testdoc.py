import requests
import json
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NWSAPIClient:
    """
    A client for interacting with the National Weather Service (NWS) API.
    """

    API_BASE_URL = "https://api.weather.gov"
    DEFAULT_USER_AGENT = "(myweatherapp.com, contact@myweatherapp.com)"  # Required by NWS API

    def __init__(self, user_agent=None):
        """
        Initializes the NWSAPIClient.

        Args:
            user_agent (str, optional):  User agent string.  If None, uses DEFAULT_USER_AGENT.
        """
        self.user_agent = user_agent if user_agent else self.DEFAULT_USER_AGENT
        self.headers = {"User-Agent": self.user_agent, "Accept": "application/geo+json"}
        self.max_retries = 3  # Maximum number of retries for API calls
        self.retry_delay = 2  # Delay in seconds between retries

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the specified NWS API endpoint with retry logic.

        Args:
            endpoint (str): The API endpoint to call (e.g., "/points/39.7456,-97.0892").
            params (dict, optional): Query parameters to include in the request. Defaults to None.

        Returns:
            dict: The JSON response from the API, or None if the request fails after multiple retries.
        """

        url = f"{self.API_BASE_URL}{endpoint}"
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

                # Check content type
                content_type = response.headers.get('Content-Type', '')
                if 'application/geo+json' not in content_type and 'application/ld+json' not in content_type and 'application/json' not in content_type:
                    logging.error(f"Unexpected Content-Type: {content_type}")
                    return None

                return response.json()
            except requests.exceptions.HTTPError as e:
                logging.error(f"HTTP Error: {e}")
                if response.status_code == 403:  # Forbidden - likely User-Agent issue
                    logging.error(f"Check your User-Agent: {self.user_agent}")
                    return None # Stop retrying, as it's likely a configuration error

                if response.status_code == 429:  # Too Many Requests
                    logging.warning("Rate limit exceeded. Retrying after delay.")
                elif 500 <= response.status_code < 600: # Server error
                    logging.warning(f"Server error ({response.status_code}). Retrying after delay.")
                else: # Other HTTP error, don't retry
                    return None

            except requests.exceptions.RequestException as e:
                logging.error(f"Request Exception: {e}")

            if attempt < self.max_retries - 1:
                time.sleep(self.retry_delay)
            else:
                logging.error("Max retries reached. Request failed.")
                return None

    def get_points(self, latitude, longitude):
        """
        Gets the point information for a given latitude and longitude.

        Args:
            latitude (float): The latitude.
            longitude (float): The longitude.

        Returns:
            dict: The JSON response from the API, or None if the request fails.
        """
        endpoint = f"/points/{latitude},{longitude}"
        return self._make_request(endpoint)

    def get_forecast(self, office, grid_x, grid_y):
        """
        Gets the forecast for a given grid point.

        Args:
            office (str): The office ID.
            grid_x (int): The grid X coordinate.
            grid_y (int): The grid Y coordinate.

        Returns:
            dict: The JSON response from the API, or None if the request fails.
        """
        endpoint = f"/gridpoints/{office}/{grid_x},{grid_y}/forecast"
        return self._make_request(endpoint)

    def get_alerts_active_zone(self, zone_id):
        """
        Gets active alerts for a specific zone.

        Args:
            zone_id (str): The zone ID.

        Returns:
            dict: The JSON response from the API, or None if the request fails.
        """

        endpoint = f"/alerts/active/zone/{zone_id}"
        return self._make_request(endpoint)


if __name__ == "__main__":
    # Example Usage:
    client = NWSAPIClient() # Using default user agent, change if needed

    # 1. Get point information for a location:
    point_data = client.get_points(39.7456, -97.0892)
    if point_data:
        print("Point Data:")
        print(json.dumps(point_data, indent=2))

        # 2. Get forecast for the gridpoint specified in the point data:
        office = point_data['properties']['gridId']
        grid_x = point_data['properties']['gridX']
        grid_y = point_data['properties']['gridY']

        forecast_data = client.get_forecast(office, grid_x, grid_y)
        if forecast_data:
            print("\nForecast Data:")
            print(json.dumps(forecast_data, indent=2))
        else:
            print("\nFailed to retrieve forecast data.")

    else:
        print("Failed to retrieve point data.")

    # 3. Get active alerts for a zone (example zone):
    alerts = client.get_alerts_active_zone("VAZ079")
    if alerts:
        print("\nActive Alerts for VAZ079:")
        print(json.dumps(alerts, indent=2))
    else:
        print("\nFailed to retrieve active alerts for VAZ079.")