import datetime
from pathlib import Path
from transformers import pipeline
import os

start = datetime.datetime.now()
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
summarizer = pipeline("summarization")
# summarizer = pipeline("summarization", model='sshleifer/distilbart-cnn-12-6')
# Model
# https://huggingface.co/sshleifer/distilbart-cnn-12-6
# News
# https://edition.cnn.com/2022/01/28/politics/wayne-stenehjem-north-dakaota-attorney-general-dies/index.html
text = """Wayne Stenehjem, North Dakota's longest-serving attorney general, has died "unexpectedly" at age 68, 
according to a news release from the Attorney General's Office. 
"It is with the utmost sadness that the Office of Attorney General announces that Attorney General Wayne Stenehjem 
passed away unexpectedly on Friday January 28, 2022. He was 68," the release said. The office said funeral 
arrangements are pending. A cause of death was not provided. "We know Wayne was a widely respected and well-known 
public figure, but we ask that his family be allowed time to grieve in private," the statement said. According to 
North Dakota Gov. Doug Burgum's office, Stenehjem was the longest-serving attorney general in the state's history, 
having held the position for 21 years after being elected in 2000. He announced in December that he would not seek 
another term as attorney general. Prior to his time as the state's attorney general, Stenehjem spent 24 years in the 
North Dakota Legislature. Burgum extended his condolences in a statement on Friday. "Like so many North Dakotans who 
treasured his friendship and admired him for his more than four decades of exceptional service to our state, 
we are absolutely devastated by the passing of Attorney General Wayne Stenehjem," said Burgum, a Republican. "Wayne 
embodied public service, both as a dedicated legislator and the longest-serving attorney general in our state's 
133-year history." "As the top law enforcement officer in North Dakota for over two decades, Attorney General 
Stenehjem always put the safety and well-being of our citizens first. North Dakota is a safer place because of his 
unwavering commitment to law and order, his loyalty to his team members and his utmost respect for our men and women 
in uniform." The governor directed all state government agencies to fly the US and North Dakota flags at half-staff 
until further notice. """

summary_text = summarizer(text, max_length=100, min_length=5, do_sample=False)[0]['summary_text']
end = datetime.datetime.now()
print(end-start)
Path('summary.txt').write_text(summary_text, encoding='utf-8')
