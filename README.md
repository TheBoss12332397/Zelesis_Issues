<div align="center">

# 🚀 Zelesis Neo & Utilities
**The Complete Guide & Documentation**

[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)]()
[![Support](https://img.shields.io/badge/Support-Discord-7289da.svg)]()

This repository contains official guides, tools, and setup instructions for **Zelesis Neo**, **Zelesis AI**, and supporting utilities (including Logitech G Hub fixes and Arduino HID usage). Please read the relevant sections carefully to avoid setup issues, crashes, or delays.

</div>

---

## 📚 Table of Contents
1. [First-Time Setup & Installation](#1-first-time-setup--installation)
2. [Console Remote Play (Chiaki)](#2-console-remote-play-chiaki)
3. [Zelesis AI Configuration](#3-zelesis-ai-configuration)
4. [Hardware Spoofing & Fixes](#4-hardware-spoofing--fixes)
5. [Troubleshooting & Support](#5-troubleshooting--support)

---

## 1. First-Time Setup & Installation

Follow these steps carefully to ensure a clean installation.

*   **Step 1 — License Key:** Check the email used during signup (wait 1–2 minutes and check your spam folder). If delayed over 1 hour, create a support ticket.
*   **Step 2 — Download:** Open the provided link (usually Google Drive) and allow the download to complete fully. The installer size is approximately **1.7 GB**.
*   **Step 3 — Security Prompts:** If Windows Defender flags the installer, click **More info** $\rightarrow$ **Run anyway**.
*   **Step 4 — Execution:** Run the installer and review the installation location. Do not spam-click.
*   **Step 5 — Initialization:** Search for Zelesis in the Start Menu and **Run as Administrator** (this is strictly required). 
    > ⚠️ **IMPORTANT:** Initialization may take ~10 minutes. Do NOT close Zelesis or shut down your PC during this process.
*   **Step 6 — Activation:** Once Zelesis Neo launches, enter your license key. *(Tip: Use `Win + V` to access your clipboard history).*

---

## 2. Console Remote Play (Chiaki)

To achieve minimal input delay when routing console gameplay through Zelesis, use the following hardware and software stack.

### Prerequisites
*   **2x Ethernet Cables** (One for your PC, one for your Console)
*   **[Chiaki](https://chiaki.en.softonic.com)** (Remote Play Client)

### Configuration Steps
1.  **Network Setup:** Hardwire both your PC and your console directly to your router using Ethernet cables. This eliminates wireless latency.
2.  **Chiaki Installation:** Download, install, and link Chiaki to your PS5 (refer to YouTube tutorials for initial linking).
3.  **Display & Inputs:** Launch Chiaki on your PC to view the console output. Connect your controller to the PC and verify that your inputs are registering. 
    > 💡 **Pro Tip:** Play your game on a separate monitor or TV utilizing the PS5's direct HDMI output, while leaving Chiaki running on the PC display for Zelesis to capture.
4.  **Zelesis Targeting:** Open Zelesis and configure your controller settings. Ensure the Chiaki window is either perfectly centered or running in fullscreen so the AI can analyze the entire gameplay area.
5.  **Calibration:** Manually adjust your smoothing and tracking settings within Zelesis until it tracks reliably without over-flicking. If you require absolute hardware-level lock-on, you will need to invest in a Titan 2 device.

---

## 3. Zelesis AI Configuration

Read this section carefully before using Zelesis AI to avoid crashes, misconfiguration, and detection issues.

### Profile Configs
Configs are **not universal**. Every setup differs based on DPI, mouse hardware, sensitivity, and movement method. 
*   Manual tuning is strictly required; do not expect imported configs to work out-of-the-box.
*   You must verify your movement method, as Zelesis does not auto-detect this. 
*   **Warning:** If a config is set to **Arduino movement** and no Arduino is connected, it will fail to work.

### Supported Movement Methods
You must manually select one of the following methods:
*   🔴 **Win32:** For titles with weak anti-cheat (e.g., Roblox). *Highly detected in mainstream games.*
*   🟡 **Ghub:** For popular titles (Valorant, COD, etc.).
*   🟢 **Arduino (Paid) / KMBOX_B (Paid):** Safest methods for all titles (undetected so far).

### Models (YOLO)
Custom YOLO models are supported but must follow strict indexing rules to prevent software crashes. Any square resolution is supported (640×640 is recommended).

**Required Classes:**
*   `Class 0` $\rightarrow$ Head
*   `Class 1` $\rightarrow$ Body

*(Optional classes such as weapons, dead bodies, or teammates can be set to ignore).*

---

## 4. Hardware Spoofing & Fixes

### Arduino Resources
For hardware-level movement spoofing, refer to the [Official Arduino HID Setup Guide](https://github.com/zen-ham/HID_Arduino/blob/master/readme.md). 
*   **Purchase Links:** [Amazon Option 1](https://a.co/d/f6ucDzk) | [Amazon Option 2](https://www.amazon.com.au/Changor-ATmega32u4-Microcontroller-Development-Leonardo/dp/B0FPD9DK6Y) | [Alibaba](https://www.alibaba.com/product-detail/Leonardo-R3-High-Quality-Development-Board_1601564076478.html).

### Logitech G Hub Install Fix
If Logitech G Hub fails to install (usually caused by running unauthorized PowerShell commands), use our automated Python tool to clean your host files. Admin permissions are required.
*   [Download hosts_cleanup.py](https://github.com/TheBoss12332397/Zelesis_Issues/releases/download/download/hosts_cleanup.py)
*   [Official G Hub Setup Guide](https://github.com/zen-ham/HID_Arduino/blob/master/GHUB_exploit/readme.md)

---


---

## 5. Troubleshooting & Support

### Engine File Deletion Guide

If Zelesis Neo is crashing or throwing errors, clearing the compiled engine files often resolves the issue.

1. Press `Win + R`, paste `%LOCALAPPDATA%\Programs\Zelesis Neo`, and press Enter.
2. Navigate to the `models` folder.
3. Delete `universal.engine` and any other `.engine` files. **Do not delete anything else.**
4. Relaunch Zelesis Neo.

### Anti-Cheat & Moderation Notice

Zelesis is undetected by most automated anti-cheats, but it **does not** protect you from manual reviews or manual bans. Playing blatantly will result in a ban.

> 🛑 **Trust Notice:** Only accept support from **@.theboss12332397** and **@.yxssir**. These are the only trusted moderators with the **@Sr. Mod/Helper** role. We utilize the Windows built-in **Quick Assist** feature for secure troubleshooting.

### Refund Policy

Refunds are processed by Stripe and take **5–10 business days**. They are only available within **3 days of purchase**. To request one, submit a [Discord support ticket](https://www.google.com/search?q=https://discord.com/channels/1232617064959709224/1381153501836607610/1381156175684304996) with the following exact format:

I would like to request a refund for Zelesis Neo.

Email: your@email.com  
License Key: YOUR-LICENSE-KEY  
Purchase Date: DD/MM/YYYY - Time  
Reason (Optional): Did not meet my expectations

