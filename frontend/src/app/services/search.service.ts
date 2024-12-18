import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  private url= 'http://127.0.0.1:5000'; // API uç noktasını buraya yazın

  constructor(private http: HttpClient) {}

  searchRecipes(query: string): Observable<any> {
    const body = { 'ingredients': query };

    const headers = { 'Content-Type': 'application/json' };
    const response=this.http.post(`${this.url}/search`,body,{headers,responseType:'json'});
    return response;
  }
}
