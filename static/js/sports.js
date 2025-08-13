import { createImgDiv, createRatingElement, getAllSports } from "./module.js";

const errorMessage = document.getElementById("errorMessage");

const div = document.getElementById("popular");

function displayCategories(cat) {
	for (let i = 0; i < cat.length; i++) {
		const item = document.createElement("div");
		item.className = " grid grid-cols-2 h-28 my-3 gap-4";
		const imgDiv = createImgDiv(cat[i].img);
		item.appendChild(imgDiv);
		const details = document.createElement("a");
		details.className = "group";
		details.href = `/results?search=${cat[i].title.toLocaleLowerCase()}`;
		const title = document.createElement("h4");
		title.innerHTML = cat[i].title;
		title.className =
			"mt-3 font-semibold group-hover:text-sky-500 transition-all duration-200";
		details.append(title);
		const available = document.createElement("p");
		available.className = "my-3 text-zinc-400";
		const rating = createRatingElement(cat[i].rating);
		available.innerText = `Available: ${cat[i].playgroundCount}`;
		details.append(available);
		details.append(rating);
		item.appendChild(details);

		div.appendChild(item);
	}
}

getAllSports()
	.then((res) => {
		displayCategories(res.data);
	})
	.catch((error) => {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	});
