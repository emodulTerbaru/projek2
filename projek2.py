import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

firebase_key  = st.secrets["firebase_key"]
project_id = firebase_key.project_id
private_key = firebase_key.private_key

# Mencetak nilai untuk memastikan data dapat diakses
st.write(f"Project ID: {project_id}")
st.write(f"Private Key: {private_key}")
coba = dict(firebase_key)
st.write(coba)
# Membuat credential Firebase dari dictionary yang diperoleh
cred_json = json.dumps(coba)
cred = credentials.Certificate(json.loads(cred_json))
firebase_admin.initialize_app(cred)

st.write("Firebase initialized successfully!")

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
