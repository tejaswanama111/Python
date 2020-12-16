import wolframalpha 
  
# Taking input from user 
question = input('Question: ') 
  
# App id obtained by the above steps 
app_id = 'A92R58-99EWG2TW76' 
  
# Instance of wolf ram alpha  
# client class 
client = wolframalpha.Client('A92R58-99EWG2TW76') 
  
# Stores the response from  
# wolf ram alpha 
res = client.query(question) 
  
# Includes only text from the response 
answer = next(res.results).text 
  
print(answer) 