import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AddIngredientComponent } from './add-ingredient/add-ingredient.component';

@Component({
  selector: 'app-searchbar',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './searchbar.component.html',
  styleUrl: './searchbar.component.scss'
})
export class SearchbarComponent {

  searchClicked: boolean = false;

  //constructor(private dialog: MatDialog) {}


  searchRecipe(clicked: boolean) {
    this.searchClicked=clicked;
  }

  addIngredient(): void {
    /* this.dialog.open(AddIngredientComponent, {
      width: '10vw',
      height: '30vh'
    }); */
  }
}
