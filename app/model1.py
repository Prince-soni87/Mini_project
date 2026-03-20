import google.generativeai as genai

genai.configure(api_key="AIzaSyDbJLIknXZi2RdLoUOTNv5NMjrZx4Pnh_U")

models = genai.list_models()

for model in models:
    print(model.name)