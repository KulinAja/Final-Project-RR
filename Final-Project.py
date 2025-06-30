import streamlit as st
from typing import List
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
try:
    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
except Exception:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    st.sidebar.error("API Key OpenRouter tidak ditemukan. Tambahkan di st.secrets atau .env!")

if OPENROUTER_API_KEY:
    OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

st.set_page_config(page_title="Personalized Fitness & Nutrition App", page_icon="💪", layout="centered")

st.title("💪 Personalized Fitness & Nutrition App")
st.markdown("Selamat datang! Silakan isi data berikut untuk mendapatkan rekomendasi olahraga dan nutrisi yang sesuai dengan profil Anda.")

# --- Sidebar Info ---
st.sidebar.header("ℹ️ Info")
st.sidebar.markdown("Aplikasi ini membantu Anda mendapatkan rekomendasi olahraga dan nutrisi berdasarkan data pribadi dan kebiasaan Anda.")

# --- Data Sederhana ---
st.header("1️⃣ Data Sederhana")
gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], index=0)
weight = st.number_input("Berat Badan (kg)", min_value=30, max_value=200, value=60)
height = st.number_input("Tinggi Badan (cm)", min_value=120, max_value=220, value=170)
age = st.number_input("Umur (tahun)", min_value=10, max_value=100, value=25)

# --- Data Advanced ---
st.header("2️⃣ Data Advanced")
sport_type = st.selectbox("Jenis Olahraga yang Dilakukan", ["Home Exercise", "Running", "Lifting Weights"])
frequency = st.select_slider(
    "Seberapa Sering Berolahraga?",
    options=["Sangat jarang", "Jarang", "Kadang-kadang", "Rutin", "Sangat rutin"],
    value="Kadang-kadang"
)
duration = st.radio(
    "Panjang Durasi Olahraga",
    ["≤ 30 menit", "30 menit", "45 menit", "1 jam", "≥ 1 jam"],
    index=0
)
allergy = st.multiselect(
    "Alergi pada Makanan",
    ["Tidak ada", "Kacang", "Susu", "Lainnya"],
)
other_allergy = ""
if "Lainnya" in allergy:
    other_allergy = st.text_input("Sebutkan alergi lainnya:")

# --- Tambahan ---
st.header("3️⃣ Data Tambahan")
goal = st.selectbox(
    "Apa tujuan utama Anda berolahraga?",
    ["Menurunkan berat badan", "Menambah massa otot", "Menjaga kesehatan", "Lainnya"]
)
food_pref = st.radio("Preferensi Makanan", ["Omnivore", "Vegetarian", "Vegan"], index=0)
disease = st.multiselect(
    "Riwayat Penyakit (opsional)",
    ["Tidak ada", "Diabetes", "Hipertensi", "Jantung", "Lainnya"]
)
email = st.text_input("Email (opsional, untuk kirim hasil rekomendasi)")

# --- Submit Button ---
if st.button("Dapatkan Rekomendasi 🚀"):
    st.subheader("📋 Ringkasan Data Anda")
    st.markdown(f"**Jenis Kelamin:** {gender}")
    st.markdown(f"**Berat/Tinggi Badan:** {weight} kg / {height} cm")
    st.markdown(f"**Umur:** {age} tahun")
    st.markdown(f"**Jenis Olahraga:** {sport_type}")
    st.markdown(f"**Frekuensi Olahraga:** {frequency}")
    st.markdown(f"**Durasi Olahraga:** {duration}")
    st.markdown(f"**Alergi:** {', '.join(allergy) if allergy else 'Tidak ada'}" + (f", {other_allergy}" if other_allergy else ""))
    st.markdown(f"**Tujuan:** {goal}")
    st.markdown(f"**Preferensi Makanan:** {food_pref}")
    st.markdown(f"**Riwayat Penyakit:** {', '.join(disease) if disease else 'Tidak ada'}")
    if email:
        st.markdown(f"**Email:** {email}")

    # --- Rekomendasi Sederhana (Rule-based) ---
    st.subheader("🤖 Rekomendasi untuk Anda")
    # BMI Calculation
    bmi = weight / ((height/100)**2)
    if bmi < 18.5:
        bmi_status = "Berat badan kurang"
    elif bmi < 25:
        bmi_status = "Berat badan normal"
    elif bmi < 30:
        bmi_status = "Berat badan berlebih"
    else:
        bmi_status = "Obesitas"
    st.markdown(f"**Status BMI:** {bmi:.1f} ({bmi_status})")

    # Simple fitness recommendation
    if goal == "Menurunkan berat badan":
        rec = "Fokus pada olahraga kardio seperti running dan atur pola makan rendah kalori."
    elif goal == "Menambah massa otot":
        rec = "Perbanyak latihan beban (lifting weights) dan konsumsi protein cukup."
    elif goal == "Menjaga kesehatan":
        rec = "Lakukan olahraga rutin minimal 3x seminggu dan konsumsi makanan seimbang."
    else:
        rec = "Sesuaikan olahraga dan nutrisi dengan kebutuhan pribadi Anda."
    st.info(rec)

    # Allergy & food preference
    if ("Kacang" in allergy or "Susu" in allergy or other_allergy) and "Tidak ada" not in allergy:
        st.warning("Perhatikan asupan makanan yang mengandung alergen Anda!")
    if food_pref != "Omnivore":
        st.info(f"Pastikan kebutuhan nutrisi Anda tercukupi sebagai seorang {food_pref}.")

    # Disease warning
    if disease and "Tidak ada" not in disease:
        st.warning("Konsultasikan dengan dokter sebelum memulai program olahraga/nutrisi baru.")

    # --- AI Recommendation (OpenRouter) ---
    if OPENROUTER_API_KEY:
        user_summary = f"""
        Jenis Kelamin: {gender}
        Berat Badan: {weight} kg
        Tinggi Badan: {height} cm
        Umur: {age} tahun
        Jenis Olahraga: {sport_type}
        Frekuensi Olahraga: {frequency}
        Durasi Olahraga: {duration}
        Alergi: {', '.join(allergy) if allergy else 'Tidak ada'}{', ' + other_allergy if other_allergy else ''}
        Tujuan: {goal}
        Preferensi Makanan: {food_pref}
        Riwayat Penyakit: {', '.join(disease) if disease else 'Tidak ada'}
        """
        prompt = f"Berdasarkan data berikut, berikan rekomendasi olahraga dan nutrisi yang personal, singkat, dan mudah dipahami:\n{user_summary}"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "moonshotai/kimi-dev-72b:free",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.7
        }
        try:
            response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            ai_recommendation = data["choices"][0]["message"]["content"].strip()
            st.success(f"Rekomendasi AI:\n{ai_recommendation}")
        except Exception as e:
            try:
                err_msg = response.json().get('error', {}).get('message', str(e))
            except Exception:
                err_msg = str(e)
            st.error(f"Gagal mendapatkan rekomendasi AI: {err_msg}")
    else:
        st.info("AI recommendation tidak aktif. Tambahkan API key OpenRouter di .env untuk mengaktifkan.")

    st.success("Terima kasih sudah menggunakan aplikasi ini! 💚")
else:
    st.markdown(":point_up: Silakan lengkapi data di atas dan klik tombol untuk mendapatkan rekomendasi.")
