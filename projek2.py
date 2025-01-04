import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

with open("belajar1\\percobaan-pertama-ae4ff-firebase-adminsdk-rgoyc-bb4b0284ac.json",'r') as json_file:
    coba = json.load(json_file)
# Inisialisasi Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(coba)
    firebase_admin.initialize_app(cred)

# Koneksi ke Firestore
db = firestore.client()

# Membuat koleksi dan menambahkan data
def add_data(name, age):
    doc_ref = db.collection("users").document(name)
    doc_ref.set({"name": name, "age": age})

# Menampilkan data dari Firestore
def get_data():
    docs = db.collection("users").stream()
    data = [{"name": doc.id, "age": doc.to_dict()["age"]} for doc in docs]
    return data

# Streamlit UI
st.title("Firebase Firestore with Streamlit")

name = st.text_input("Nama:")
age = st.number_input("Umur:", min_value=0, step=1)

if st.button("Tambah Data"):
    add_data(name, age)
    st.success("Data berhasil ditambahkan!")

if st.button("Lihat Data"):
    data = get_data()
    st.write(data)
