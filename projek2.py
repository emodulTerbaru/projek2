import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

cred_dict = {
  "type": "service_account",
  "project_id": "percobaan-pertama-ae4ff",
  "private_key_id": "bb4b0284ac824c953522c6d4daabc20325d5e8c5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQD1OHyPKSqEKNZG\nAUIOX6iWPd01KapV1kT/kr2MGdxM1EOIOIMJuLFTv1kEra1GVvr3XTyHfRoE9iNL\nRk9a5euy5o8KQj4v+0uUXu0RmaUtftIg+kZPCHYup2sJiysqAv4pUfOWwCzpqJII\nToBwyUGJEeL5dUg36qsUqHiVcwCXuYGsQFLvyNiNh5yNr8afe9Ah0EOi/ppyjbYZ\nZ4nYz96OWketLa1JMMOfmY7fJ5t9yMkac2tP92mx1ZAvs7cCGrSvz2CaOgVCarVl\nThDwAHIPx8Ii0Ad3EJxr0tldpB04nrVwiD+bEz+YYFL6rQKOpwG9hSav2YzbRx4z\n11viSxdFAgMBAAECggEAB4e7B3hnplRMtCygtylH14lBzDqh0O36A3EhofY/Vhqk\nkj/OAlPqGhzDoomkywarwUHbNHvqeyGF1u9rS2rJEJ7U4KdFGpsYaI97rzEtKdb9\no+ablxy26FraxhnAcxNRc7phBQ2Us34qMdgbSJtdiFSEyE1KMPFjXIiJ32j/KSmJ\nRvjijyLMP3Ihq+M9lWVGxt/TzJ4Lx2EXDLSekd2GS11kpTbFu6BMyfipKtlGJKKH\nfU4NoqrRayJteLAHQ9mbGciY+vUHO+QecoF30yC45Zkqz8c8CpQ8pSC5FWTRC/Bd\n0oW3HUcqFxyIcQ2ETnTH8KJ/68CQ8PQTI6u0+o9ZxwKBgQD7vGxTGpj8sO1lohIr\nsY8e3B/kIaSoGXXJEvNIiJcK+kTbnsAS0nXm69h3BhMdpr8P3auA9VWHpSfJvZSS\nXolpUXGhFAXjgNShd6kPDzA9tXytm3AtiOAG4unqg3h85DiQvcipnus01euJOwiv\nic+7uFJ8TOvdTl7QCzYBxLBA0wKBgQD5X8+75xPTLkiItfJDhbKqQbt7PjTxd5Nj\nKTkiJmxS/QEBIIBvvF7XEhVJAvAcqr+sqkyIwoBKPIcHHWc19Eun7J6nGAsFNX0a\nRc7xZJd3y06Gs8NZOQO3QuZ9Pksd+cbJMDs2M1PxytYHjy6dLs6zTNJtjOhh02CA\nkHL3f3J4hwKBgCo3xHb/e+7NAVNNJfz770O+qP6KgeHLO0y4h+J/Pc2SgV/PtOiz\nMSDEJu53L1eGsn5Hr86V1n1EPnL//124yxTFmufnwsEPxxk5RzoGUxHWUQ2QhvSs\nAt5EyfQRjnBrmez0VyXTSCD5S2Ida2x9EUCrPfIouFnKHe6IIsuTH/gPAoGAXci5\nsFoUK5zBbKC4rsouSjeUUaIweQtWY7mSIhS/MmqyIQFfLCZ0qH/Ff4LaWH2ivkYB\nqIE1jDW9NmDJexIYDdxAQmkZY+kc1m+gh0okaMoOCzy53+lAS4CefEWcLHbOWsWH\nzzd4f3ugCJHBnx2GYQooLUkL8BZ1uYQZqJjGrSsCgYA+6FpSQ1BikvuIPTOgC6E6\nkQ4HcnBWq1R6yz+/bbukDn2f87aGZ7GhT3uWf4RyljnMMFLEp2R+/OFd/IJqxElL\nyXlHQoQYkHYQw8ZhHk1Hlv3uvUj5cLhkaIXvl3esbxB5SUlSZrqgF3/WzOlTcfDA\nijG7wK6YNufvknC1cumZ5A==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-rgoyc@percobaan-pertama-ae4ff.iam.gserviceaccount.com",
  "client_id": "107723963896798615423",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rgoyc%40percobaan-pertama-ae4ff.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Inisialisasi Firebase
st.write(cred_dict)
st.write(type(cred_dict))
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
