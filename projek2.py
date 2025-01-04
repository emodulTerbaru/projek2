import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

cred_dict = st.secrets["firebase_key"]
# Inisialisasi Firebase
st.write(cred_dict)
st.write(type(cred_dict))
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)
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
