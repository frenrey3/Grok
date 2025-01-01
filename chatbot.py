import requests

class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.xai.com/v1/chat"

    def send_message(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "message": message
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()

    def get_response(self, message):
        response = self.send_message(message)
        return response.get("response", "Sorry, I didn't understand that.")

def main():
    api_key = "your_xai_api_key_here"
    chatbot = Chatbot(api_key)

    print("Welcome to the XAI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
