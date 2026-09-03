---
title: "2026-09-04 - Encryption & Decryption - Learning Point 5"
tags:
  - learning
  - encryption
created: 2026-09-04
---

# HTTPS Combines Both Encryption Types for Secure Web Browsing

HTTPS uses both symmetric and asymmetric encryption together. When your browser connects to a secure website: first, asymmetric encryption (RSA/ECC) authenticates the server and securely exchanges a session key. Then, symmetric encryption (AES) takes over for the actual data transfer because it's much faster. This hybrid approach gives you the best of both worlds — easy key exchange and fast bulk encryption. The little padlock icon in your browser means all of this is happening behind the scenes, protecting your passwords, credit cards, and messages from eavesdroppers.

## Key Takeaway
HTTPS combines asymmetric encryption (key exchange + authentication) with symmetric encryption (fast bulk data transfer) — the padlock means both are working.

## Related Concepts
- TLS / SSL
- Hybrid Encryption
- Digital Certificates

---

## 中文：HTTPS 結合兩種加密方式實現安全網頁瀏覽

HTTPS 同時使用對稱和非對稱加密。當你的瀏覽器連接到一個安全網站時：首先，非對稱加密（RSA/ECC）用於驗證伺服器身份並安全地交換一個會話密鑰。然後，對稱加密（AES）接管實際的數據傳輸，因為它速度快得多。這種混合方式結合了兩者的優點——既方便交換密鑰，又有快速的批量加密。你瀏覽器位址列旁邊的小鎖頭圖示，代表這一切都在幕後運行，保護你的密碼、信用卡和訊息不被竊聽。

## 核心要點
HTTPS 結合非對稱加密（密鑰交換 + 身份驗證）和對稱加密（快速的批量數據傳輸）——瀏覽器的鎖頭意味著兩者都在運作。

## 相關概念
- TLS / SSL
- 混合加密
- 數字證書
