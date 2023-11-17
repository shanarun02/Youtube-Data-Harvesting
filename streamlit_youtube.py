import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Arun@5851',
    database='youtube'
)

mycursor = mydb.cursor()

# Streamlit app
def streamlit_app():
    st.title('MySQL Data Display with Streamlit')

    if st.checkbox('What are the names of all the videos and their corresponding channels?'):
        sql = 'select title,channel_name from video_details'
        mycursor.execute(sql)
        first_question= mycursor.fetchall()
        column_names=['Video Name','Channel Name']
        first_question_with_lists=[ list(row)for row in first_question]
        st.table([column_names] + first_question_with_lists)
    
    if st.checkbox('Which channels have the most number of videos, and how many videos do they have?'):
        sql = 'SELECT channel_name, Total_videos AS max_videos FROM channel_details WHERE Total_videos = (SELECT MAX(Total_videos) FROM channel_details);'
        mycursor.execute(sql)
        second_question= mycursor.fetchone()
        st.write(f"Channel with the most videos: {second_question[0]}, Video count: {second_question[1]}")
        
    if st.checkbox('What are the top 10 most viewed videos and their respective channels ?'):
        sql = 'SELECT view_count,title,channel_name FROM video_details ORDER BY view_count DESC LIMIT 10 '
        mycursor.execute(sql)
        third_question = mycursor.fetchall()
        third_question_with_lists = [list(row) for row in third_question]
        column_names = ['View Count','Video Name','Channel Name']
        st.table([column_names] +third_question_with_lists)
    
    if st.checkbox('How many comments were made on each video, and what are their corresponding video names?'):
        sql='select comment_count, title from video_details'
        mycursor.execute(sql)
        forth_question=mycursor.fetchall()
        column_names=['Comment Count','Video Name']
        forth_question_with_list=[list (row)for row in forth_question]
        st.table([column_names]+ forth_question_with_list)
    
    
    if st.checkbox ('Which videos have the highest number of likes, and what are their corresponding channel names?'):
        sql='SELECT like_count,title,channel_name FROM video_details ORDER BY like_count DESC LIMIT 10'
        mycursor.execute(sql)
        fifth_question=mycursor.fetchall()
        column_names=['likes count','Video Name','channel_name']
        fifth_question_with_lists=[list (row) for row in fifth_question]
        st.table([column_names]+ fifth_question_with_lists)

    if st.checkbox ('What is the total number of likes  for each video, and what are their corresponding video names?'):
        sql='SELECT like_count,title FROM video_details '
        mycursor.execute(sql)
        sixth_question=mycursor.fetchall()
        column_names=["likes","Video Name"]
        sixth_question_with_lists=[list(row) for row in sixth_question]
        st.table([column_names] + sixth_question_with_lists)
        
    if st.checkbox ('What is the total number of views for each channel, and what are their corresponding channel names?'):
        sql='SELECT channel_name,views_count from channel_details '
        mycursor.execute(sql)
        seventh_question=mycursor.fetchall()
        column_names=['Channel Name','View Count']
        seventh_question_with_list=[list(row) for row in seventh_question]
        st.table([column_names]+seventh_question_with_list)
        
    if st.checkbox ('What are the names of all the channels that have published videos in the year 2022?'):
        sql='SELECT channel_name,published_at,title FROM video_details WHERE YEAR(published_at) = 2022;'
        mycursor.execute(sql)
        eigth_question=mycursor.fetchall()
        column_names = ['Channel_Name','Publishd Date','Title']
        eigth_question_with_lists = [list(row) for row in eigth_question]
        st.table([column_names ]+ eigth_question_with_lists)
        
    if st.checkbox ('What is the average duration of all videos in each channel, and what are their corresponding channel names?'):
        sql='SELECT channel_name,duration from video_details '
        mycursor.execute(sql)
        ninth_question=mycursor.fetchall()
        st.table(ninth_question)
        
    if st.checkbox ('Which videos have the highest number of comments, and what are their corresponding channel names?'):
        sql='SELECT comment_count,title,channel_name FROM video_details ORDER BY comment_count DESC LIMIT 10 '
        mycursor.execute(sql)
        tenth_question=mycursor.fetchall()
        column_names = ['Comment_count','Video Name','Channel_Name']
        tenth_question_with_lists=[list(row) for row in tenth_question]
        st.table([column_names] + tenth_question_with_lists)


            
streamlit_app()


