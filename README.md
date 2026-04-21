# 🚀 AI Stylist — Personalized Outfit Recommendation System

> AI-powered fashion recommendations using **Amazon Bedrock (Nova Micro + Nova Canvas)**, built on a fully serverless AWS architecture.

---

## 🧠 Overview

**AI Stylist** is a full-stack, serverless application that generates personalized outfit recommendations and AI-generated images based on user preferences such as occasion, season, style, and colors.

The system integrates generative AI with real-world cloud infrastructure, demonstrating how modern AI applications are built and deployed at scale.

---

## ⚡ Key Features

- 🎯 Personalized outfit recommendations based on structured inputs
- 🧠 AI-generated outfit descriptions using **Amazon Nova Micro**
- 🎨 Image generation using **Amazon Nova Canvas**
- ☁️ Fully serverless backend (no servers to manage)
- 🌐 Live frontend hosted on **Amazon S3**
- 🔐 Secure IAM-based architecture
- ⚡ Real-time API processing via **API Gateway + Lambda**

---

## 🏗️ Architecture

![AI Stylist Architecture](images/architecture.png)

### 🔄 Workflow

1. User inputs preferences (occasion, season, style, etc.)
2. Request is sent to **API Gateway**
3. API triggers **AWS Lambda**
4. Lambda calls:
   - **Nova Micro** → text generation
   - **Nova Canvas** → image generation
5. Images are stored in **Amazon S3**
6. Results are returned to frontend via API response

---

## 🛠️ Tech Stack

| Layer        | Technology                                   |
| ------------ | -------------------------------------------- |
| Frontend     | HTML / CSS (S3 Static Hosting)               |
| Backend      | AWS Lambda                                   |
| API Layer    | API Gateway                                  |
| AI Models    | Amazon Bedrock (Nova Micro, Nova Canvas)     |
| Storage      | Amazon S3                                    |
| Dev Env      | SageMaker Notebook                           |
| Security     | IAM Roles & Policies                         |

---

## 📸 Demo

### 🖥️ Frontend UI

![AI Stylist Frontend](images/AI_stylist_website.png)

### 🎨 Generated Outfits

![AI-Generated Outfits](images/AI_stylist_outfit.png)

---

## 📦 Sample API Input

```json
{
  "occasion": "Business Casual",
  "season": "Summer",
  "styles": ["Minimalist", "Classic"],
  "colors": ["Earth Tones"],
  "gender": "neutral",
  "custom_prompt": "office friendly and comfortable"
}
```

---

## 🧩 Backend Logic (Simplified)

- [x] Parse user input
- [x] Build structured prompt
- [x] Call Bedrock models
- [x] Store generated images in S3
- [x] Return JSON response with descriptions + image URLs

![Lambda Function Test Event](images/Lambda_function.png)

---

## ⚠️ Challenges & What I Solved

This project involved **real-world cloud debugging**, not just implementation:

- ❌ `AccessDeniedException` (IAM misconfigurations)
- ❌ Bedrock model access issues
- ❌ API Gateway integration errors
- ❌ Lambda permission errors (`InvokeModel`, `AddPermission`)

### ✅ Solution

- Designed **least-privilege IAM roles**
- Configured **Bedrock access** correctly
- Fixed **API Gateway → Lambda permissions**
- Implemented **secure service-to-service communication**

#### IAM Policy Configuration

![IAM Policy — Bedrock + S3 Access](images/policy_editor.png)

![IAM Policy — CloudWatch Logs Access](images/policy_editor_1.png)

---

## 🧠 Key Learnings

- How to build production-style **serverless systems**
- Integrating **AI models** into real applications
- Debugging **AWS IAM and permission systems**
- Designing **scalable cloud architectures**
- Handling **structured prompts + AI responses**

---

## 🚀 Deployment

- **Frontend** deployed via S3 Static Website Hosting
- **Backend** deployed using AWS Lambda
- **API** exposed via API Gateway
- **Models** accessed through Amazon Bedrock

### 📓 Development Environment

The entire backend was provisioned and tested from a SageMaker Jupyter Notebook:

![SageMaker Notebook Setup](images/Jupyter_notebook.png)

---

## 👨‍💻 Author

**Jaswant Singh**

- 🎓 Aspiring AI Engineer / AI Automation Specialist
- 💡 Passionate about building real-world AI systems
- 🌱 Open to opportunities in AI, Cloud, and Data

---

## 🔥 Why This Project Matters

This is **not just a demo** — it demonstrates:

- ✅ Real AI + Cloud integration
- ✅ Full end-to-end system design
- ✅ Ability to debug production-level issues
- ✅ Understanding of modern AI architecture

---

## ⭐ If you like this project

Give it a **star ⭐** and feel free to connect!
