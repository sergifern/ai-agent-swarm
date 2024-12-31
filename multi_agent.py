from swarm import Swarm, Agent
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Define the first agent

def identify_problem(context_variables):
    # Logic to identify the problem
    print("Identifying the problem...")
    return agent_b

agent_a = Agent(
    name="Problem Identifier",
    instructions="Identify the user's problem and pass it to the next agent.",
    functions=[identify_problem],
    model="gpt-3.5-turbo"  # Fast model
)

# Define the second agent

def handle_payment(context_variables):
    # Logic to handle payment
    print("Handling payment...")
    return "Payment processed."

agent_b = Agent(
    name="Payment Handler",
    instructions="Handle payment-related queries.",
    functions=[handle_payment],
    model="gpt-4"  # More powerful model
)

# Create the Swarm client
client = Swarm()

# Run the loop conversation
while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break

    response = client.run(
        agent=agent_a,
        messages=[{"role": "user", "content": user_input}]
    )

    print("Response:", response.messages[-1]["content"])