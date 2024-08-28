import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
const firebaseConfig = {
    apiKey: "AIzaSyCmFKTZoBw5x6-WvXNwn34CD0gvfFYup5c",
    authDomain: "pantry-tracker-7462b.firebaseapp.com",
    projectId: "pantry-tracker-7462b",
    storageBucket: "pantry-tracker-7462b.appspot.com",
    messagingSenderId: "36623385655",
    appId: "1:36623385655:web:c0be359af06fe234192bb2",
 }

const app = initializeApp(firebaseConfig)
const firestore = getFirestore(app)
export {app, firestore}