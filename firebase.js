// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import{getFirestore} from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDus-85UZjCIns8wVf8NSI4KKTJcJ92_RY",
  authDomain: "inventory-management-36c21.firebaseapp.com",
  projectId: "inventory-management-36c21",
  storageBucket: "inventory-management-36c21.appspot.com",
  messagingSenderId: "915768690640",
  appId: "1:915768690640:web:ef937c5a0c430a820e9bd5",
  measurementId: "G-6E81G4NHY1"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const firestore = getFirestore(app);

export{firestore};