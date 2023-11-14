#!/usr/bin/node
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
			this.width = w;
			this.height = h;
		} else {
			return {};
		}
	}

	print() {
		if (this.width && this.height) {
			for (let i = 0; i < this.height; i++) {
				let row = '';
				for (let j = 0; j < this.width; j++) {
					row += 'X';
				}
				console.log(row);
			}
		}
	}
}

const rectangle1 = new Rectangle(4, 3);
rectangle1.print();

const rectangle2 = new Rectangle(0, 5);
console.log(rectangle2);
