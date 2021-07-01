"""
Program: Show Latest COVID Details of Pakistan as Notification on Desktop

Programmer: HUSSNAIN AHMAD

Date: 01 July 2021
"""
import requests
from win10toast import ToastNotifier

# Send API request
try:
    data = requests.get("https://api.covid19api.com/summary")

    # COVID Data of Pakistan
    jsonData = data.json()
    country = jsonData["Countries"][129]["Country"]
    NewConfirmed = jsonData["Countries"][129]["NewConfirmed"]
    TotalConfirmed = jsonData["Countries"][129]["TotalConfirmed"]
    NewDeaths = jsonData["Countries"][129]["NewDeaths"]
    TotalDeaths = jsonData["Countries"][129]["TotalDeaths"]
    NewRecovered = jsonData["Countries"][129]["NewRecovered"]
    TotalRecovered = jsonData["Countries"][129]["TotalRecovered"]
    DateObj = jsonData["Countries"][129]["Date"]
    Date = DateObj[0:10]
    Time = DateObj[11:19]

# Title and Description of the Notification
# Based on errors like no internet connection

    notificationTitle = f"{country} COVID Details"
    notificationDesc = f"Updated: {Date}\nCases: {NewConfirmed}, Deaths: {NewDeaths}, Recovered: {NewRecovered}"
except:
    notificationTitle = "Pakistan COVID Details"
    notificationDesc = "You are not connected to the internet"


# Showing the Notification
toaster = ToastNotifier()
toaster.show_toast(notificationTitle,
notificationDesc,
icon_path="virus.ico",
duration=20)