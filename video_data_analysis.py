import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("video_data.csv")

#Initialise each different plot.
fig, axs = plt.subplots(1, 2)
fig2, axs2 = plt.subplots()

#Content Type Data Visualisation
content_types = ["Game", "Simulator", "Discussion", "Software"]
content_type_mapping = {
    "Game": 1,
    "Simulator": 2,
    "Discussion": 3,
    "Software": 4
}

for type in content_types:
    #Create a copy of the original dataframe to avoid overwriting data.
    new_df = df.copy() 

    #A dataframe to record the frequency of each individual type of game. 
    if type == "Game":
        game_df =  new_df.loc[new_df["Content Overview"].str.contains(type)]
        grouped_game_df = game_df.groupby("Content Overview").agg({"Video": "count"}).reset_index()

    #A dataframe to record data about each individual content type defined in the content_types list.
    new_df.loc[new_df["Content Overview"].str.contains(type), "Content Type"] = content_type_mapping[type]
    grouped_type_df = new_df.groupby("Content Type").agg({"Video": "count", "Likes": "sum"}).reset_index()

    #Create a bar chart for the number of videos per content type.
    axs[0].bar(grouped_type_df["Content Type"], grouped_type_df["Video"], label=type)
    
    #Create a bar chart for the total likes per content type.
    axs[1].bar(grouped_type_df["Content Type"], grouped_type_df["Likes"], label=type)

    #Create a bar chart for the number of videos per game type.
    axs2.bar(grouped_game_df["Content Overview"], grouped_game_df["Video"])

#Video Style Visualisation
style_df = df.groupby(["Video Style", "Subtitles"]).size().unstack().reset_index()
style_df = style_df[style_df.columns[::-1]]
style_df = style_df.drop(columns="Video Style")
fig3 = style_df.plot(kind="bar", stacked=True)

#Format the labels and axes for each plot.
axs[0].set_xlabel("Content Type")
axs[0].set_ylabel("Number of Videos")
axs[0].set_title("Number of Videos per Content Type")
axs[0].set_xticks(list(content_type_mapping.values()))
axs[0].set_xticklabels(["Game", "Simulator", "Discussion", "Miscellaneous\nSoftware"])
axs[0].set_yticks(range(0,30,5))

axs[1].set_xlabel("Content Type")
axs[1].set_ylabel("Total Likes")
axs[1].set_title("Total Likes per Content Type")
axs[1].set_xticks(list(content_type_mapping.values()))
axs[1].set_xticklabels(["Game", "Simulator", "Discussion", "Miscellaneous\nSoftware"])
axs[1].set_yticks(range(0,1000000,100000))

axs2.set_xlabel("Game Type")
axs2.set_ylabel("Number of Videos")
axs2.set_title("Number of Videos per Game Type")
axs2.set_xticks(range(5))
axs2.set_xticklabels(["Cooking", "Language", "Music", "Science", "Sports"])

fig3.set_xlabel("Video Style")
fig3.set_ylabel("Number of Videos")
fig3.set_title("Number of Videos per Video Style")
fig3.set_xticks(range(4))
fig3.set_xticklabels(range(1,5))
fig3.set_yticks(range(0,22,2))
fig3.legend(title="Subtitles", labels=["With Subtitles", "Without Subtitles", "No Speech"])

# Display the subplots
plt.show()