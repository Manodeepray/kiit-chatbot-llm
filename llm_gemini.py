import google.generativeai as genai
import os

genai.configure(api_key = "AIzaSyBKsyvw-c3WFy9tWncfiWIPTC1-e_5XPiQ")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)