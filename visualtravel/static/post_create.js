
/*
var marker;
const mapArea = document.getElementById("map");

console.log("hello there");

function placeMarker(location) {
  if ( marker ) {
    marker.setPosition(location);
  } else {
    marker = new google.maps.Marker({
      position: location,
      map: map,
      animation: google.maps.Animation.BOUNCE,
      clickable: true,
    });
  }

  console.log("place marker is activated");

  $("#id_latitude").val(location.lat());
  $("#id_longitude").val(location.lng());

}
google.maps.event.addListener(map, 'click', function(event) {
  console.log("hi there");
  console.log(event);
  placeMarker(event.latLng);
});

mapArea.event.addEventListner(mapArea, 'click', function(event) {
  console.log("hello hello");
})

*/