# HTTP Client Real and Simulated

import requests
import json


class HTTPClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint, method='GET', params=None, data=None, headers=None):
        raise NotImplementedError("Subclasses must implement make_request method")


class RealHTTPClient(HTTPClient):
    def make_request(self, endpoint, method='GET', params=None, data=None, headers=None):
        url = self.base_url + endpoint
        response = requests.request(method, url, params=params, data=data, headers=headers)
        return response


class SimulatedHTTPClient(HTTPClient):
    def __init__(self, base_url, har_file):
        super().__init__(base_url)
        self.har_file = har_file
        self.requests = self._load_har_file()
        self.current_index = 0

    def _load_har_file(self):
        with open(self.har_file, 'r') as file:
            har_data = json.load(file)
        return har_data['log']['entries']

    def make_request(self, endpoint, method='GET', params=None, data=None, headers=None):
        if self.current_index >= len(self.requests):
            raise IndexError("No more requests in HAR file")

        request_data = self.requests[self.current_index]
        self.current_index += 1

        request_url = request_data['request']['url']
        request_method = request_data['request']['method']
        response = request_data['response']['content']['text']

        # Simulate network delay
        # You may adjust this delay as needed
        import time
        time.sleep(1)

        # Log the simulated request
        print(f"Simulating Request - {request_method} {request_url}")

        # Return a mock response
        return MockResponse(status_code=200, content=response)


class MockResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def json(self):
        return self.content # json.loads(self.content)


# Example usage real:
real_client = RealHTTPClient("https://jsonplaceholder.typicode.com")
real_response = real_client.make_request("/todos/1")

print("Real Response Status Code:", real_response.status_code)
print("Real Response JSON:", real_response.json())

# Example usage simulated:
simulated_client = SimulatedHTTPClient("https://jsonplaceholder.typicode.com", "jsonplaceholder.typicode.com.har")
simulated_response = simulated_client.make_request("/todos/1")

print("Simulated Response Status Code:", simulated_response.status_code)
print("Simulated Response JSON:", simulated_response.json())


