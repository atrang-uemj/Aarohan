// ============================================================
//  firebase.js — Aarohan 1.0 | Firebase v10 (Modular SDK)
//  Exports: auth, db, googleProvider, RecaptchaVerifier utility
// ============================================================
//
//  HOW TO SET UP:
//  1. Go to https://console.firebase.google.com/
//  2. Create a project → "Aarohan1"
//  3. Add a Web App → Copy the firebaseConfig object
//  4. REPLACE the firebaseConfig below with your own config
//
//  Enable in Firebase Console → Authentication → Sign-in method:
//    ✅ Email/Password
//    ✅ Google
//    ✅ Phone
//
//  Firestore: Create database in Test Mode, then apply rules below.
// ============================================================

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, GoogleAuthProvider }
    from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

// ============================================================
//  🔧 PASTE YOUR FIREBASE CONFIG HERE
// ============================================================
const firebaseConfig = {
  apiKey: "AIzaSyCWLIAChjAXJJh4Sg4RaNFSDZgdIAjqddg",
  authDomain: "aarohan-19b83.firebaseapp.com",
  projectId: "aarohan-19b83",
  storageBucket: "aarohan-19b83.firebasestorage.app",
  messagingSenderId: "366041608093",
  appId: "1:366041608093:web:d9a6fd50b9189e152e4974"
};

// Initialize
const app = initializeApp(firebaseConfig);

// ============================================================
//  Exported Services
// ============================================================
export const auth = getAuth(app);
export const db = getFirestore(app);

// Google Auth Provider — scopes for basic profile info
export const googleProvider = new GoogleAuthProvider();
googleProvider.addScope('profile');
googleProvider.addScope('email');
googleProvider.setCustomParameters({ prompt: 'select_account' });

// ============================================================
//  FIRESTORE SECURITY RULES (paste in Firebase Console)
// ============================================================
//
//  rules_version = '2';
//  service cloud.firestore {
//    match /databases/{database}/documents {
//      match /participants/{docId} {
//        allow read, write: if request.auth != null;
//      }
//    }
//  }
//
// ============================================================

// ============================================================
//  ADMIN VERIFICATION CONCEPT
// ============================================================
//
//  QR Scan Flow:
//    1. Admin scans QR on gate pass → gets GatePassID only
//    2. Query: db.collection('participants')
//               .where('gatePassID', '==', scannedID).get()
//    3. Found → valid entry  |  Not found → deny entry
//
//  Manual Search:
//    Admin panel with a search input → query Firestore by gatePassID
//
//  Privacy: QR never contains name/email — only the opaque ID.
// ============================================================
