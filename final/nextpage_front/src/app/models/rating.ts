import { Book } from "./book";

export class Rating {
        count : number;
        sum: number;
        book: Book;
        constructor(count: number,  sum: number, book: Book){
            this.count = count;
            this.sum = sum;
            this.book = book;
        }
}