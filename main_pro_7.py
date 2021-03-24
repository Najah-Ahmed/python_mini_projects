import requests

r=requests.post('https://textbelt.com/text',{
  'phone':'+25255555555',
  'message':'Hello jahn deo iska wrn wa najah o marakeykanka joogta ',
  'key':'textbelt', #free key 
})
print(r.json())