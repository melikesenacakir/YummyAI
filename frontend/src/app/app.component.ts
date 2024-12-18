import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchbarComponent } from './components/searchbar/searchbar.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone:true,
  imports:[RouterOutlet,SearchbarComponent,CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  hasResults = false;
  searchResult = ''; 
  displayedText = ''; 
  typingIndex = 0; 

  onSearchResults($event:any): void {

      this.searchResult = $event;
      if(this.searchResult.length>0){
        this.hasResults=true
      }
      console.log(this.searchResult)
      this.startTypingEffect(); 

  }

  startTypingEffect() {
    this.typingIndex = 0;
    this.displayedText = '';
    const interval = setInterval(() => {
      if (this.typingIndex < this.searchResult.length) {
        this.displayedText += this.searchResult[this.typingIndex];
        this.typingIndex++;
      } else {
        clearInterval(interval);
      }
    }, 20); 
  }
}
