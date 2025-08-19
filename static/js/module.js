// function to create img html element dynamic
export function createImgDiv(path) {
	const imgDiv = document.createElement("div");
	imgDiv.className = "rounded-lg overflow-hidden ";
	const img = document.createElement("img");
	img.src = path;
	img.className = "w-full h-full object-cover";
	imgDiv.appendChild(img);
	return imgDiv;
}

// function to create rating html element
export function createRatingElement(rate) {
	const div = document.createElement("div");
	div.className = "flex gap-2 mt-auto";

	for (let i = 0; i < 5; i++) {
		if (i < rate) {
			const fillStar = document.createElement("img");
			fillStar.src = "static/images/fill-star.png";
			fillStar.className = "size-5";
			div.append(fillStar);
		} else {
			const star = document.createElement("img");
			star.src = "static/images/star.png";
			star.className = "size-5";

			div.append(star);
		}
	}

	return div;
}

// API request to get sports from backend
export async function getAllSports() {
	const response = await fetch("http://127.0.0.1:5000/api/sports", {
		method: "GET",
	});
	if (!response.ok) throw new Error(response.statusText || "Can't Get sports");
	const payload = await response.json();
	if (!payload.data.length) throw new Error("There are no categories to show");
	return payload;
}

// API request to get all courts from backend
export async function getAllPlayGround(category) {
	const response = await fetch(
		`http://127.0.0.1:5000/api/playgrounds?search=${category}`,
		{
			method: "GET",
		}
	);
	if (!response.ok)
		throw new Error(response.statusText || "Can't Get playgrounds");
	const payload = await response.json();

	if (!payload.data.length)
		throw new Error(payload.message || "There are no playgrounds to show");
	return payload;
}
