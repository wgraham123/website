import { initializeApp } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-app.js";
import {
    getAuth,
    signInAnonymously,
    onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/12.7.0/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "AIzaSyDcwYAQoye1X4YznXtyh_-mLVTxMZWlEe0",
    authDomain: "website-98c94.firebaseapp.com",
    projectId: "website-98c94",
    storageBucket: "website-98c94.firebasestorage.app",
    messagingSenderId: "403011854830",
    appId: "1:403011854830:web:362f78ac054e8ec0c56eff",
    measurementId: "G-9T39V72F1V"
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

signInAnonymously(auth)
    .then(() => console.log("Signed in anonymously"))
    .catch((err) => console.log(err));

export function waitForAuthReady() {
    return new Promise((resolve) => {
        const unsub = onAuthStateChanged(auth, (user) => {
            if (user) {
                unsub();
                resolve(user);
            }
        });
    });
}

export async function getIdToken() {
    const user = auth.currentUser();
    if (!user) {
        throw new Error("User not authenticated yet!");
    }
    return await user.getIdToken();
}
