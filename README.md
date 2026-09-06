<div align="center">

# 🚀 Zelesis Neo & Utilities
**The Complete Guide & Documentation**

[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)]()
[![Support](https://img.shields.io/badge/Support-Discord-7289da.svg)]()

This repository contains official guides, tools, and setup instructions for **Zelesis Neo**, **Zelesis AI**, and supporting utilities (including Logitech G Hub fixes and Arduino HID usage)[cite: 1]. Please read the relevant sections carefully to avoid setup issues, crashes, or delays[cite: 1].

</div>

---

## 📚 Table of Contents
1. [First-Time Setup & Installation](#1-first-time-setup--installation)
2. [Console Remote Play (Chiaki Integration)](#2-console-remote-play-chiaki-integration)
3. [Zelesis AI Configuration](#3-zelesis-ai-configuration)
4. [Hardware Spoofing & Fixes](#4-hardware-spoofing--fixes)
5. [Troubleshooting & Support](#6-troubleshooting--support)

---

## 1. First-Time Setup & Installation

Follow these steps carefully to ensure a clean installation[cite: 1].

*   **Step 1 — License Key:** Check the email used during signup (wait 1–2 minutes and check your spam folder)[cite: 1]. If delayed over 1 hour, create a support ticket[cite: 1].
*   **Step 2 — Download:** Open the provided link (usually Google Drive) and allow the download to complete fully[cite: 1]. The installer size is approximately **1.7 GB**[cite: 1].
*   **Step 3 — Security Prompts:** If Windows Defender flags the installer, click **More info** $\rightarrow$ **Run anyway**[cite: 1].
*   **Step 4 — Execution:** Run the installer and review the installation location[cite: 1]. Do not spam-click[cite: 1].
*   **Step 5 — Initialization:** Search for Zelesis in the Start Menu and **Run as Administrator** (this is strictly required)[cite: 1]. 
    > ⚠️ **IMPORTANT:** Initialization may take ~10 minutes[cite: 1]. Do NOT close Zelesis or shut down your PC during this process[cite: 1].
*   **Step 6 — Activation:** Once Zelesis Neo launches, enter your license key[cite: 1]. *(Tip: Use `Win + V` to access your clipboard history[cite: 1]).*

---

## 2. Console Remote Play (Chiaki Integration)

To achieve minimal input delay when routing console gameplay through Zelesis, use the following hardware and software stack.

### Prerequisites
*   **2x Ethernet Cables** (1 for your PC and 1 for your Console for minimal delay)
*   **[Chiaki](https://chiaki.en.softonic.com)** (Remote Play Client)
*   **Zelesis Application**

### Configuration Steps
1.  **Network Setup:** For minimal input delay, connect your PC and console straight to your router with an Ethernet cable (optional but recommended).
2.  **Chiaki Installation:** Download Chiaki and set it up by connecting your PS5 to it (please look up a YouTube tutorial, it is very simple).
3.  **Display & Inputs:** Once Chiaki is all set up, you can click on your console icon and see it on your PC. Connect your controller to your PC and make sure you can move stuff around. 
    > 💡 **Pro Tip:** Play your game on a separate monitor or TV utilizing a separate screen and an HDMI for your PS5, while leaving Chiaki running on the PC display for Zelesis to capture.
4.  **Zelesis Targeting:** Open Zelesis and set up your controller. Either center Chiaki or run it in fullscreen so Zelesis can see the whole screen.
5.  **Calibration:** You are all set. It should track, etc., but mind you, input delay will make the aimbot not be a full lock-on. You will have to play around with it till it tracks but doesn't over-track. If you want a full lock-on, invest in a Titan 2 (good luck tryin' to figure that shit out).

---

## 3. Zelesis AI Configuration

Read this section carefully before using Zelesis AI to avoid crashes, misconfiguration, and detection issues[cite: 1].

### Profile Configs
Configs are **not universal**[cite: 1]. Every setup differs based on DPI, mouse hardware, sensitivity, and movement method[cite: 1]. 
*   Manual tuning is strictly required; do not expect imported configs to work out-of-the-box[cite: 1].
*   You must verify your movement method, as Zelesis does not auto-detect this[cite: 1]. 
*   **Warning:** If a config uses **Arduino movement** and no Arduino is connected, the config will fail to work[cite: 1].

### Supported Movement Methods
You must manually select one of the following methods[cite: 1]:
*   🔴 **Win32:** For titles with weak anti-cheat (e.g., Roblox)[cite: 1]. *Highly detected in most mainstream games[cite: 1].*
*   🟡 **Ghub:** For popular titles (Valorant, COD, etc.)[cite: 1].
*   🟢 **Arduino (Paid) / KMBOX_B (Paid):** Safest methods for all titles (undetected so far)[cite: 1].

### Models (YOLO)
Custom YOLO models are supported but must follow strict indexing rules to prevent software crashes[cite: 1]. Any square resolution is supported (640×640 is recommended)[cite: 1].

**Required Classes[cite: 1]:**
*   `Class 0` $\rightarrow$ Head (Required)[cite: 1]
*   `Class 1` $\rightarrow$ Body (Required)[cite: 1]

*(Optional classes such as Class 3 & 4 for teammates or dead bodies can be set to ignore)[cite: 1].*

---

## 4. Hardware Spoofing & Fixes

### Arduino Resources
Purchase links and setup guides for hardware-level movement spoofing[cite: 1]:
*   **Purchase Links:** [Amazon Option 1](https://a.co/d/f6ucDzk) | [Amazon Option 2](https://www.amazon.com.au/Changor-ATmega32u4-Microcontroller-Development-Leonardo/dp/B0FPD9DK6Y) | [Alibaba](https://www.alibaba.com/product-detail/Leonardo-R3-High-Quality-Development-Board_1601564076478.html)[cite: 1].
*   **HID Setup Guide:** [Official Arduino HID Setup Guide](https://github.com/zen-ham/HID_Arduino/blob/master/readme.md)[cite: 1].

### Logitech G Hub Install Fix
If Logitech G Hub fails to install (usually caused by running unauthorized PowerShell commands), use our automated Python tool to clean your host files[cite: 1]. Admin permissions are required[cite: 1].
*   [Download hosts_cleanup.py](https://github.com/TheBoss12332397/Zelesis_Issues/releases/download/download/hosts_cleanup.py)[cite: 1]
*   [Official G Hub Setup Guide](https://github.com/zen-ham/HID_Arduino/blob/master/GHUB_exploit/readme.md)[cite: 1]

---

## 5. Troubleshooting & Support

### Engine File Deletion Guide

If Zelesis Neo is crashing or throwing errors, clearing the uncompiled engine files often resolves the issue:

1. Press the Run dialog by pressing `Win + R`.


2. Paste the path `%LOCALAPPDATA%\Programs\Zelesis Neo` and press Enter.


3. Navigate to the `models` folder.


4. Delete `universal.engine` and any other `.engine` file. Do not delete any other files. Leave the rest untouched.


5. Relaunch Zelesis Neo.



### Anti-Cheat & Moderation Notice

Zelesis is undetected by most automated anti-cheats, but it **does not** protect you from manual reviews or manual bans. Playing blatantly will result in a ban. Only you can prevent manual bans.

> 🛑 **Trust Notice:** Please do not trust any moderators other than **@.theboss12332397** and **@.yxssir**. These are the only two trusted moderators with the **@Sr. Mod/Helper** role. For assistance, use the Windows built-in feature called **Quick Assist** to ensure secure communication.
> 
> 

### Refund Policy

Refunds are processed by Stripe and take **5–10 business days**. They are only available within **3 days of purchase**. To request one, submit a [Discord support ticket](https://www.google.com/search?q=https://discord.com/channels/1232617064959709224/1381153501836607610/1381156175684304996) with the following exact format:

```text
I would like to request a refund for Zelesis Neo.

Email: your@email.com  
License Key: YOUR-LICENSE-KEY  
Purchase Date: DD/MM/YYYY - Time  
Reason (Optional): Did not meet my expectations
