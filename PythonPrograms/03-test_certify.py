#!/usr/bin/env python3

import json
import locale
import sys
import os
import reports
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sale = {"sale":0}
  dict_pop = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    item_sale = item["total_sales"]
    key = item['car']['car_year']
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item_sale > max_sale['sale']:
        item['sale'] = item_sale
        max_sale = item
    # TODO: also handle most popular car_year
    if not key in dict_pop:
        dict_pop[key] = item["total_sales"]
    else:
    dict_pop[key] +=  item["total_sales"]
year_max = max(dict_pop.keys(), key = (lambda k:dict_pop[k]))
summary = [
 "The {} generated the most revenue: ${}".format(
   format_car(max_revenue["car"]), max_revenue["revenue"]),
 "The {} had the most sales: {}".format(format_car(max_sale["car"]),max_sale["sale"]),
 "The most popular year was {} with {} sales.".format(year_max, dict_pop[year_max]),
 ]

return summary


def cars_dict_to_table(car_data):
"""Turns the data in car_data into a list of lists."""
table_data = [["ID", "Car", "Price", "Total Sales"]]
car_data = sorted(car_data,key= lambda i: (i['total_sales']),reverse=True)
for item in car_data:
 table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
return table_data

def generate_paragraph(summary_table):
paragraph = ''
for item in summary_table:
  paragraph += str(item) + '\n'
return paragraph

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  file_path = "/home/" + os.environ.get('USER') + "/car_sales.json"
  data = load_data(file_path)
  summary = process_data(data)
  body = generate_paragraph(summary)
  print(body)
  paragraph = body.replace('\n',"<br/>")
  # TODO: turn this into a PDF report
  table_data = cars_dict_to_table(data)
  #reports.generate("/tmp/cars.pdf", "Sales summary for last month", paragraph, table_data)
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  #message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  #emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
