import os
import time
import json
import ollama

from openai import OpenAI
from langchain.tools import tool
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY_TWO"))

system_context = """
You are an assistant designed to extract specific information from a raw, unformatted, and 
uncleaned piece of text. Extract the following information from the text, if available. If less 
than half of the required information is found, output 'no information'. If more than half of the required 
information is found, leave the missing information blank. The output must follow the provided format structure.

Example Structure of Information to Extract from Each Chunk, If Found:
###
Course Name -- Enter course name

Course Definition -- Master the essentials of web development with HTML, CSS, and JavaScript on our interactive learning platform.

Course Description -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Learning Objectives --
1. Create responsive and interactive web pages
2. Build and style web layouts
3. Manipulate the document object model
4. Collaborate using version control

Timeline -- 4 Months

Recommended Experience -- Beginner Level

Tools Needed -- Laptop

Course Content
1. Module One Name: Introduction to Wireframe
   Module One Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
2. Module Two Name: Introduction to HTML tags
   Module Two Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
###
   
Instructions:

1. Extract the required information from the text.
2. If less than half of the required information is found, output 'NO INFORMATION'.
3. If more than half of the required information is found, leave the missing information blank.
4. the output MUST be formatted according to the provided structure.

If less than half of the required information is found, output 'NO INFORMATION'.
"""
backticks = f'````'

def answer(message,
             model= 'gpt-3.5-turbo',
             max_tokens = 4096):
  response = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": system_context},
    {"role": "user", "content": message},
  ]
)
  return response.choices[0].message.content

class BingScrapeTool:

   @tool("Scrape website content to extract information about courses")
   def bing_scrape(course_query: str ):
      """Useful for scrapping and summarizing content from a website by
         searching microsoft bing for specific queries like 'machine learning 
         in python course' 'course' must be in the query"""
      try:
            SBR_WEBDRIVER = 'https://brd-customer-hl_7b582a0b-zone-scraping_browser2:czxscfcdxiq8@brd.superproxy.io:9515'
            chrome_options = Options()
            chrome_options.binary_location = "/usr/bin/google-chrome"
            driver = webdriver.Remote(command_executor=SBR_WEBDRIVER, options=chrome_options)
            driver.get('https://bing.com/')

            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sb_form_q'))
               )
            input_element = driver.find_element(By.ID, 'sb_form_q')
            input_element.clear()
            input_element.send_keys(f'{course_query}' + Keys.ENTER)

            WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
               )

            courses_elements = driver.find_elements(By.CSS_SELECTOR, 'li h2 a')
            courses_links = [elem.get_attribute('href') for elem in courses_elements if 'course' in elem.text.lower()]
            print(courses_links[0])
            driver.quit()
            main_list = []

            if len(courses_links) > 10:
               sliced_links = courses_links[:10]
            else:
               sliced_links = courses_links[:]

            for link in sliced_links:
                  chrome_options = Options()
                  chrome_options.binary_location = "/usr/bin/google-chrome"
                  driver = webdriver.Remote(command_executor=SBR_WEBDRIVER, options=chrome_options)
                  driver.get(link)
                  WebDriverWait(driver, 20).until(
                     EC.presence_of_element_located((By.TAG_NAME, 'body'))
                  )
                  page_source = driver.page_source
                  driver.quit()
                  
                  parsed = BeautifulSoup(page_source, 'html.parser')
                  text = parsed.get_text()

                  cleaned_text = ' '.join([i for i in text.split('\n') if i.strip() != ''])
                  cleaned_text = " ".join([i for i in cleaned_text.split(' ') if i.strip() != ""])
                  main_list.append(cleaned_text)
            print(main_list[0])

            main_text = ''
            for i in main_list:
               try:
                  
                  sub_result = answer(str(i))
                  main_text += f'\n{backticks}\n' + sub_result

               except:
                  
                  response = ollama.chat(model='llama_scrape',
                                             messages=[{
                                                'role': 'user',
                                                'content': str(i)
                                             },
                                             ])
                  sub_result = response['message']['content']
                  main_text += f'\n{backticks}\n' + sub_result
                  
            return main_text

      except Exception as e:
            print(str(e))
            return ""
  

  



if __name__ == "__main__":
   course_query = input("Enter the course query: ")
   result = BingScrapeTool.bing_scrape(course_query)

   print(result)