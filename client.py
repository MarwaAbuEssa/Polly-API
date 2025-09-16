import requests
import json

BASE_URL = "http://127.0.0.1:8000"  # Assuming the API is running locally

def cast_vote(poll_id: int, option_id: int, token: str):
    """
    Casts a vote on an existing poll.

    Args:
        poll_id (int): The ID of the poll to vote on.
        option_id (int): The ID of the option to vote for.
        token (str): The authentication token of the user.

    Returns:
        dict: The response from the API, typically the created vote object.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"option_id": option_id}
    response = requests.post(
        f"{BASE_URL}/polls/{poll_id}/vote",
        headers=headers,
        data=json.dumps(data)
    )
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

if __name__ == "__main__":
    # Usage example:
    # This example assumes you have a running API and a valid user token.
    # You would typically obtain a token by logging in first.

    # Replace with a valid token obtained from the /login endpoint
    # For demonstration purposes, let's assume a dummy token.
    # In a real scenario, you'd call a login function to get this token.
    # Example:
    # login_data = {"username": "testuser", "password": "testpassword"}
    # login_response = requests.post(f"{BASE_URL}/login", data=login_data)
    # login_response.raise_for_status()
    # auth_token = login_response.json()["access_token"]
    auth_token = "YOUR_AUTH_TOKEN_HERE" # Replace with a real token

    if auth_token == "YOUR_AUTH_TOKEN_HERE":
        print("Please replace 'YOUR_AUTH_TOKEN_HERE' with a valid authentication token.")
        print("You can obtain one by registering and logging in to the API.")
    else:
        try:
            # Example: Vote on poll with ID 1, for option with ID 1
            poll_id_to_vote = 1
            option_id_to_vote = 1
            
            print(f"Attempting to cast vote on poll {poll_id_to_vote} for option {option_id_to_vote}...")
            vote_result = cast_vote(poll_id_to_vote, option_id_to_vote, auth_token)
            print("Vote cast successfully:")
            print(json.dumps(vote_result, indent=2))
        except requests.exceptions.HTTPError as e:
            print(f"Error casting vote: {e}")
            print(f"Response content: {e.response.json()}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def get_poll_results(poll_id: int):
    """
    Retrieves the results for a specific poll.

    Args:
        poll_id (int): The ID of the poll to retrieve results for.

    Returns:
        dict: The poll results from the API.
    """
    response = requests.get(f"{BASE_URL}/polls/{poll_id}/results")
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


    try:
        # Example: Get results for poll with ID 1
        poll_id_for_results = 1
        print(f"\nAttempting to retrieve results for poll {poll_id_for_results}...")
        results = get_poll_results(poll_id_for_results)
        print("Poll results retrieved successfully:")
        print(json.dumps(results, indent=2))
    except requests.exceptions.HTTPError as e:
        print(f"Error retrieving poll results: {e}")
        print(f"Response content: {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_poll_chart_data_client(poll_id: int):
    """
    Retrieves poll results data for charting.

    Args:
        poll_id (int): The ID of the poll to retrieve chart data for.

    Returns:
        dict: The poll chart data from the API.
    """
    response = requests.get(f"{BASE_URL}/polls/{poll_id}/chart_data")
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


    try:
        # Example: Get chart data for poll with ID 1
        poll_id_for_chart = 1
        print(f"\nAttempting to retrieve chart data for poll {poll_id_for_chart}...")
        chart_data = get_poll_chart_data_client(poll_id_for_chart)
        print("Poll chart data retrieved successfully:")
        print(json.dumps(chart_data, indent=2))
    except requests.exceptions.HTTPError as e:
        print(f"Error retrieving poll chart data: {e}")
        print(f"Response content: {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")