const div = document.getElementById("popular");
const search = document.getElementById("search");
const signin = document.getElementById("signin");
const message = document.getElementById("message");
const user = localStorage.getItem("user");

function createImgDiv(path) {
	const imgDiv = document.createElement("div");
	imgDiv.className = "rounded-lg overflow-hidden";
	const img = document.createElement("img");
	img.src = `static/images/${path}`;
	img.className = "w-full h-full object-cover";
	imgDiv.appendChild(img);
	return imgDiv;
}

const sports = [
	{ title: "Football", img: "football.jpg" },
	{ title: "Basketball", img: "basketball.jpg" },
	{ title: "Volleyball", img: "volleyball.jpg" },
	{ title: "Tennis", img: "tennis.jpg" },
	{ title: "Padel", img: "Padel.jpg" },
];

if (!user) {
	search.style.display = "none";
	signin.style.display = "block";
	message.style.display = "block";
} else {
	signin.style.display = "none";
	search.style.display = "flex";
	message.style.display = "none";
}

for (let i = 0; i < sports.length; i++) {
	const item = document.createElement("a");
	item.className = "group";
	if (!user) {
		item.classList.add("disabled");
	}
	item.href = `/sport/search=${sports[i].title.toLocaleLowerCase()}`;
	const imgDiv = createImgDiv(sports[i].img);
	item.appendChild(imgDiv);
	const title = document.createElement("h4");
	title.innerHTML = sports[i].title;
	title.className =
		"mt-3 font-semibold group-hover:text-sky-500 group-hover:border-b border-b-sky-500 transition-all duration-200";
	item.appendChild(title);
	div.appendChild(item);
}
