import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, catchError } from 'rxjs/operators';
import { Observable, of } from 'rxjs';

import { AppConfig } from '../../conf/app.config';

// Adress is subject to change so unknown
type Municipality = {
    place_id: number;
    licence: string;
    osm_type: string;
    osm_id: number;
    lat: string;
    lon: string;
    display_name: string;
    address: Address;
    boundingbox: string[];
};

type Address = {
    city: string | null;
    town: string | null;
    village: string | null;
};

@Injectable({
    providedIn: 'root',
})
export class RefGeoService {
    private readonly URL = AppConfig.API_CITY;

    constructor(protected http: HttpClient) {}

    getMunicipality(lat: number, lon: number): Observable<string> {
        return this.http
            .get<Municipality>(`${this.URL}?lat=${lat}&lon=${lon}&format=json`)
            .pipe(
                map((municipality) => {
                    const address = municipality.address;
                    const city = address.city
                        ? address.city
                        : address.town
                        ? address.town
                        : address.village
                        ? address.village
                        : 'Non trouvé';
                    return city;
                })
            );
    }

    private handleError<T>(operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {
            console.error(`${operation} failed: ${error.message}`, error);
            return of(result as T);
        };
    }
}
