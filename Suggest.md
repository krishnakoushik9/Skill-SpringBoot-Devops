[[DSA]]
# **Offline AI Learning Platform – High-Level Overview**

## **Project Title**

**Offline AI Learning Platform (Problem Statement 3)**  
_A solution designed to enable rural students with low-end smartphones and limited internet access to learn efficiently through AI-powered offline tools._

---

## **1. Architecture Overview**

### **Backend & API Layer**

- **GEMINI API:**  
    Used for **AI-based content generation**, including creating practice questions, summaries, key points, and visual concept maps from NCERT materials. It powers the quiz generator and study assistant modules, operating both online and in partially cached offline modes.
    
- **Bhashini API:**  
    Enables **multi-language translation** of English study materials into **regional Indian languages** (Telugu, Hindi, Tamil, etc.). It is triggered when the user selects a non-English language. Acts as a bridge for inclusivity among low-literacy users by pairing with text-to-speech modules.
    
- **Firebase & Google Cloud:**  
    Firebase Authentication manages secure **OAuth-based login** using Google accounts.  
    Firebase Firestore and Cloud Storage handle **user progress**, class-level data, and **synced NCERT content**, ensuring efficient backup and minimal data redundancy.  
    Google Cloud Functions perform background updates and sync checks when the device regains internet.
    
- **Web Scraping Service:**  
    A **custom Python scraping service hosted on GCP** dynamically fetches NCERT and government-approved open educational resources (OER). The scraped content is cleaned, categorized by subject and grade, and stored in structured JSON format for offline usage and periodic updates.
    

---

## **2. Key User Flows**

- **User Login and Authentication:**  
    Users authenticate via Google OAuth. Basic details (name, grade, preferred language) are stored locally in encrypted form and synced to Firebase when connected.
    
- **Grade/Class Selection:**  
    Upon login, users choose their grade (e.g., Class 8, Class 10). The system fetches the corresponding subject folders and topics (Science, Math, etc.) from pre-cached or downloadable NCERT content packages.
    
- **Offline Content Download:**  
    Selected lessons, videos, and quizzes are downloaded in compressed formats.  
    Content is stored in the device’s **secure application directory**, not cache, ensuring persistence even after app restarts. Download prioritization and pause-resume logic optimize low bandwidth usage.
    
- **Learning & Study Tools (Offline):**  
    Students can read lessons, listen to them via **text-to-speech**, and generate **AI summaries and concept maps** offline. The local mini-LLM (Gemini micro-cache) ensures continuity of study even without connectivity.
    
- **Quiz & Practice:**  
    The **auto-quiz generator** uses stored textual lessons to create MCQs, fill-in-the-blanks, and one-word answers. Each quiz session is scored locally, and results are added to progress logs.
    
- **Translation:**  
    Whenever the user switches to a regional language, **Bhashini API** translates visible UI and content dynamically. For fully offline translation, a lightweight **on-device model** caches recent translation pairs for quick reuse.
    
- **Progress Tracking & Sync:**  
    Each learning session (lesson viewed, quiz score, completion time) is recorded locally in a JSON-based progress file.  
    When internet becomes available, the sync engine updates Firebase Cloud, and **parent accounts receive SMS or PDF-based progress summaries** via integrated Twilio or Firebase Functions.
    

---

## **3. Storage & Data Flow**

- **Persistent Local Storage:**  
    All lessons, media, quizzes, and progress data are stored in a **SQLite-based encrypted local database**. File-based materials (PDFs, audio files) are placed in the app’s internal directory, with SHA checksums to ensure data integrity.  
    Sensitive info like login tokens are protected with **AES encryption** and Android’s KeyStore.
    
- **Data Flow Diagram (Conceptual):**
    
    ```
    User → App Interface → Local Storage (SQLite + Files)
         ↘ Sync Engine ↗
           Firebase Cloud (Firestore + GCP Storage)
    AI Engines (Gemini + Bhashini) ↔ App Backend (FastAPI Layer)
    ```
    
    This ensures minimal network usage, and complete offline functionality with delayed sync.
    

---

## **4. Requirements**

- **Offline-first usage:**  
    Core app runs fully offline, including reading, quiz, TTS, and summary tools.
    
- **Lightweight design:**  
    Android APK optimized under **50 MB**, ensuring smooth performance on devices with **8 GB RAM or less**.
    
- **Multi-language support:**  
    English + Indian languages supported through dynamic translation and speech synthesis.
    
- **Voice input/output features:**  
    Voice-based query assistant allows students to **ask study-related questions** and get spoken answers.
    
- **Smart sync:**  
    Intelligent background sync uploads only changed progress and downloads newly updated materials.
    

---

## **5. Known Problems**

- **No iOS Build:**  
    Current version is Android-exclusive due to storage and caching restrictions on iOS.
    
- **Bhashini API Instability:**  
    Intermittent downtime or slow response affects live translation; fallback local translation model mitigates this.
    
- **Web Scraping Reliability:**  
    Content updates depend on the availability and structure of NCERT/OER websites; hence, a **custom GCP microservice** is used to maintain consistency.
    

---

## **6. Security & Privacy**

- The app requests **Storage, Microphone, and Internet permissions** only.
    
- **Storage access**: Required for offline data saving; files stored in protected app directories.
    
- **Microphone access**: Needed for voice queries in low-literacy mode.
    
- **Data encryption**: All user info and performance data encrypted locally using **AES-256** and synced securely via HTTPS.
    
- **Privacy compliance**: Designed under **Digital India Education Policy** and complies with **GDPR-style anonymization** for analytics.
    

---

## **7. Visual Reference**

📊 **High-Level Architecture Flow Diagram (Text Summary):**

```
         ┌────────────────────────────┐
         │         User App           │
         │────────────────────────────│
         │  Login • Lessons • Quiz    │
         │  Summaries • Voice Chat    │
         └──────────────┬─────────────┘
                        │
        ┌───────────────┼────────────────┐
        │ Local Storage (SQLite + Files) │
        │   Offline Access + Sync Cache  │
        └───────────────┬────────────────┘
                        │
        ┌───────────────┴──────────────────┐
        │        Backend (FastAPI)         │
        │  Gemini API   |   Bhashini API   │
        │  Quiz Gen     |   Translation    │
        └───────────────┬──────────────────┘
                        │
        ┌───────────────┴──────────────────┐
        │ Firebase & GCP Storage           │
        │ Auth | Progress | Content Backup │
        └──────────────────────────────────┘
```

---

