import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.cluster import KMeans

#Import the video data from the csv file.
df = pd.read_csv("video_data.csv")

def content_type_plots():
    '''
    Creates plots to visualise data about each different content type.
    The first graph displays the number of videos and mean number of likes per content type.
    The second graph displays the cumulative frequency of each individual type of game.
    '''
    fig, axs = plt.subplots()
    fig2, axs2 = plt.subplots()

    result_df = pd.DataFrame()
    game_result_df = pd.DataFrame()

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

        #Group the dataframe by game type, recording the frequency of each individual type.
        if type == "Game":
            game_df =  new_df.loc[new_df["Content Overview"].str.contains(type)]
            grouped_game_df = game_df.groupby("Content Overview").agg({"Video": "count"}).reset_index()
            game_result_df = pd.concat([game_result_df, grouped_game_df], ignore_index=True)

            #Calculate the cumulative frequency for each game type, in descending order of frequency.
            game_result_df = game_result_df.sort_values(by="Video", ascending=False)
            game_result_df["Cumulative Videos"] = game_result_df["Video"].cumsum()

        #Group the dataframe by content type, recording the number of videos and mean number of likes for each type.
        new_df.loc[new_df["Content Overview"].str.contains(type), "Content Type"] = content_type_mapping[type]
        grouped_type_df = new_df.groupby("Content Type").agg({"Video": "count", "Likes": "mean"}).reset_index()
        result_df = pd.concat([result_df, grouped_type_df], ignore_index=True)

    #Create a bar chart for the number of videos per content type.
    axs.bar(result_df["Content Type"], result_df["Video"], color=['red', 'green', 'orange', 'blue'], alpha=0.75, label="Number of Videos")
        
    #Create a line graph on the same axes for the mean number of likes per content type.
    axs_twin = axs.twinx()
    axs_twin.plot(result_df["Content Type"], result_df["Likes"], marker=".", ms=10, ls="-", lw=2, c="k", label="Mean Number of Likes") 

    #Create a bar chart and line graph for the cumulative number of videos per game type.
    axs2.bar(game_result_df["Content Overview"], game_result_df["Cumulative Videos"], color="red", alpha=0.75)
    axs2.plot(game_result_df["Content Overview"], game_result_df["Cumulative Videos"], marker=".", c="k")

    #Format the labels and axes for each plot.
    axs.set_xlabel("Content Type", size="large")
    axs.set_ylabel("Number of Videos", size="large")
    axs.set_title("Number of Videos and Mean Number of Likes per Content Type", size="x-large")
    axs.set_xticks(list(content_type_mapping.values()))
    axs.set_xticklabels(["Game", "Simulator", "Discussion", "Miscellaneous\nSoftware"])
    axs.set_yticks(range(0,30,5))

    axs_twin.set_ylabel("Mean Number of Likes", size="large")
    axs_twin.set_ylim(0, 45000)
    axs_twin.margins(0)
    
    #Create a legend for the plot.
    lines, labels = axs.get_legend_handles_labels()
    lines2, labels2 = axs_twin.get_legend_handles_labels()
    axs.legend(lines + lines2, labels + labels2, loc="upper right")

    axs2.set_xlabel("Game Type", size="large")
    axs2.set_ylabel("Cumulative Number of Videos", size="large")
    axs2.set_title("Cumulative Number of Videos per Game Type", size="x-large")
    axs2.set_xticks(range(5))
    axs2.set_xticklabels(["Language", "Sports", "Music", "Cooking", "Science"])
    axs2.set_yticks(range(0,25,5))

def video_style_plot():
    '''
    Creates a plot to visualise data about each different video style.
    The graph displays the number of videos and mean number of likes per video style.
    '''
    fig, axs = plt.subplots()

    #Group the dataframe by video style and subtitle type, recording the number of videos per video style per subtitle type.
    style_count_df = df.groupby(["Video Style", "Subtitles"]).agg({"Video": "count"}).reset_index()

    #Pivot the dataframe to ensure that it is in a format suitable for plotting.
    pivot_df = style_count_df.pivot(index="Video Style", columns="Subtitles", values="Video").reset_index().fillna(0)
    pivot_df = pivot_df[pivot_df.columns[::-1]] #Reverse the column order.
    
    #Create a stacked bar chart with separate sections for each subtitle type.
    axs.bar(pivot_df["Video Style"], pivot_df[1], label="With Subtitles")
    axs.bar(pivot_df["Video Style"], pivot_df[0], bottom=pivot_df[1], label="Without Subtitles")
    axs.bar(pivot_df["Video Style"], pivot_df[-1], bottom=pivot_df[1] + pivot_df[0], label="No Speech")

    #Group the dataframe by video style, recording the mean number of likes per video style.
    style_likes_df = df.groupby("Video Style").agg({"Likes": "mean"}).reset_index()
    
    #Create a line graph on the same axes for the mean number of likes per video style.
    axs_twin = axs.twinx()
    axs_twin.plot(style_likes_df["Video Style"], style_likes_df["Likes"], marker=".", ms=10, ls="-", lw=2, c="k", label="Mean Number of Likes")

    #Format the labels and axes for the plot.
    axs.set_xlabel("Video Style", size="large")
    axs.set_ylabel("Number of Videos", size="large")
    axs.set_title("Number of Videos and Mean Number of Likes per Video Style", size="x-large")
    axs.set_xticks(range(1,5))
    axs.set_yticks(range(0,22,2))

    axs_twin.set_ylabel("Mean Number of Likes", size="large")
    axs_twin.set_ylim(0, 70000)
    axs_twin.margins(0)

    #Create a legend for the plot.
    lines, labels = axs.get_legend_handles_labels()
    lines2, labels2 = axs_twin.get_legend_handles_labels()
    axs.legend(lines + lines2, labels + labels2, loc="upper right")

def video_scenes_plot():
    ''' 
    Creates a plot to visualise each video's scene data.
    The graph displays the number of scenes against the average scene length for each video.
    The size of the marker depends on how many likes the video has. The square root is used to maintain relative marker size.
    '''
    fig, axs = plt.subplots()

    #The values to be plotted on the scatter graph.
    data = df[["Number of Scenes", "Average Scene Length"]].values 

    #Apply k-means clustering to the data, with 3 distinct clusters.
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(data)
    df["Cluster"] = kmeans.labels_
    clusters = [data[df["Cluster"] == i] for i in range(3)]

    sizes = np.sqrt(df["Likes"]) 
    colors = ["r", "g", "b"]
    markers = ["s", "o", "^"]

    #Loop through each individual cluster.
    for i, cluster in enumerate(clusters):
        plt.scatter(cluster[:, 0], cluster[:, 1], s=sizes[df["Cluster"] == i], c=colors[i], marker=markers[i], alpha=0.4, label=f'Cluster {i+1}')

    #Format the labels and axes for the plot.
    axs.set_xlabel("Number of Scenes")
    axs.set_ylabel("Average Scene Length")
    axs.set_title("Number of Scenes vs Average Scene Length")
    axs.set_xticks(range(0,40,4))
    axs.set_yticks(range(0,22,2))
    axs.legend()

if __name__ == "__main__":
    content_type_plots()
    video_style_plot()
    video_scenes_plot()
    
    # Display the subplots
    plt.show()