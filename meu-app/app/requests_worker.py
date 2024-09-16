import requests

def call_external_api():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        print(data) 
    except requests.RequestException as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    call_external_api()
