import { createRatingElement, getAllPlayGround } from "./module.js";
const errorMessage = document.getElementById("errorMessage");
const results = document.getElementById("results");
const search = new URLSearchParams(window.location.search).get("search");
const userId = localStorage.getItem("userId");

if (!userId) {
	errorMessage.innerText = "You Should signin to book court";
	errorMessage.style.display = "block";
}

// Function to add details about court
function createDetails(item) {
	const details = document.createElement("div");
	details.className = "flex flex-col";
	details.innerHTML = `<h3 class = font-bold text-lg>${item.name}</h3>
		<p class = text-zinc-400>${item.sport}</p>
		<p class = font-semibold>Price: ${item.price}/hr EGP </p>
		`;
	const rating = createRatingElement(item.rating);
	details.appendChild(rating);

	return details;
}

// display court and availability for booking
function createBook(item) {
	const book = document.createElement("div");
	book.className = "flex flex-col py-3";
	book.innerHTML = `<p class= flex gap-2 h-5><img src=static/images/location.png class= w-5 h-3/>${item.address}</p>
	`;

	// if user logged in show book options
	if (userId) {
		// create book button
		const bookButton = document.createElement("a");
		bookButton.innerText = "Book";
		bookButton.href = `/booking?courtId=${item.id}&userId=${userId}`;
		bookButton.className =
			"mt-auto w-full bg-[var(--main-color)] block text-center text-white fond-semibold py-1 hover:opacity-90 rounded-md";

		const p = document.createElement("p");
		p.innerText = "This playground is unavailable";
		p.className = "mt-auto text-red-500 fond-semibold";

		if (item.isReservable) {
			book.append(bookButton);
		} else book.append(p);
	}
	return book;
}

// function to generate courts depends on sport
function createResultsElements(playgrounds) {
	for (let item in playgrounds) {
		const div = document.createElement("div");
		div.className = "grid grid-cols-[auto,1fr,auto] gap-3 ";
		const imgDiv = document.createElement("div");
		imgDiv.className = "w-56 h-28";
		const img = document.createElement("img");
		img.src = playgrounds[item].img;
		img.className = "w-full h-full rounded-md ";
		imgDiv.append(img);
		const details = createDetails(playgrounds[item]);
		const book = createBook(playgrounds[item]);
		div.append(imgDiv);
		div.append(details);
		div.append(book);
		results.append(div);
	}
}

getAllPlayGround(search)
	.then((res) => {
		createResultsElements(res.data);
	})
	.catch((error) => {
		errorMessage.innerText = error.message;
		errorMessage.style.display = "block";
	});
