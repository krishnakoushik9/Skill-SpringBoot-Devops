# Medha AI - Feature List

## Home Screen

### Statistics & Dashboard
- **Stats Hero Card** - Displays learning statistics with animated progress metrics
- **Usage Time Tracking** - Tracks and displays daily app usage time for study sessions
- **Progress Summary** - Shows quiz scores, streak count, and overall progress

### Quick Actions
- **Quick Action Chips** - Fast navigation buttons for frequently used features
- **Download Status** - Shows AI model download progress and status
- **Notification Bell** - Shows unread notification count with badge

### Content Access
- **PDF File Viewer** - Opens and views PDF study materials
- **GitHub Integration** - Links to project repository and resources
- **Dev Popup** - Developer information and app details dialog

### System Features
- **Network Status Indicator** - Shows online/offline connection status
- **Smart Sync Widget** - Displays cloud synchronization status
- **Feature Flags Polling** - Checks for remotely enabled/disabled features
- **Haptic Feedback** - Provides tactile feedback on interactions

---

## Progress Screen

### Analytics
- **Weekly Activity Chart** - Line chart showing prompts per day over the week
- **Subject Mastery Bars** - Horizontal progress bars for each subject category
- **Prompt History List** - Scrollable list of all AI prompts with timestamps

### Study Insights
- **Subject Tagging** - Categorize prompts by subject (Math, Science, History, etc.)
- **Time Formatting** - Human-readable timestamps for prompt history

### Actions
- **Share Progress** - Share learning progress with others
- **Progress Report Generator** - AI-generates detailed PDF progress reports
- **Focus Mode Button** - Quick access to the Focus Timer screen

---

## Profile Screen

### Personal Information
- **Profile Picture** - Upload and display custom profile image
- **Name & Age Fields** - Editable personal details with validation
- **Educational Level** - Track current grade/class level

### Goals & Ambitions
- **Ambition Statement** - Save learning goals and aspirations
- **Target Exam** - Track specific exam preparation targets

### Location & Map
- **Location Display** - Shows current location with optional GPS
- **Interactive Map** - Flutter Map integration showing user location

### App Settings
- **Theme Toggle** - Light/Dark mode switching
- **Share App APK** - Share the app installer with friends
- **Clear Model Cache** - Delete downloaded AI models to free space
- **Delete Individual Models** - Remove specific AI models (Gemma/Qwen)
- **Cloud Sync** - Sync profile data to cloud storage
- **Privacy Disclosure** - Access privacy policy and data disclosure

---

## Tasks Screen

### Task Management
- **Add Task Dialog** - Create new study tasks with title and notes
- **Task Toggle** - Mark tasks as complete/incomplete with animation
- **Task Persistence** - Saves tasks locally with SharedPreferences

### AI-Powered Features
- **PDF Generator** - AI generates detailed study notes as PDF from tasks
- **Mind Map Generator** - Creates visual mind maps from task topics
- **Offline Mind Map** - Uses local LLM for offline mind map generation

### Collaboration
- **Cloud Sync Queue** - Queues tasks for background cloud synchronization
- **Learn With Me** - Opens interactive AI teaching session on task topic

---

## Chat Screen (AI Assistant)

### Conversation
- **AI Chat Interface** - Chat with locally running LLM (Gemma/Qwen)
- **Streaming Responses** - Real-time text generation with typing effect
- **Message History** - Scrollable conversation history

### Input Methods
- **Voice Input** - Speech-to-text for hands-free questions
- **Text Input** - Traditional keyboard input with send button

### AI Model Management
- **Model Status Banner** - Shows current model status (loading/ready)
- **Model Selection** - Choose between Gemma and Qwen models
- **Inference Metrics** - Displays tokens/second and generation time

### Visual Effects
- **Shader Background** - Animated gradient shader effect
- **Text Generation Effect** - Typewriter-style text reveal animation

---

## Quiz Screen

### Quiz Generation
- **AI Quiz Generation** - Creates quizzes using AI based on topics
- **RAG-Enhanced Questions** - Uses document retrieval for context-aware quizzes
- **Quiz Caching** - Saves generated quizzes for offline access

### Quiz Experience
- **Question View** - Displays question with multiple choice options
- **Answer Feedback** - Visual feedback for correct/incorrect answers
- **Score Tracking** - Tracks quiz score and updates progress

### AI Progress Indicator
- **Loading Steps Visualization** - Shows detailed model loading progress
- **Generation Stats Card** - Displays inference performance metrics

---

## Flashcards Screen

### Flashcard Generation
- **AI Flashcard Creation** - Generates flashcards on any topic using AI
- **Topic Input** - Enter any subject for flashcard generation

### Flashcard Interaction
- **Flip Animation** - 3D flip animation to reveal answer
- **Card Navigation** - Swipe through multiple flashcards
- **Visual Design** - Gradient cards with icons and styling

### AI Image Generation
- **Topic Illustration** - Generates AI images related to flashcard topic
- **Image Viewer** - Full-screen image viewing experience

---

## Focus Timer Screen

### Pomodoro Timer
- **E-Ink Aesthetic** - Minimalist black/white design with grain texture
- **Analog Clock Display** - Visual clock face showing remaining time
- **Preset Durations** - Quick buttons for 15, 25, 45 minute sessions

### Timer Controls
- **Start/Stop Timer** - Play/pause focus session
- **Reset Timer** - Reset to initial duration
- **Completion Dialog** - Celebration dialog when session completes

### Visual Effects
- **Grain Texture Overlay** - E-ink paper-like grain effect
- **Custom Clock Painter** - Hand-drawn analog clock visualization

---

## Games Screen

### Educational Games
- **Trig Tower Defense** - Learn trigonometry by answering questions to defend
- **Pass The Phone** - Multiplayer quiz game for group study sessions

### Game Cards
- **Fun Game Cards** - Colorful, animated game selection cards
- **Coming Soon Placeholders** - Future game indicators with popup

---

## Trig Tower Defense Game

### Gameplay
- **Trigonometry Questions** - Answer sin, cos, tan questions to attack enemies
- **Wave System** - Progressive difficulty with enemy waves
- **Scoring System** - Points and combo tracking

### Visual Effects
- **Rainbow Explosions** - Colorful particle effects on correct answers
- **Sad Particles** - Visual feedback for wrong answers
- **Sound Effects** - Audio feedback for gameplay events

### Progress
- **High Score Tracking** - Saves best scores locally
- **Cloud Sync** - Syncs game scores to cloud

---

## Pass The Phone Game

### Multiplayer Setup
- **Player Count Selection** - Choose 2-5 players
- **Topic Selection** - Pick quiz subject (Math, Science, General)
- **Player Names** - Enter names for each participant

### Gameplay
- **AI Question Generation** - Gemma generates unique questions offline
- **Pass Phone Phase** - Prompts to hand device to next player
- **Answer Selection** - Multiple choice with feedback animation

### Results
- **Final Scoreboard** - Shows all players ranked by score
- **Restart Option** - Play again with same or new players

---

## Learn With Me Screen

### Interactive Learning
- **AI Mascot Teaching** - Animated mascots explain topics
- **Text-to-Speech** - AI reads explanations aloud
- **Conversation Transcript** - Shows full learning dialogue

### Playback Controls
- **Pause/Resume** - Control lecture playback
- **Skip Forward/Back** - Navigate between conversation steps
- **Replay Current** - Repeat current explanation

### Interactive Q&A
- **Ask Question Overlay** - Pause and ask follow-up questions
- **Voice Question Input** - Speak questions with STT
- **AI Response Generation** - Gemini generates contextual answers

### Visual Features
- **Landscape Mode** - Locks to landscape for immersive learning
- **AI Image Generation** - Creates topic illustrations during lesson

---

## Mind Map Screen

### Visualization
- **Radial Layout** - Mind map arranged in circular pattern
- **Animated Appearance** - Nodes animate into view
- **Zoom/Pan** - Interactive scroll and scale

### Node Types
- **Root Node** - Central topic with glow effect
- **Branch Nodes** - Main subtopics with color coding
- **Leaf Nodes** - Detail items at edges

### Visual Design
- **Curved Connections** - Smooth Bezier curves between nodes
- **Color-Coded Branches** - Each branch has unique color scheme

---

## Netra Screen (AI Vision)

### Image Capture
- **Camera Capture** - Take photo with device camera
- **Gallery Selection** - Pick existing image from gallery
- **Camera Permission** - Handles permission requests gracefully

### Text Recognition
- **Offline OCR** - ML Kit text recognition without internet
- **Extracted Text Display** - Shows recognized text with styling

### AI Integration
- **Send to Gemma** - Send extracted text to local AI for explanation
- **Transition Animation** - Smooth transition to chat screen

---

## Blind Mode Screen

### Accessibility Features
- **High Contrast UI** - Black/white design for visibility
- **Screen Reader Support** - TalkBack/VoiceOver compatible
- **Large Touch Targets** - Oversized buttons for easy tapping

### Audio Learning
- **Text-to-Speech** - Reads all content aloud
- **Voice Topic Input** - Speak to request topics
- **Morse Code Output** - Haptic morse code for lessons

### Learning Modes
- **Learn Panel** - AI-generated lessons with TTS
- **Flashcard Panel** - Audio flashcards with speech

### Interaction Design
- **Tap to Hear Label** - Single tap announces button
- **Long Press to Activate** - Long press executes action

---

## Web Search Screen

### Search Modes
- **WebView Browser** - Full in-app web browser
- **TxtNet Client Mode** - SMS-based web search without data

### Browser Features
- **URL Navigation** - Enter URLs or search queries
- **Loading Indicator** - Shows page load progress

### TxtNet Integration
- **SMS Web Access** - Browse web via SMS gateway
- **Server Mode Toggle** - Switch between client/server modes

---

## Wikipedia Screen

### Content Library
- **Offline Content Packs** - Pre-downloaded Wikipedia articles
- **Pack Categories** - Articles organized by topic (Science, History, etc.)
- **Search Function** - Search through available articles

### Article Reader
- **Markdown Rendering** - Rich text article display
- **Table Support** - Properly formatted tables in articles
- **Back Navigation** - Return to article list

---

## Notifications Screen

### Notification Management
- **Notification List** - Shows all notifications with read status
- **Mark as Read** - Mark individual notifications read
- **Mark All Read** - Clear all unread badges

### Notification Types
- **Download Notifications** - File download with progress
- **Update Announcements** - App update information
- **Learning Reminders** - Study reminder notifications

### File Handling
- **Download Files** - Download attachments from notifications
- **Open Downloaded Files** - Open files with system viewer

---

## Optimization Screen

### Device Analysis
- **Device Metadata** - Collects device info for optimization
- **Memory Check** - Analyzes available memory/storage

### Optimization Process
- **Step Sequence** - Animated optimization steps display
- **Progress Animation** - Visual progress through optimization
- **Haptic Feedback** - Tactile feedback during process

---

## Background Services

### AI Services
- **Local LLM Service** - Runs Gemma/Qwen models on-device
- **Gemini Service** - Cloud AI for complex operations
- **PDF Generator Service** - Creates PDF documents from AI content
- **Progress Report Service** - Generates learning analytics reports

### Sync Services
- **Smart Sync Service** - Intelligent cloud synchronization
- **Network Status Service** - Monitors internet connectivity
- **Notification Service** - Handles push and local notifications

### Content Services
- **Wikipedia Service** - Manages offline Wikipedia content
- **TxtNet Service** - SMS-based web access bridge
- **Prompt History Service** - Tracks all AI interactions
- **Activity Service** - Logs user activity for analytics

### Utilities
- **File Service** - Handles file operations and storage
- **TTS Service** - Text-to-speech wrapper

---

## Widgets & Components

### Navigation
- **Limelight Nav Bar** - Custom animated bottom navigation bar
- **Sync Status Widget** - Shows cloud sync status indicator

### Input
- **AI Input Widget** - Smart text input for AI queries
- **AI Voice Input** - Voice recording with visualization
- **Mic Animation** - Animated microphone indicator

### Display
- **Text Generate Effect** - Typewriter text animation
- **Animated Card** - Cards with animation effects
- **Progress Bar** - Custom styled progress indicator
- **Gemma Chat Chip** - AI model status chip
- **Gravity Easter Egg** - Hidden gravity simulation game


[[Extra]]