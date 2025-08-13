import { createImgDiv, getAllSports } from "./module.js";

const div = document.getElementById("popular");
const search = document.getElementById("search");
const signin = document.getElementById("signin");
const message = document.getElementById("message");
const user = localStorage.getItem("user");

function displayCategories(cat) {
	for (let i = 0; i < cat.length; i++) {
		const item = document.createElement("a");
		item.className = "group";
		if (!user) {
			item.classList.add("disabled");
		}
		item.href = `/results?search=${cat[i].title.toLocaleLowerCase()}`;
		const imgDiv = createImgDiv(cat[i].img);
		item.appendChild(imgDiv);
		const title = document.createElement("h4");
		title.innerHTML = cat[i].title;
		title.className =
			"mt-3 font-semibold group-hover:text-sky-500 group-hover:border-b border-b-sky-500 transition-all duration-200";
		item.appendChild(title);
		div.appendChild(item);
	}
}

if (!user) {
	search.style.display = "none";
	signin.style.display = "block";
	message.style.display = "block";
} else {
	signin.style.display = "none";
	search.style.display = "flex";
	message.style.display = "none";
}

getAllSports()
	.then((res) => {
		displayCategories(res.data);
	})
	.catch((error) => {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	});
