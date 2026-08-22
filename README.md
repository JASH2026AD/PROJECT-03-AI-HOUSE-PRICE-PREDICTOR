# 🎓 CampusConnec

**CampusConnect** is a full-stack campus platform designed to bring essential student services into one unified digital ecosystem.

Students can exchange skills, buy and sell campus items, report lost or found belongings, communicate with other students, build reputation, and use AI-powered review analysis — all from a single platform.

---

## 🚀 Features

### 🤝 Skill Exchange

Students can share their knowledge and learn from other students.

* Offer skills you can teach
* Find students with skills you want to learn
* Connect with other students
* Track skill-exchange sessions
* Build reputation through successful sessions

Examples:

`Programming • Languages • Design • Video Editing • Academic Subjects`

---

### 🛒 Campus Marketplace

A student-focused marketplace for buying and selling useful campus items.

Students can list items such as:

* 📚 Textbooks
* 🧮 Calculators
* 💻 Electronics
* 🪑 Dorm supplies
* 🎒 College accessories

Users can browse listings and communicate with sellers directly through the platform.

---

### 🔍 Lost & Found Portal

CampusConnect provides a centralized system for reporting lost and found belongings.

Students can:

* Report lost items
* Post found items
* Browse available reports
* Claim belongings
* Verify ownership using verification questions

Successful returns can also improve the student's reputation score.

---

### 🤖 AI Review Analyzer

CampusConnect integrates **Google Gemini AI** to analyze user reviews.

The AI system can:

* Detect suspicious or spam reviews
* Analyze sentiment
* Summarize positive and negative feedback
* Generate trust insights

If the Gemini API is unavailable, the application can fall back to local rule-based analysis.

---

### 💬 Student Communication

CampusConnect allows students to communicate directly inside the platform.

Features include:

* Student-to-student messaging
* Message history
* Notifications
* User interaction across marketplace and skill exchange features

---

### ⭐ Student Reputation System

Students build reputation through positive activity on the platform.

Examples include:

* Completing teaching sessions
* Successfully returning lost items
* Marketplace activity
* Community participation

This helps create a more trustworthy campus community.

---

### 🛡️ Admin Dashboard

Administrators can monitor and moderate activity across CampusConnect.

Admin capabilities include:

* User management
* Content moderation
* Marketplace monitoring
* Lost & Found monitoring
* Platform activity management

---

## 🔐 Authentication & Verification

CampusConnect includes authentication features designed for a university environment.

* Student registration
* Login authentication
* JWT-based authentication
* College email verification
* Role-based access
* Student and Admin accounts

---

## 🛠️ Tech Stack

### Frontend

* ⚛️ React.js
* ⚡ Vite
* 🎨 Tailwind CSS
* 🧭 React Router
* 🔗 Axios
* 🎯 Lucide Icons

### Backend

* 🟢 Node.js
* 🚂 Express.js
* 📁 Multer
* 🔐 JWT Authentication

### Database

* 🐬 MySQL
* 🔷 Prisma ORM

### Artificial Intelligence

* ✨ Google Gemini API
* `@google/genai`

---

## 📂 Project Structure

```text
PROJECT-01-CAMPUS-CONNECT/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── prisma/
│   ├── routes/
│   ├── controllers/
│   ├── middleware/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚙️ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/JASH2026AD/PROJECT-01-CAMPUS-CONNECT.git
```

Move into the project:

```bash
cd PROJECT-01-CAMPUS-CONNECT
```

---

## 2️⃣ Configure MySQL

Make sure **MySQL Server** is installed and running.

Navigate to:

```text
backend/
```

Create a `.env` file.

Example:

```env
DATABASE_URL="mysql://root:password@localhost:3306/campusconnect"

JWT_SECRET="your_secure_jwt_secret"

GEMINI_API_KEY="your_gemini_api_key"
```

> ⚠️ Never commit your real `.env` file, passwords, JWT secrets, or API keys to GitHub.

---

## 3️⃣ Backend Setup

Open a terminal:

```bash
cd backend
```

Install dependencies:

```bash
npm install
```

Run Prisma migration:

```bash
npx prisma migrate dev --name init
```

Generate Prisma Client:

```bash
npx prisma generate
```

Seed sample data:

```bash
npx prisma db seed
```

Start the backend:

```bash
npm run dev
```

Backend server:

```text
http://localhost:5000
```

---

## 4️⃣ Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🧪 Demo Accounts

After running the database seed, the following development accounts can be used.

### 👨‍🎓 Student

```text
Email: alice@college.edu
Password: password123
```

### 👨‍🎓 Student

```text
Email: bob@college.edu
Password: password123
```

### 🛡️ Administrator

```text
Email: admin@college.edu
Password: password123
```

> These accounts are intended only for local development and testing.

---

# 🔄 Application Flow

```text
Student
   │
   ▼
Register / Login
   │
   ▼
College Email Verification
   │
   ▼
CampusConnect Dashboard
   │
   ├──► Skill Exchange
   │
   ├──► Campus Marketplace
   │
   ├──► Lost & Found
   │
   ├──► AI Reviews
   │
   ├──► Messages
   │
   └──► Notifications
```

---

# 🌟 Core Idea

College students often need different services throughout their campus life:

* Finding someone who can teach a skill
* Selling unused textbooks
* Buying second-hand college items
* Finding lost belongings
* Communicating with other students
* Identifying trustworthy users

Instead of using multiple disconnected platforms, **CampusConnect combines these services into one campus-focused ecosystem.**

---

# 🔮 Future Improvements

Possible future enhancements include:

* 📱 Mobile application
* 🔔 Real-time push notifications
* 💬 WebSocket-based real-time chat
* 🗺️ Campus map integration
* 📍 Location-based Lost & Found
* 🤖 AI-powered recommendations
* 📊 Advanced admin analytics
* 🎓 Multi-college support
* 🔐 OTP/email verification service
* ☁️ Cloud deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/your-feature
```

5. Create a Pull Request

---

# ⭐ Support

If you find **CampusConnect** useful or interesting, consider giving the repository a ⭐.

It helps support the project and its future development.

---

## 👨‍💻 Author

**Jaswanth Chennu**

GitHub: `@JASH2026AD`

---

## 📄 License

This project is intended for educational and development purposes.

---

<div align="center">

### 🎓 CampusConnect

**Connect • Learn • Exchange • Discover**

Built for a smarter and more connected campus. 🚀

</div>
