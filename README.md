# HarmanFood

## Frontend

Frontend static files can be built for production environment with webpack.
```
cd frontend
npm run build
```
These files are created under <ROOT>/dist folder, which is excluded from version control.

### Frontend dev server

Webpack is also configured to run server which really helps with UI development. Frontend is divided to 2 separate pages:
  1. Login page. It can be started via:
  ```
  cd frontend
  npm run login
  ```
  2. Main content page.
  ```
  cd frontend
  npm run dev
  ```

  Both pages are served on localhost:8080

## Backend

Flask server is used for backend. Source files are placed under <ROOT>/webserver.

To run websrever:
1. Build static files (from frontend)
2. Set environment variables:
   ```
   set FLASK_APP=webserver
   set FLASK_ENV=development
   ```
3. Start webserver (from <ROOT>)
	```
	flask run
	```

Webserver will listen 127.0.0.1:5000

