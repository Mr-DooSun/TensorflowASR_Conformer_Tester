from STT_Test import STT
import streamlit as st

if 'stt' not in st.session_state:
    st.session_state.stt = STT()

st.title('Speech-to-Text System')
# st.subheader('Speech-to-Text System')

audio_files = st.file_uploader('Choose a Audio file', type=['flac','mp3','wav'])

if audio_files is not None :
    st.write('file : ',audio_files)
    st.success('Ready')
else :
    st.warning('Select Audio File')

stt_button = st.button('STT')

if stt_button:
    if audio_files is not None :
        with open('temp/'+audio_files.name,'wb') as f: 
            f.write(audio_files.getbuffer()) 

        result = st.session_state.stt.Test('temp/'+audio_files.name)
        st.success(result)
    else :
        st.warning('You must Choose Audio data')
    
