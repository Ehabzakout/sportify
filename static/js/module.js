export function createImgDiv(path) {
	const imgDiv = document.createElement("div");
	imgDiv.className = "rounded-lg overflow-hidden ";
	const img = document.createElement("img");
	img.src = path;
	img.className = "w-full h-full object-cover";
	imgDiv.appendChild(img);
	return imgDiv;
}

export function createRatingElement(rate) {
	const div = document.createElement("div");
	div.className = "flex gap-2";

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

export async function getAllSports() {
	const response = await fetch("http://127.0.0.1:5000/api/sports", {
		method: "GET",
	});
	if (!response.ok) throw new Error(response.statusText || "Can't Get sports");
	const payload = await response.json();
	if (!payload.data.length) throw new Error("There are no categories to show");
	return payload;
}

export async function getAllPlayGround() {
	const response = await fetch("http://127.0.0.1:5000/api/playgrounds", {
		method: "GET",
	});
	if (!response.ok)
		throw new Error(response.statusText || "Can't Get playgrounds");
	const payload = await response.json();
	if (!payload.data.length) throw new Error("There are no playgrounds to show");
	return payload;
}
