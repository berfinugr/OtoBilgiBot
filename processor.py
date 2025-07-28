import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_article(title, url):
    prompt = f"""Aşağıdaki haber başlığını ve bağlantısını kullanarak kısa bir haber özeti oluştur.
    
    Başlık: {title}
    Kaynak: {url}

    Lütfen açık ve anlaşılır bir Türkçe ile 3-4 cümlelik bir özet yaz."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # GPT-4 varsa bunu da kullanabilirsin
            messages=[
                {"role": "system", "content": "Sen profesyonel bir haber yazarı yardımcısısın."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250,
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary

    except Exception as e:
        print(f"LLM hatası: {e}")
        return "Özetlenemedi."
