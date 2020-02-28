## Structure

```app/``` Source code for the application <br>
```bin/```  Scripts to initialize, update, or/and deploy application. <br>
```config/```  Configuration, routes, database, etc. <br>
```db/```  Current schema and migrations of the database. <br>
```lib/```  External modules of the app. <br>
```log/``` logs. <br>
```public``` static files and complicated assets. <br>
```test``` Unit test. <br>
```tmp``` Temporary files. <br>
```vendor``` third party code. <br>
```gemfile``` gem file configuration. <br>



| HTTP Verb | Path | Controller#Action | Used for |
|-|-|-|-|
| GET | /photos | photos#index | display a list of all photos |
| GET | /photos/new | photos#new | return an HTML form for creating a new photo |
| POST | /photos | photos#create | create a new photo |
| GET | /photos/:id | photos#show | display a specific photo |
| GET | /photos/:id/edit | photos#edit | return an HTML form for editing a photo |
| PATCH/PUT | /photos/:id | photos#update | update a specific photo |
| DELETE | /photos/:id | photos#destroy | delete a specific photo |


