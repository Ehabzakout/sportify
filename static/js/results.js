import { getAllPlayGround } from "./module.js";
const errorMessage = document.getElementById("errorMessage");

getAllPlayGround()
	.then((res) => {
		console.log(res.data);
	})
	.catch((error) => {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	});
