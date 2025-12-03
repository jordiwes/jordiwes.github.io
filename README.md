# Friends Map

A simple, publicly accessible map showing where your friends are located around the world.

## Features

- Interactive Google Maps interface
- Friend locations pulled from Google Sheets
- Easy to update - just edit your spreadsheet
- No backend required - pure HTML/CSS/JavaScript
- Mobile responsive

## Setup Instructions

### Step 1: Get a Google Maps API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the "Maps JavaScript API"
4. Go to "Credentials" and create an API key
5. (Optional but recommended) Restrict the API key to your domain

### Step 2: Set Up Your Google Sheet

1. Create a new Google Sheet
2. Add three columns with these exact headers:
   - `Name` - Your friend's name
   - `Latitude` - The latitude coordinate
   - `Longitude` - The longitude coordinate

Example:

```
Name        | Latitude  | Longitude
Alice       | 40.7128   | -74.0060
Bob         | 51.5074   | -0.1278
Charlie     | 35.6762   | 139.6503
```

3. To find coordinates for a location:
   - Open Google Maps
   - Right-click on a location
   - Click on the coordinates to copy them
   - Or search for "latitude longitude [city name]"

4. Publish your Google Sheet to the web:
   - Click **File > Share > Publish to web**
   - Choose "Entire Document" or your specific sheet
   - Select **"Comma-separated values (.csv)"** format
   - Click "Publish"
   - Copy the URL provided

### Step 3: Configure the Map

1. Open `index.html` in a text editor
2. Find the `CONFIG` section near the top of the `<script>` tag
3. Replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual API key
4. Replace `YOUR_GOOGLE_SHEETS_CSV_URL` with your published Google Sheets CSV URL
5. Also update the API key in the script tag at the bottom:
   ```html
   <script async defer
       src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap">
   </script>
   ```

### Step 4: Deploy Your Map

You can host this map on any static hosting service:

#### Option 1: GitHub Pages (Free)
1. Create a new GitHub repository
2. Upload `index.html`
3. Go to Settings > Pages
4. Select the branch and save
5. Your map will be live at `https://yourusername.github.io/repository-name`

#### Option 2: Netlify (Free)
1. Create a [Netlify](https://www.netlify.com/) account
2. Drag and drop the `index.html` file
3. Your map will be live instantly

#### Option 3: Vercel (Free)
1. Create a [Vercel](https://vercel.com/) account
2. Import your project
3. Deploy with one click

#### Option 4: Local Testing
Simply open `index.html` in your web browser. Note: Some browsers may block loading external data locally due to CORS policies.

## Updating Friend Locations

Just edit your Google Sheet and the changes will automatically appear on the map (you may need to refresh the page).

## Customization

### Change Map Center
Edit the `center` property in the `initMap()` function:
```javascript
center: { lat: 20, lng: 0 }  // Change these coordinates
```

### Change Zoom Level
Edit the `zoom` property:
```javascript
zoom: 2  // Lower = zoomed out, Higher = zoomed in
```

### Change Map Style
The map includes a custom style that hides points of interest. You can modify the `styles` array in the map initialization or remove it entirely for the default Google Maps style.

### Change Title
Edit the header text in the HTML:
```html
<h1>Friends Around the World</h1>
```

## Troubleshooting

**Map not loading:**
- Check that your Google Maps API key is correct
- Verify the Maps JavaScript API is enabled in Google Cloud Console
- Check browser console for errors (F12)

**Friend locations not appearing:**
- Verify your Google Sheets URL is correct
- Make sure the sheet is published to the web as CSV
- Check that column names are exactly: `Name`, `Latitude`, `Longitude`
- Verify coordinates are valid numbers

**CORS errors:**
- Make sure your Google Sheet is published to the web (not just shared)
- If testing locally, try using a local server or deploy to a hosting service

## Privacy Note

Since this map is publicly accessible, be mindful about:
- Only using approximate locations if friends prefer privacy
- Not including sensitive information
- Ensuring friends consent to having their location shared

## License

Free to use and modify as needed.
