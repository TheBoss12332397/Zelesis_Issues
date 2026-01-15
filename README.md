# Zelesis Neo & Utilities — Complete Guide

This repository contains guides, tools, and setup instructions related to **Zelesis Neo**, **Zelesis AI**, and supporting utilities (including Logitech G Hub fixes and Arduino HID usage).

Please read the relevant sections carefully to avoid setup issues, crashes, or delays.

---

## 📚 Table of Contents

- [Logitech G Hub Install Fix](#logitech-g-hub-install-fix)
- [Refund Guide — Zelesis Neo](#refund-guide--zelesis-neo)
- [Zelesis AI — Getting Started](#zelesis-ai--getting-started)
  - [Configs](#configs)
  - [Models (YOLO)](#models-yolo)
  - [Movement Methods](#movement-methods)
  - [Anti-Cheat Notice](#anti-cheat-notice)
- [Arduino Resources](#arduino-resources)
- [Zelesis Installer & First-Time Setup](#zelesis-installer--first-time-setup)

---

## Logitech G Hub Install Fix

This guide explains how to fix the issue where **Logitech G Hub fails to install**, most commonly caused by running PowerShell commands when not instructed to do so.

### Included Tool
A **Python utility** is provided that triggers a UAC prompt and offers **three options**:

1. Remove Logitech G Hub blocks  
2. Restore hosts file from backup  
3. Exit  

- A backup is automatically created when **Option 1** is used  
- **Option 2** restores that backup if needed  

### Usage
1. Run the Python file  
2. Select the desired option  
3. The process is fully automated  

### Security Notice
- Administrator permissions are required  
- All code is fully reviewable  
- No malicious code is published  
- If unsure, inspect the file using:
  - Notepad
  - VS Code
  - Notepad++

### Official python download

- [Download host cleanup file](https://raw.githubusercontent.com/TheBoss12332397/Zelesis_Issues/57f707fb5058814214f9402ed77a7491526e6ddd/hosts_cleanup.py)

### Official G Hub Setup Guide
https://github.com/zen-ham/HID_Arduino/blob/master/GHUB_exploit/readme.md

---

## Refund Guide — Zelesis Neo

This section explains how to **correctly request a refund**.

⚠️ Incorrect formatting may delay processing.

---

### STEP 1 — Required Details

All details **must** be formatted exactly like this:

Email:
Purchase Date:
License Key:

Reason: (Optional)

Example (NOT a real request):

Email: borger1231@gmail.com  
Purchase Date: 21/06/2025 - 12:31 PM  
License Key: 4HBX7RJR7B6SLDKPK8NKBQA42CNE0  

---

### STEP 2 — Ticket Message

Send the following inside a support ticket (edit with your own details):

https://discord.com/channels/1232617064959709224/1381153501836607610/1381156175684304996

I would like to request a refund for Zelesis Neo.

Reason (Optional): Did not meet my expectations

Email: your@email.com  
License Key: YOUR-LICENSE-KEY  
Purchase Date: DD/MM/YYYY - Time  

---

### IMPORTANT NOTICE

- Refunds are NOT instant  
- Refunds take 5–10 business days  
- Processing is handled by Stripe  
- Processing speed cannot be accelerated  
- Refunds are only available within 3 days of purchase  

---

## Zelesis AI — Getting Started

Read this section carefully before using Zelesis AI to avoid crashes, misconfiguration, and detection issues.

---

## Configs

- Configs are NOT universal  
- Every setup differs due to:
  - DPI
  - Mouse hardware
  - Sensitivity
  - Movement method

Important Notes:
- Do NOT expect configs to work out-of-the-box  
- Manual tuning is REQUIRED  

Importing Configs:
- Importing configs is safe  
- You MUST verify your movement method  
- Zelesis does NOT auto-detect movement methods  

⚠️ IMPORTANT  
If a config uses **Arduino movement** and no Arduino is connected,  
the config WILL NOT work.

You must manually select one:
- Win32
- Ghub
- Arduino
- KMBOX_B

---

## Models (YOLO)

Custom YOLO models are supported but MUST follow strict rules.

Minimum Required Classes:
- Class 0 → Head (REQUIRED)
- Class 1 → Body (REQUIRED)

Optional / Ignore Classes:
- Class 3 & 4 → Ignore (teammates, dead bodies, etc.)
- Additional classes are allowed

Example Class Layout:

class_player = 0  
class_bot = 1  
class_weapon = 2  
class_outline = 3  
class_dead_body = 4  
class_hideout_target_human = 5  
class_hideout_target_balls = 6  
class_head = 7  
class_smoke = 8  
class_fire = 9  
class_third_person = 10  

Resolution:
- Any square resolution is supported  
- Recommended: 640×640  

❌ Incorrect model structure WILL cause crashes.

Crash Recovery:
1. Open Zelesis AI  
2. Keep it open  
3. Open Task Manager  
4. Right-click Zelesis AI  
5. Open file location  
6. Delete the imported model  

---

## Movement Methods

Supported:
- Win32  
- Ghub  
- Arduino (Paid)  
- KMBOX_B (Paid)  

Recommended Usage:
- Win32 → Weak anti-cheat games (e.g. Roblox)
- Ghub → Popular titles (Valorant, COD)
- Arduino → All titles (Undetected so far)
- KMBOX_B → All titles (Undetected so far)

⚠️ WARNING  
Win32 is highly detected in most games.

---

## Anti-Cheat Notice

Zelesis is undetected by most anti-cheats, but does NOT protect you from:

- Manual reviews  
- Manual bans  

Going blatant WILL result in a ban.  
Only you can prevent manual bans.

---

## Arduino Resources

Purchase Links:
- https://a.co/d/f6ucDzk
- https://www.alibaba.com/product-detail/Leonardo-R3-High-Quality-Development-Board_1601564076478.html
- https://www.amazon.com.au/Changor-ATmega32u4-Microcontroller-Development-Leonardo/dp/B0FPD9DK6Y

Arduino HID Setup Guide:
https://github.com/zen-ham/HID_Arduino/blob/master/readme.md

---

## Zelesis Installer & First-Time Setup

Step 1 — License Key
- Check the email used during signup
- Wait 1–2 minutes
- Check spam folder
- If delayed over 1 hour, create a support ticket

Step 2 — Installer Download
- Open the download link (usually Google Drive)
- Wait for the download to complete fully

Step 3 — Installing
- Open the installer
- If Windows Defender appears:
  - Click More info
  - Click Run anyway

Step 4 — Installer Process
- Installer size ~1.7 GB
- Do NOT spam-click
- Review install location carefully

Step 5 — First Launch
- Search Zelesis in Start Menu
- Run as Administrator (REQUIRED)

Setup Notes:
- Initialization may take ~10 minutes
- Do NOT close Zelesis
- Do NOT shut down your PC

Once complete:
- Zelesis Neo will launch
- Enter your license key
- Clipboard history: Win + V
