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
        results = mycursor.fetchall()
        st.table(results)
    
    if st.checkbox('Which channels have the most number of videos, and how many videos do they have?'):
        sql = 'SELECT channel_name, Total_videos AS max_videos FROM channel_details WHERE Total_videos = (SELECT MAX(Total_videos) FROM channel_details);'
        mycursor.execute(sql)
        result = mycursor.fetchone()
        st.write(f"Channel with the most videos: {result[0]}, Video count: {result[1]}")
        
    if st.checkbox('What are the top 10 most viewed videos and their respective channels ?'):
        sql = 'SELECT view_count,channel_name FROM video_details ORDER BY view_count DESC LIMIT 10 '
        mycursor.execute(sql)
        third_question = mycursor.fetchall()
        third_question_with_lists = [list(row) for row in third_question]
        column_names = ['View Count', 'Channel Name']
        st.table([column_names] +third_question_with_lists)
    
    if st.checkbox('How many comments were made on each video, and what are their corresponding video names?'):
        sql='select comment_count, title from video_details'
        mycursor.execute(sql)
        forth_question=mycursor.fetchall()
        st.table( forth_question)
    
    
    if st.checkbox ('Which videos have the highest number of likes, and what are their corresponding channel names?'):
        sql='SELECT like_count,channel_name FROM video_details ORDER BY like_count DESC LIMIT 10'
        mycursor.execute(sql)
        fifth_question=mycursor.fetchall()
        st.table(fifth_question)

    if st.checkbox ('What is the total number of likes  for each video, and what are their corresponding video names?'):
        sql='SELECT like_count,title FROM video_details '
        mycursor.execute(sql)
        sixth_question=mycursor.fetchall()
        st.table(sixth_question)
        
    if st.checkbox ('What is the total number of views for each channel, and what are their corresponding channel names?'):
        sql='SELECT channel_name,views_count from channel_details '
        mycursor.execute(sql)
        seventh_question=mycursor.fetchall()
        st.table(seventh_question)
        
    if st.checkbox ('What are the names of all the channels that have published videos in the year 2022?'):
        sql='SELECT channel_name,views_count from channel_details '
        mycursor.execute(sql)
        eigth_question=mycursor.fetchall()
        st.table(eigth_question)
        
    if st.checkbox ('What is the average duration of all videos in each channel, and what are their corresponding channel names?'):
        sql='SELECT channel_name,views_count from channel_details '
        mycursor.execute(sql)
        ninth_question=mycursor.fetchall()
        st.table(ninth_question)
        
    if st.checkbox ('Which videos have the highest number of comments, and what are their corresponding channel names?'):
        sql='SELECT comment_count,channel_name FROM video_details ORDER BY comment_count DESC LIMIT 10 '
        mycursor.execute(sql)
        ninth_question=mycursor.fetchall()
        st.table(ninth_question)


    

        
        
        
        
        
        
streamlit_app()


