import { log } from "console";
import { initializeApp } from "firebase/app";
import { getStorage, ref, uploadBytes } from "firebase/storage";
import 'fs'
import { readFile, readFileSync } from "fs";

const firebaseConfig = {
  apiKey: "AIzaSyDMCyR9dEslWRhNvp5r4A-QnbcbKOdAns4",
  authDomain: "ndvi-rpi.firebaseapp.com",
  projectId: "ndvi-rpi",
  storageBucket: "ndvi-rpi.appspot.com",
  messagingSenderId: "579623357333",
  appId: "1:579623357333:web:6007b1629403601bd6449c",
  measurementId: "G-3JJSFEFSGJ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const storage = getStorage();
const storageRef = ref(storage);

const images = ref(storage, 'images');
const ndvi = ref(storage, 'images/ndvi.png');

try{
  const data = readFileSync('color_mapped_image.png');
  uploadBytes(ndvi, new File(data, "ndvi.png")).then(() => {
  console.log("Uploaded");
  })
}catch(err){
  log(err)
}
