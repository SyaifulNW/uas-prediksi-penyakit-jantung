import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))



st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)


from PIL import Image
image = Image.open('banner.jpeg')

st.image(image,
      use_column_width=True)


def predict_age(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    input=np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]).astype(np.float64)
    prediction = model.predict(input)
    return int(prediction)

def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Aplikasi Prediksi Penyakit Jantung Berbasis Website </h2>
    </div>
    
    <br>
    <br>
    """
    st.markdown(html_temp, unsafe_allow_html = True)



    col1, col2 = st.columns(2)


    with col1:
        age = st.text_input("**Umur**")
    with col2:
        sex = st.text_input("**Jenis Kelamin**")
    with col1:
      cp = st.text_input("**Nyeri Dada**")
    with col2:
         trestbps = st.text_input("**Tekanan Darah**")
    with col1:
         chol = st.text_input("**Kolesterol**")
    with col2:
        fbs = st.text_input("**Gula Darah**")
    with col1:
        restecg = st.text_input("**Hasil Elektrokadiografi**")
    with col2:
        thalach = st.text_input("**Detak Jantung**")
    with col1:
     exang = st.text_input("**Induksi Angina**")
    with col2:
        oldpeak = st.text_input("**Depresi ST**")
    with col1:
        slope = st.text_input("**slope**")
    with col2:
        ca = st.text_input("**Nilai CA**")
    with col1:
        thal = st.text_input("**Nilai Thal**")



    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> Anda Tidak Masuk Kedalam Kategori Potensi Penyakit Jantung</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> <b>Anda Berpotensi Masuk Kedalam Kategori Penyakit Jantung</b></h2>
      </div>
    """

    if st.button("Lakukan Prediksi"):
        output = predict_age(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        st.success('Output Is {}'.format(output))

        if output == 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
