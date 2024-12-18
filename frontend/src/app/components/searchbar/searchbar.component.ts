import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { SearchService } from '../../services/search.service';

@Component({
  selector: 'app-searchbar',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './searchbar.component.html',
  styleUrl: './searchbar.component.scss'
})
export class SearchbarComponent {
  searchTerm: string = '';
  searchResults: string='';
  errorMessage: string = '';
  searchClicked: boolean = false;
  @Output() dataEmitter = new EventEmitter<any>();

  constructor(private searchService: SearchService) {}

  searchRecipe(clicked: boolean) {
    this.searchClicked = clicked;
    if (this.searchTerm.trim() !== '') {
      this.searchService.searchRecipes(this.searchTerm).subscribe({
        next: (data) => {
            this.searchResults = data.recipe;
            this.dataEmitter.emit(this.searchResults)
        },
        error: () => {
          this.errorMessage = 'Tarifler yüklenirken bir hata oluştu!';
          this.dataEmitter.emit(this.errorMessage)
  
        }
      });
    } else {
      this.errorMessage = 'Lütfen bir malzeme girin.';
      this.dataEmitter.emit(this.errorMessage)
    }
  }
}
