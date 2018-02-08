'use strict'
var google_maps_api_key = 'AIzaSyCvwOFiIK3mt9MdD8gwlGtLmwJiKo-bZPg';
var request_lib = require('request');
var googlemaps = require('googlemaps');

function get_venue_data_via_gps(request, reponse)
{
  var latitude = request.query.lat ? request.query.lat : 43.652073;
  var longitude = request.query.long ? request.query.long : -79.382293;

  var publicConfig = {
    key: google_maps_api_key,
    stagger_time:       1000, // for elevationPath 
    encode_polylines:   false,
    secure:             true // use https 
    // proxy:              'http://127.0.0.1:9999' // optional, set a proxy for HTTP requests 
  };
  var gmAPI = new googlemaps(publicConfig);

  var searchParams = {
    "location": JSON.stringify(latitude) + ',' + JSON.stringify(longitude),
    "radius": '50', // In meters
    // "types": ['restaurant'] // types is optional
  }
  
  gmAPI.placeSearch(searchParams, function(err, places){
    places.results.forEach(place => {
      console.log(place);
    });
  });
}

module.exports.get_venue_data_via_gps = get_venue_data_via_gps;