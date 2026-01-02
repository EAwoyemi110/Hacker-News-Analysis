
'''
title: Analyzing Yc hacker news
paragraph:
In this project, I took a deep dive into the Hacker News community—a
massive hub for tech enthusiasts and startup founders—to figure out what
makes a post actually get noticed. My primary goal was to see if there’s a
"secret formula" for engagement by comparing how well Ask HN and Show HN posts perform.
Beyond just the type of post, I wanted to find out if the timing of a submission could be the
difference between a post that goes viral and one that gets ignored. Working within a Jupyter Notebook,
and Pycharm IDE
I used Python’s built-in csv module to handle the raw data and the datetime library to navigate the
complexities of time zones and hourly trends. This project wasn't just about crunching numbers;
it was about using data to uncover the best time for a user to hit "submit" and maximize their
chance of starting a real conversation.
'''
import csv
import datetime as dt
import matplotlib.pyplot as plt


with open("hacker_news.csv", "r") as f:
    reader = csv.reader(f)
    hn = list(reader)

#print(hacker[0:5])

hn_head = hn[0]
hn_data = hn[1:]

print(hn_head, "\n")



#filter data
ask_posts = []

show_posts = []

other_posts = []

for row in hn_data:
    title = row[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(row)
    elif title.lower().startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

#average # of comments and posts for each

total_ask_comments = 0
for row in ask_posts:
    total_ask_comments += int(row[4])

#avg
avg_ask_comments = total_ask_comments / len(ask_posts) if ask_posts else 0
print(avg_ask_comments)

total_show_comments = 0
for row in show_posts:
    total_show_comments += int(row[4])

avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)


#posts per hour
result_list = []


## Iterate over ask_posts to get created_at and number of
for row in ask_posts:
    created_at = row[6]
    num_comments = int(row[4])
    result_list.append([created_at, num_comments])

#dictionaries to make key, value pairs of comments and when they were made
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    date_str = row[0]
    comment = row[1]

    # Parse the date string and extract the hour
    # Note: Hacker News format is typically "MM/DD/YYYY HH:MM"
    date_dt = dt.datetime.strptime(date_str, "%m/%d/%Y %H:%M")
    hour = date_dt.strftime("%H")

    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comment
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += comment

# To verify, you can print the dictionaries
print("Posts per hour:", counts_by_hour)
print("Comments per hour:", comments_by_hour)


avg_by_hour = []

for hour in counts_by_hour:
    #use key (hour) to get values from both dicts
    total_comments = comments_by_hour[hour]
    num_posts = counts_by_hour[hour]

    #find avg
    avg = total_comments / num_posts

    avg_by_hour.append([hour, avg])

print(f"Average By hour: {avg_by_hour}")

swap_avg_by_hour = []

for element in avg_by_hour:
    swap_avg_by_hour.append([element[1], element[0]])

print(swap_avg_by_hour)
sorted_swap = sorted(swap_avg_by_hour, reverse=True)
#Decsencding order

print("Top 5 Hours for Ask Posts Comments: ")
for avg, hour in sorted_swap[:5]:
    hour_dt = dt.datetime.strptime(hour, "%H")
    formatted_hour = hour_dt.strftime("%H:%M")

    print(f"{formatted_hour}: {avg:.2f} average comments per post")

print("Conclusion: 15:00 is the best time to ask a question on the forum.")

#plot data on graph
# Sort hours numerically so the x-axis is in time order
avg_by_hour_sorted = sorted(avg_by_hour, key=lambda x: int(x[0]))

hours = [hour for hour, avg in avg_by_hour_sorted]
avg_comments = [avg for hour, avg in avg_by_hour_sorted]

plt.figure()
plt.bar(hours, avg_comments)
plt.xlabel("Hour of Day (24-hour format)")
plt.ylabel("Average Number of Comments")
plt.title("Average Number of Comments on Ask HN Posts by Hour")

plt.show()


print("Analysis done by Emmanuel Awoyemi")

