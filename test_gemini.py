from main import client

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Say hello"
)

print(response.text)